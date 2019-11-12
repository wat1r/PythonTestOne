from zhihu_oauth import ZhihuClient, Answer, Question, Article, Column, Pin

client = ZhihuClient()

client.load_token('token.pkl')

# topic = client.topic(20175669)#摩托车旅行
topic = client.topic(19940272)  # 摩托车赛事



# for question in topic.unanswered_questions:
#     print(question.title)

# print(client.TopicIndex(19940272))
#
# print(topic.activities)
# print(topic.best_answers)
# print(topic.best_answers)

# for answer in topic.best_answers:
#     print(answer.author.name, answer.voteup_count)

# print(topic.next())

for act in topic.activities:
    if isinstance(act, Answer):
        print("1Answer:",act.author.name)
        # pass
        # act.save(topic.name)
    elif isinstance(act, Column):
        print("Column:", act)
        # act.save(act.name)
    elif isinstance(act, Article):
        print("Article:", act)
        # act.save(act.name)
    elif isinstance(act, Pin):
        print("Pin:", act)
        # act.save(act.name)
    else:
        for answer in act.answers:
            print(answer.author.name, answer.voteup_count)
            # answer.save(act.title)
        # assert (isinstance(act, Question))
        # pass
