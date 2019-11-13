from selenium import webdriver
import time
import string
import re
import requests
from bs4 import BeautifulSoup

parser_cn_file = open('parser_cn_file.txt', 'wt', encoding='utf-8')
#11638 25843
if __name__ == '__main__':
    url_format = "http://ztflh.xhma.com/html/{0}.html"
    # for i in range(22774, 45836 + 1):
    for i in range(9580, 11633 + 1):
        print(i)
        url = url_format.format(i)
        # print(url)
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        time.sleep(0.5)

        content = soup.select(".category-item")
        if content and content.__len__() == 1:
            code = soup.select(".category-code")[0].text.strip()
            desc = soup.select(".category-title")[0].text.strip()
            # print(code, "|", desc, ":")
            select = soup.select('ol > li')
            final_str = ""
            for j in range(select.__len__() - 2, 0, -1):
                final_str += select[j].text
                if j != select.__len__() - 1:
                    final_str += ","
            print(code, "|", desc, ":", final_str)
            final_str = code + "|" + desc + ":" + final_str
            parser_cn_file.write(final_str+"\n")
        parser_cn_file.flush()
        # pass

        # webdriver.get



        # if i == 9063:
        #     exit()

print("end")
