import re
import time

import requests


def all_list_page(http_link_universal):
    number_page = 1
    page = True
    while page:  #
        time.sleep(2)
        page = get_page(http_link_universal, number_page)
        number_page += 1
        pars_page(page)


def get_page(http_link_universal, number_page):
    page = requests.get(http_link_universal.format(number_page))
    if 'По вашему запросу ничего не найдено.' in page.text:
        return False
    # print(http_link_universal.format(number_page))
    print('nunber page parsed = ', number_page)
    # print(r.text)
    return page


def pars_page(page):
    # print(page.text)
    if page == False:
        print('done')
        exit()
    pattern_mail = '[a-z\.A-Z0-9_\-]+@[a-zA-Z0-9]+\.[a-z]+'
    pattern_phon = '[7-8]{1}9{1}[0-9]{9}'
    save_result(re.findall(pattern_mail, page.text), (re.findall(pattern_phon, page.text)))


def save_result(email, phon):
    if email == phon == '':
        with open('phon.txt', 'w') as file_phon:
            pass
        with open('mail.txt', 'w') as file_email:
            pass
    with open('phon.txt', 'a') as file_phon:
        for phon_number in phon:
            file_phon.write(phon_number + '\n')
    with open('mail.txt', 'a') as file_email:
        for email_list in email:
            file_email.write(email_list + '\n')


def main():
    save_result('', '')
    http_link_universal = 'https://omsk.mlsn.ru/pokupka-nedvizhimost/?district=52401372%2C52401376%2C52401380%2C52401382%2Ccenter&objectTypeId=1%2C2%2C3&onlyOwners=1&page={}&priceMax=70000&priceUnitId=2'
    all_list_page(http_link_universal)


if __name__ == '__main__':
    main()
