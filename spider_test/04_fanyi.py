# coding=utf-8
import requests
import json
import sys

# query_string = sys.argv[1]

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"}

post_data = {
    "query": "人生苦短,我用Python",
    "from": "zh",
    "to": "en",
}

post_url = "http://fanyi.baidu.com/basetrans"

r = requests.post(post_url, data=post_data, headers=headers)
print(r.content.decode())

# dict_ret = json.loads(r.content.decode())
# ret = dict_ret["trans"][0]["dst"]
# print("result is :", ret)
