from zhihu_oauth import ZhihuClient, Article, SearchType

client = ZhihuClient()

client.load_token('token.pkl')

# search = client.search('7sDream', SearchType.PEOPLE)
# print(search)

# for result in client.search('摩托车赛事', SearchType.TOPIC):
#     topic = result.obj
#
#     print(topic.name, topic.question_count)

# for result in client.search_unfold("摩托车"):
#     # result is SearchResult object
#     r = result
#     print(r.highlight_title, r.highlight_desc)
#     print(r.obj)
#     print('-' * 20)