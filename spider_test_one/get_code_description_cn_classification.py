def get_code_and_description():
    final_code_desc = open('final_code_desc.txt', 'wt', encoding="utf-8")
    cnt = 0
    # with open(r'C:\Users\FrankCooper\Desktop\cn_txt\destination\destination_.txt', "r", encoding="utf-8") as f:
    #     line = f.readline()  # 调用文件的 readline()方法
    final_set = set()
    final_list = list()
    for line in open(r'C:\Users\FrankCooper\Desktop\cn_txt\destination_all.txt', "r", encoding="utf-8"):
        line = line.replace("\r", "").replace("\n", "")

        split = line.split(":")
        final_list += split

        # print(final_set)
        # cnt += 1
        # if cnt == 1000:
    final_list.sort()
    final_set = set(final_list)
    final_set.remove('')
    for item in final_set:
        final_code_desc.write(item + '\n')
        print(item)
            # exit()


if __name__ == '__main__':
    get_code_and_description()
