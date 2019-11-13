import requests
import re


def parse_page(url):
    headers = {
        "user-agent": " Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    response = requests.get(url, headers)
    text = response.text
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    content_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>', text, re.DOTALL)
    contents = []
    for content in content_tags:
        # print(content)
        x = re.sub(r'<.*?>', "", content)
        # print(x.strip())
        contents.append(x.strip())

    peoms = []
    for value in zip(titles, dynasties, authors, contents):
        title, dynasty, author, content = value
        peom = {
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'content': content
        }
        peoms.append(peom)

    # print(peoms)

    for peom in peoms:
        print(peom)
        print("*" * 30)


def main():
    for i in range(1, 11):
        url = "https://www.gushiwen.org/default_%s.aspx" % i
        print(url)
        parse_page(url)


if __name__ == '__main__':
    # main()
    l1 = ['1', '3', '4']
    l2 = ['1', '3', '6']
    # l1.append(l2)
    print(l1+l2)
