# get_response.py

import requests, browsercookie
from bs4 import BeautifulSoup
import pandas as pd

# global variables
# ================

BASE_URL = 'https://cbs.app.box.com'
SUFFIX = '/folder/0/search'
URL = BASE_URL + SUFFIX
QUERY = "*.pst"
PAGE_SIZE = '1000'
PAGE_NUMBER = '0'

# CSS selectors
# =============

CONTENT_CSS = ['ol', 'file-list-body list-view']
TITLE_CSS = ['div', 'item-name file-list-name']
MODIFIED_CSS = ['div', 'item-modified-and-size']
BREADCRUMBS_CSS = ['div', 'item-breadcrumbs']

# functions
# =========

def extract_col(row):
    """iterates over a beautifulsoup list of strings and returns all the rows"""
    col = []
    for x in row:
        col[x] = extract_row(x)
    return col
    

def extract_row(result_list):
    """takes a list element in a soup element object and returns parsed data """
    title = result_list.find('div', attrs = { 'class' : 'item-name file-list-name' }).text
    modified = result_list.find('div', attrs = { 'class' : 'item-modified-and-size' }).text
    breadcrumbs = result_list.find('div', attrs = { 'class' : 'item-breadcrumbs' }).text
    href = BASE_URL + result_list.find('a')['href']
    row = [title, modified, breadcrumbs, href]
    return row
    

def extract_table(soup):
    """takes soup object and class of data to be extracted"""
    result_list = soup.find('ol', attrs = { 'class' : 'file-list-body list-view' })
    return result_list

def make_soup(response_body):
    """takes response content and returns BeautifulSoup object"""
    soup = BeautifulSoup(response_body, 'lxml')
    return soup

def get_response(url, params):
    """attach cookies to request and return body of GET request"""
    # dump session cookies from browser 
    cj = browsercookie.firefox()
    # use cookies for get request
    response = requests.get(url=url, params=params, cookies=cj)
    # make soup out of response body
    response_body = response.content
    return response_body

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
    result_list = extract_table(soup_object)
    data = extract_col(result_list)
    

    print(data) # !TODO: extract relevant info from this list 
    print(type(data))
    print('=========================================')

