# parse_response.py

import requests, browsercookie
from bs4 import BeautifulSoup
import pandas as pd

# functions
# =========

def get_result(soup):
    """takes a Soup Object returns a list """
    title = soup.find("div", class_='item-name file-list-name')
    modified = soup.find("div", class_='item-modified-and-size')
    breadcrumbs = soup.find("div", class_='item-breadcrumbs')
    href = soup.find("a", class_="item-name-link")
    result = [title.text, modified.text, breadcrumbs.text, href.attrs['href']]
    return result


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

