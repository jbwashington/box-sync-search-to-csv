import requests, browsercookie
from bs4 import BeautifulSoup as bs

url='https://cbs.app.box.com/folder/0/search'
query='*.pst'
page_number='0'

def scrape_page(url, query, page_number):

    """takes the search URL string, search, and page number;
    returns the results of a PST search in Box.com"""

    query = 'query'
    page_number = 'pageNumber'

    payload = {
            'query': query,
            'pageSize' : '1000',
            'sortDirection' : 'desc',
            'folderID' : '0',
            'pageNumber' : page_number
            }

    # dump session cookies from browser into object
    cj = browsercookie.load()

    # use cookie object in GET request
    r = requests.get(url, params=payload, cookies=cj)

    # store response to GET request in object
    response_body = r.content

    # instantiate BeautifulSoup object from response object
    soup = bs(response_body, "lxml")

    # find all the link items with the class that contains the relevant info from the response body

    file_list = soup('ol', attrs={'class': "file-list-body"})

    if len(file_list) == 0:
        print("nothing showing, so you're likely not authenticated in browser.")
    else:
        count = []
        print('result count: ', len(file_list))

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

