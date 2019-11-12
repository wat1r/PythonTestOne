import re
from bs4 import BeautifulSoup as BeautifulSoup
# import cursor as cursor
import pymysql as sql
import requests
from fake_useragent import UserAgent

sqlarg = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'house-chengdu',
    'charset': 'utf8'
}

conn = sql.connect(**sqlarg)
cursor = conn.cursor()

ua = UserAgent()

headers = {'User-Agent': ua.random}


class House(object):

    # 获取区域的url和name
    def get_area_url(self):
        response = requests.get('https://cd.lianjia.com/ershoufang/', headers=headers)
        response.encoding = 'utf8'
        result = response.text
        area_name = re.findall(r'<a href="/ershoufang/(.*?)/"  title=".*?">.*?</a>', result)
        print(area_name)
        area_name.pop(0)
        area_url = []
        for tmp in area_name:
            print(tmp)
            area_url.append('https://cd.lianjia.com/ershoufang/{}'.format(tmp))
        self.name_url = tuple(zip(area_name, area_url))
        return None

    # 获取页码
    def get_page(self, url):
        response = requests.get(url, headers=headers)
        response.encoding = 'utf8'
        result = response.text
        page = re.findall(r'{"totalPage":(.*?),"curPage":1}', result)
        if page:
            return page[0]
        else:
            return '0'

    # 获取小区域的URL:这里主要用于当大区域超过100页时，就需要缩小区域抓取。
    def get_smallarea(self, url):
        response = requests.get(url, headers=headers)
        response.encoding = 'utf8'
        result = response.text
        smallarea_name = re.findall(r'<a href="/ershoufang/(.*?)/" >.*?</a>', result)
        smallarea_url = []
        for tmp in smallarea_name:
            smallarea_url.append('https://cd.lianjia.com/ershoufang/{}'.format(tmp))
        return smallarea_url

    # 获取HTML信息
    def get_text(self, url):
        response = requests.get(url, headers=headers)
        response.encoding = 'utf8'
        self.result = response.text
        self.soup = BeautifulSoup(self.result, 'lxml')
        return None

    # 获取标题
    def get_title(self):
        title_soup = self.soup.find_all('div', class_="title")
        self.title = []
        for i in title_soup:
            try:
                title = i.a.text
                if ' ' in title:
                    title = title.replace(' ', '')
                if len(title) > 34:
                    title = title[:35]
                self.title.append(title)
            except AttributeError as e:
                pass
        return None

    # 获取房子相关信息
    def get_houseinfo(self):
        houseinfo_soup = self.soup.find_all('div', class_='houseInfo')
        self.houseinfo = []
        self.url = []
        for j in houseinfo_soup:
            self.url.append(j.a.get('href'))
            middle_list = j.text.replace(' ', '').split('|')
            for q in middle_list[1:]:
                if '室' not in q and '平米' not in q:
                    middle_list.remove(q)
            self.houseinfo.append(middle_list)
        floor_soup = self.soup.find_all('div', class_='positionInfo')
        self.floor = []  # 楼层信息
        self.area = []  # 所在区域
        for k in floor_soup:
            middle = k.text.split('-')
            self.floor.append(middle[0].strip())
            self.area.append(middle[1].strip())
        return None

    # 获取房子价格信息
    def get_price(self):
        price_soup = self.soup.find_all('div', class_='totalPrice')
        self.totalprice = []
        for n in price_soup:
            self.totalprice.append(n.text)

        unitprice_soup = self.soup.find_all('div', class_='unitPrice')
        self.unitprice = []
        for p in unitprice_soup:
            self.unitprice.append(p.text)

        return None

    # 处理数据
    def modify_price(self):
        for i in self.houseinfo:
            try:
                if i[2]:
                    i[2] = i[2].replace('平米', '')
            except IndexError as e:
                pass
        for j, k in enumerate(self.totalprice):
            self.totalprice[j] = k.replace('万', '')

        for n, m in enumerate(self.unitprice):
            _ = m.replace('单价', '')
            _ = _.replace('元/平米', '')
            self.unitprice[n] = _
        return None

    # 将获取到的房子所有信息打包
    def zipp(self):

        self.information = list(self.title, self.houseinfo, self.floor, self.area, self.unitprice,
                                self.totalprice, self.url)
        for i in self.information:  # 移除掉车库
            if len(i[2]) < 3:
                self.information.remove(i)
        return None

    # 写入数据库Mysql
    def write(self, title, information):
        for i in information:
            try:
                if len(information[1]) < 3:
                    continue
                elif not i:
                    continue
            except IndexError:
                continue

            try:
                insert_info = '''insert into %s(title,apartment,structure,built_area,floor,area,unitprice,totalprice,url) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s');''' % (
                    title, i[0], i[1][0], i[1][1], i[1][2], i[2], i[3], i[4], i[5], i[6])
                cursor.execute(insert_info)
            except IndexError:
                continue

        conn.commit()
        return None

    def qidong(self):
        print("+++++++++")
        self.get_area_url()
        print("-------")
        for name, url in self.name_url:
            create_tb = '''create table if not exists {}(
                                  id int primary key auto_increment,
                                  title varchar(35) not null,
                                   apartment varchar(15) not null,
                                    structure varchar(10) not null,
                                   built_area float not null,
                                    floor varchar(30) not null,
                                 area varchar(10) not null,
                                 unitprice int not null,
                                  totalprice int not null,
                                  url varchar(80) not null
                                );'''.format(name)
            cursor.execute(create_tb)


if __name__ == '__main__':
    house = House()
    house.qidong()
