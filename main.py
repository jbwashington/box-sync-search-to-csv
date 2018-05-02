# main.py

import requests, browsercookie, sqlite3, os, re, config
from bs4 import BeautifulSoup as bs
import pandas as pd

# change these in config.py
# =========================
url = config.TEST_URL
url = config.URL
url = config.QUERY
url = config.PAGE_NUMBER




def main():
    """takes no arguments, main function"""
    # dump session cookies from browser into object
    # use cookie object in GET request
    # instantiate BeautifulSoup object from response object
    # find all the link items with the class that contains the relevant info from the response body
    # assign each result to a variable
    # iterate through each result and put it into a pandas dataframe
    print('main() finished with no errors: TRUE')

if __name__ == '__main__':
    main()
