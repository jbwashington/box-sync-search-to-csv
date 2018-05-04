# get_response.py
# ===============
import requests, browsercookie
from bs4 import BeautifulSoup
import pandas as pd

# global variables
# ================
BASE_URL = 'https://cbs.app.box.com'
URL =  'https://cbs.app.box.com/folder/0/search'
QUERY = "*.pst"
PAGE_SIZE = '1000'
PARENT_CSS = ['ol', 'file-list-body list-view']
PAGE_NUMBER = '0'

# functions
# =========
def get_response(url, params):
    """attach cookies to request and return body of GET request"""
    # dump session cookies from browser 
    cj = browsercookie.firefox()
    # use cookies for get request
    response = requests.get(url=url, params=params, cookies=cj)
    # make soup out of response body
    response_body = response.content
    return response_body

def extract_data(soup, div, css):
    """takes soup object and class of data to be extracted"""
    # result_list = soup.select(selector)
    result_list = soup.find(div, attrs={ 'class' : css })
    return result_list

def make_soup(response_body):
    """takes response content and returns BeautifulSoup object"""
    soup = BeautifulSoup(response_body, 'lxml')
    return soup

def send_payload(query, page_size='1000', page_number='0'):
    """takes a search parameter string and page number, returns dictionary with payload """
    payload = {
            'query': query, 
            'itemSize' : '', 
            'pageSize' : page_size, 
            'sortDirection' : 'asc', 
            'updatedTime' : '', 
            'kinds' : 'name',
            'metadata' : '',
            'folderID' : '0',
            'pageNumber' : page_number
            }
    return payload

if __name__ == '__main__':

    print('=========================================')
    payload = send_payload(QUERY, PAGE_SIZE, PAGE_NUMBER)
    response = get_response(URL, payload)
    soup_object = make_soup(response)
    result_list = extract_data(soup_object, PARENT_CSS[0], PARENT_CSS[1])

    print(result_list) # !TODO: extract relevant info from this list 

    print('=========================================')

