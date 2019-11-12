from __future__ import print_function  # 使用python3的print方法
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('token.pkl')  # 加载token文件
# 显示自己的相关信息
me = client.me()

# 获取最近 5 个回答
for _, answer in zip(range(5), me.answers):
    print(answer.question.title, answer.voteup_count)

print('----------')

# 获取点赞量最高的 5 个回答
for _, answer in zip(range(5), me.answers.order_by('votenum')):
    print(answer.question.title, answer.voteup_count)

print('----------')

# 获取最近提的 5 个问题
for _, question in zip(range(5), me.questions):
    print(question.title, question.answer_count)

print('----------')

# 获取最近发表的 5 个文章
for _, article in zip(range(5), me.articles):
    print(article.title, article.voteup_count)
