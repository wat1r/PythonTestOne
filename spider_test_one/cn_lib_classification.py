from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


class Stack:
    """用栈维护搜索顺序"""

    res_file = open('res_file_one.txt', 'wt', encoding='utf-8')

    # ctrl_list = ["Q959", "Q959.1|无脊椎动物", "Q959.19|环节动物门", "Q959.195|",
    #              "Q959.197|星虫纲", "Q959.197|", "星虫纲|","Q959.3|脊椎动物",
    #              "Q959.4|鱼纲","Q959.27|毛颚动物门"]
    # ctrl_list = ["Q959", "Q959.1|无脊椎动物", "Q959.22|节肢动物门", "Q959.227|有气管亚门",
    #              "Q959.229|多足纲", "Q959.229+.1|综合亚纲", "Q959.229+.2|", "Q959.229+.3|倍足亚纲",
    #              "Q959.229+.4|触颚目", "Q959.229+.5|唇颚目"]

    # ctrl_list = ['J31|雕塑技法', 'J3|雕塑', 'J|艺术', 'J31', 'A11', 'F23', 'B71']
    # ctrl_list_level_1 = ['B', 'F']
    # ctrl_list_level_1 = ['X', 'Z']
    ctrl_list_level_1 = ['U']
    ctrl_list_level_2 = ['V4', '[V7]']
    # ctrl_list_level_3 = ['B91', 'B92', 'B93', 'B71', 'F23', 'F239']
    ctrl_list_level_3 = ['K61']

    ctrl_set = set()

    unnormal_flag = 0

    # "Q954" "Q954.43+1", "Q954.4|动物胚胎学（动物发生学、动物胎生学）"
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def insert_symbol_into_list(self, m_list):
        '''
        process special situation cause there are one item in one box which must have two
        this function fill there unnormal box into '---'
        e.g. src dest
        {['Q959.212+.2', 'Q959.212+.3', 'Q959.212+.3'] |
        'Q959.212+.2', '---', 'Q959.212+.3', '---', 'Q959.212+.3', '---' }
        { ['Q959.229+.9','Q959.229+.1', '综合亚纲', 'Q959.229+.2', 'Q959.229+.3', 'Q959.229+.2',
        '倍足亚纲', "Q959.229+.2", 'Q959.229+.6', '唇足亚纲', 'Q959.229+.6']|
              ['Q959.229+.9', '---', 'Q959.229+.1', '综合亚纲', 'Q959.229+.2', '---', 'Q959.229+.3', '---', 'Q959.229+.2',
              '倍足亚纲', 'Q959.229+.2', '---', 'Q959.229+.6', '唇足亚纲', 'Q959.229+.6', '---']}
        :param m_list:
        :return:
        '''
        for i in range(0, len(m_list)):
            # print(m_list[i])
            flag = False
            if self.check_if_contains_letter(m_list[i]):
                flag = True
            if (i + 1) < len(m_list):
                if self.check_if_contains_letter(m_list[i + 1]):
                    flag = flag and True
                else:
                    flag = False
            if flag:
                m_list.insert(i + 1, "---")
                flag = False
        if self.check_if_contains_letter(m_list[len(m_list) - 1]):
            m_list.insert(len(m_list), "---")

    def check_if_contains_letter(self, str):
        contents = str
        pattern = r".*([a-z]|[A-z]).*"
        compile_res = re.search(pattern, contents)
        if compile_res:
            pattern = u'[\u4e00-\u9fa5]'
            compile_res = re.search(pattern, contents)
            if compile_res:
                return False
            else:
                return True
        else:
            return False

    def check_if_is_normal(self, m_list):
        first_str_cnt = 0
        second_str_cnt = 0
        for item in m_list:
            compile_res = self.check_if_contains_letter(item)
            if compile_res:
                first_str_cnt += 1
            else:
                second_str_cnt += 1
        bool_res = first_str_cnt == second_str_cnt
        print("******bool_res:", bool_res)
        return bool_res

    def generate_m_list_len(self, m_next_validation):
        '''
        generate list length
        :param m_next_validation:
        :return:
        '''
        parent_len_validation = len(m_next_validation)
        if len(m_next_validation) % 2 == 1:
            parent_len_validation += 1
        final_len_validation = (int(parent_len_validation / 2))
        return final_len_validation

    def final_str_write(self, i, q):
        '''
        write str to the file
        :param i:
        :param q:
        :return:
        '''
        final_str = ''
        if q.isEmpty():
            pass
        else:
            max_size = q.size() - 1
            for t in range(max_size, -1, -1):
                if i != max_size:
                    final_str = final_str + ':' + q.items[t]
                else:
                    final_str = q.items[t]
            print("final_str:", final_str)
            self.res_file.write(final_str + '\n')

    def continue_detection_once_more(self, driver, i, m, q):
        m_next_validation = self.click_and_find_elements(q, driver, i)
        final_len_validation = self.generate_m_list_len(m_next_validation)
        if final_len_validation == 1 or final_len_validation == 0:
            m_next_validation_continue = self.click_and_find_elements(q, driver, i)
            m_len_continue = self.generate_m_list_len(m_next_validation_continue)
            if m_len_continue > 1:
                q.push(m_next_validation[0] + '|' + m_next_validation[1])
                for i in range(1, m_len_continue + 1):
                    self.next_level_detection(i, m_next_validation_continue, m_len_continue, q, driver, '')
                    if i == m_len_continue:
                        q.pop()
                        driver.back()
            m_len = self.generate_m_list_len(m)
            final_str_validation = m_next_validation[0] + "|" + m_next_validation[1]
            # the str is equals to the next level
            if q.peek() == final_str_validation:
                self.final_str_write(i, q)
                # if has more than one item ,don't back
                if m_len < 2:
                    q.pop()
                    driver.back()
                else:
                    q.pop()
                    driver.back()
            else:
                q.push(final_str_validation)
                self.final_str_write(i, q)
                q.pop()
                driver.back()
        else:
            for i in range(1, final_len_validation + 1):
                self.next_level_detection(i, m_next_validation, final_len_validation, q, driver, '')
                if i == final_len_validation:
                    q.pop()
                    driver.back()

    def next_level_detection(self, i, m, len0, q, driver, next_str):
        # if i == len0:
        #     q.pop()
        #     driver.back()
        # print("next_str:" + next_str)
        # print("*" * 20)
        # print("*" * 20)
        # print(m[0 + (i - 1) * 2] + ':' + m[(i - 1) * 2 + 1] + ':' + next_str)
        # unnormal_flag = 0
        print("i:", i)
        # pattern = r'.*([a-z]|[A-z]).*'
        if not self.check_if_is_normal(m):
            self.insert_symbol_into_list(m)
            print("insert_into_list:", m)
        # if self.unnormal_flag == 1 :
        #     first_str = m[0 + (i - 1) * 2 - 1]
        #     second_str = m[(i - 1) * 2]
        #     print("----unnormal_flag==1,first_str:%s,second_str:%s" % (first_str, second_str))
        # else:
        first_str = m[0 + (i - 1) * 2]
        second_str = m[(i - 1) * 2 + 1]
        print("====normal_flag==1,first_str:%s,second_str:%s" % (first_str, second_str))
        # compile_res = re.search(pattern, second_str)
        # if compile_res:
        #     second_str = ''
        #     self.unnormal_flag = 1
        time.sleep(0.5)
        q.push(first_str + '|' + second_str)
        m_next = self.click_and_find_elements(q, driver, i)
        parent_len5 = len(m_next)
        if len(m_next) % 2 == 1:
            parent_len5 += 1

        len5 = (int(parent_len5 / 2))
        # if i==len0:
        #     q.pop()
        #     driver.back()
        # pop5 = q.peek()
        if len5 == 1 or len5 == 0 or len0 == 1:
            i = 1
            # next_str = m_next[0 + (i - 1) * 2] + '|' + m_next[(i - 1) * 2 + 1] + ':' + next_str
            # print("len5==1,next_str", next_str)
            l_str = m_next[0] + "|" + m_next[1]
            # self.ctrl_set.add(l_str)
            if q.peek() != l_str:
                q.push(l_str)
            self.continue_detection_once_more(driver, i, m, q)
            # if i == len0:
            #     q.pop()
            #     driver.back()

            # self.final_str_write(i, q)

            return
        else:
            for i in range(1, len5 + 1):
                # if q.peek() not in self.ctrl_list:
                #     q.pop()
                #     driver.back()
                #     break
                # next_str = q.peek() + ':' + next_str
                # next_str = pop5 + ':' + next_str
                self.next_level_detection(i, m_next, len5, q, driver, next_str)
                if i == len5:
                    # self.unnormal_flag = 0
                    q.pop()
                    driver.back()

    def click_and_find_elements(self, q, driver, i):
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[{0}]/div".format(i)).click()
        except Exception as e:
            try:
                driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div[{0}]/div".format(i)).click()
            except Exception as e1:
                q.pop()
                driver.back()
                self.click_and_find_elements(q, driver, i)
        time.sleep(0.5)
        try:
            m_next = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]").text.split('\n')
        except Exception as e:
            m_next = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]").text.split('\n')
        return m_next

    def run(self):
        driver = webdriver.Chrome(r"E:\DevTools\chromedriver2.39\chromedriver.exe")  # 用chrome浏览器打开
        driver.get("http://ztflh.xhma.com/")
        time.sleep(2)
        driver.maximize_window()
        # m1 = driver.find_element_by_xpath("//div[@class='row category-list']/div")
        m1 = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]").text.split('\n')
        len1 = (int(len(m1) / 2))
        # 第一层遍历
        for i in range(1, len1 + 1):
            if m1[0 + (i - 1) * 2] not in self.ctrl_list_level_1:
                continue
            q = Stack()
            level1_str = m1[0 + (i - 1) * 2] + '|' + m1[(i - 1) * 2 + 1] + ':::'
            print(level1_str)
            self.res_file.write(level1_str + '\n')
            q.push(m1[0 + (i - 1) * 2] + '|' + m1[(i - 1) * 2 + 1])
            m2 = self.click_and_find_elements(q, driver, i)
            len2 = (int(len(m2) / 2))
            pop2 = q.peek()
            # 第二层遍历
            for i in range(1, len2 + 1):
                if len2 > 1:
                    self.next_level_detection(i, m2, len2, q, driver, "")
                    self.res_file.flush()
                if i == len2:
                    q.pop()
                    driver.back()
            if i == len1:
                q.pop()
                driver.back()


if __name__ == '__main__':
    main = Stack()
    main.run()
    main.res_file.close()
    # s = Stack()
    # # print(s.isEmpty())
    # s.push(4)
    # s.push('dog')
    # # print(s.peek())
    # s.push(True)
    # # print(s.size())
    # # print(s.isEmpty())
    # s.push(8.4)
    # # print(s.pop())
    # # print(s.pop())
    # print(s.size())
    # for j in range(s.size() - 1, -1, -1):
    #     print(s.items[j])
