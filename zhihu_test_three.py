from zhihu_oauth import ZhihuClient, Article

client = ZhihuClient()

client.load_token('token.pkl')
# me = client.me()

# question = client.question(35166763)
question = client.question(27946261)  # 怎样从零开始学习骑大排摩托车？

# client.topic()

# topic = client.topic(19942170)
# for people in topic.best_answerers:
#     print(people.name)

# article = client.article(27430620)
#
# if isinstance(article,Article):
#     print(article)

# article.save('test1')

# print(question.title)
#
count = 0
for answer in question.answers:
    count += 1
    print(answer.author.name, answer.voteup_count)
#     answer.save(question.title)
print('-------count:',count)
