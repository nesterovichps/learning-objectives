import requests
import time
def send_sms(phone,params):
    params['phone']=phone
    print(phone)
    print(requests.get(url,params=params).text)
url='https://semysms.net/api/3/sms.php'
TOKEN='953cc1ada634323447cecc90f10eba04'
device='active'
# phone='+79503333343'

msg='test'
params={'token':TOKEN,'device':device,'msg':msg}
# print(requests.get(url,params=params).text)
with open('number.txt','r',encoding='utf-8') as file:
    for line in file.readlines():
        phone='+7'+str(line.strip())[-10:]
        send_sms(phone,params)
        time.sleep(2)