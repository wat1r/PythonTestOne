import requests
from fake_useragent import UserAgent

ua = UserAgent()

headers = {'User-Agent': ua.random}


print(ua.random)

url = 'https://su.lianjia.com/ershoufang/'

resp = requests.get(url, headers=headers)

print(resp)
