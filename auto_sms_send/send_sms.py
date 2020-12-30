import requests
import time
def send_sms(phone,params):
    with open('used_number.txt','r+',encoding='utf-8') as number_file:
        if phone[1:] not in number_file.read():
            print('good')
            params['phone'] = phone
            print(phone)
            print(requests.get(url,params=params).text)
            number_file.writelines(phone[1:] + '\n')
        else:
            print('bad')
            print(phone)
url='https://semysms.net/api/3/sms.php'
TOKEN='953cc1ada634323447cecc90f10eba04'
device='active'


msg='''Продам Вашу квартиру Быстро, Качественно, Без нервов!
Петр. Специалист по недвижимости и ипотеки Мегаполис. 
тел 89503333343 
https://onlinevizitka.com/petr_megapolis/
Звоните! Сейчас самое время продавать.'''
params={'token':TOKEN,'device':device,'msg':msg}
with open('number.txt','r',encoding='utf-8') as file:
    for line in file.readlines():
        phone='+7'+str(line.strip())[-10:]
        send_sms(phone,params)
        time.sleep(2)