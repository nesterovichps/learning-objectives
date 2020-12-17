import requests ,time
from bs4 import BeautifulSoup as bs
def all_list_page( http_link_universal):
    number_page=1
    page=True
    while page:#
        time.sleep(100)
        page=get_page(http_link_universal,number_page)
        number_page+=1
        pars_page(page)
def get_page(http_link_universal,number_page):
    page=requests.get(http_link_universal.format(number_page))
    if 'По вашему запросу ничего не найдено.' in page.text:
        return False
    print(http_link_universal.format(number_page))
    print(number_page)
    # print(r.text)
    return page
def pars_page():
    pass

def save_result():
    pass

def main():
    http_link_universal='https://omsk.mlsn.ru/pokupka-nedvizhimost/?district=52401372%2C52401376%2C52401380%2C52401382%2Ccenter&objectTypeId=1%2C2%2C3&onlyOwners=1&page={}&priceMax=70000&priceUnitId=2'
    all_list_page( http_link_universal)

if __name__ == '__main__':
    main()

