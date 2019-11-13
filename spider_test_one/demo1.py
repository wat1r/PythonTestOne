from bs4 import BeautifulSoup
from bs4.element import NavigableString
from bs4.element import Comment

import re


text = "the number is 20.50"
r = re.compile('\d+\.?\d*')
res = re.search(r, text)
print(res.group())