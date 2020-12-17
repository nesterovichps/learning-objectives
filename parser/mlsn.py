import requests
from bs4 import BeautifulSoup as bs
def all_list_page( http_link_universal):
    get_page(http_link_universal,1)

def get_page(http_link_universal,number_page):
    r=requests.get(http_link_universal.format(number_page))

    print(http_link_universal.format(number_page))
    print(r.text)
def pars_page():
    pass
def save_result():
    pass
def main( http_link_universal):
    all_list_page( http_link_universal)

if __name__ == '__main__':
    http_link_universal='https://omsk.mlsn.ru/pokupka-nedvizhimost/?district=52401372%2C52401376%2C52401380%2C52401382%2Ccenter&objectTypeId=1%2C2%2C3&onlyOwners=1&page={}&priceMax=70000&priceUnitId=2'
    main( http_link_universal)

