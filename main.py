import requests, browsercookie
from bs4 import BeautifulSoup as bs

def get_results():
    """takes no arguments, returns the results of a PST search in Box.com"""

    payload = {
            'query': '*.pst', 
            'pageSize' : '500', 
            'sortDirection' : 'desc', 
            'folderID' : '0', 
            'pageNumber' : '0'
            }

    prefix = 'https://cbs.app.box.com'
    suffix = '/folder/0/search'

    # dump session cookies from browser into object
    cj = browsercookie.load()

    # use cookie object in GET request
    r = requests.get(prefix+suffix, params=payload, cookies=cj)

    # store response to GET request in object
    response_body = r.content

    # instantiate BeautifulSoup object from response object
    soup = bs(response_body, "lxml")

    # find all the link items with the class that contains the relevant info from the response body

    file_list = soup('ol', attrs={'class': "file-list-body"})

    if file_list is None:
        print("nothing showing, so you're likely not authenticated in browser.  log in to your account within Firefox, exit the browser, then retry.")
    else:
        count = []
        print('result count =>', len(file_list))

    file_titles = soup('a', attrs={'class': "item-name-link"})
    file_link = soup('a', attrs={'a': "href"})
    modified = soup('span', attrs={'span': "item-modified-date"})
    file_sizes = soup('div', attrs={'span': "item_size"})
    breadcrumbs = soup('span', 'item-breadcrumbs')

    file_list = {}

    for i in file_titles:
        title = i.get_text()
        file_list[title] = prefix + i.attrs['href']

    return file_list
