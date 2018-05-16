# get_response.py
import parse_response as pr

# GLOBAL VARIABLES
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

if __name__ == '__main__':

    print('=========================================')
    payload = pr.send_payload(QUERY, PAGE_SIZE, PAGE_NUMBER)
    response = pr.get_response(URL, payload)
    soup_object = pr.make_soup(response)
    table = pr.extract_table(soup_object, BASE_URL)
    # data = pr.extract_col(table)

    print(table) # !TODO: extract relevant info from this list 
    print(type(table))
    print('=========================================')

