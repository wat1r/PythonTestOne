from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException

client = ZhihuClient()
user = 'water8990@sina.com'
pwd = 'wz8962260'
try:
    client.login(user, pwd)
    print(u"登陆成功!")
except NeedCaptchaException:  # 处理要验证码的情况
    # 保存验证码并提示输入，重新登录
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login(user, pwd, captcha)

client.save_token('token.pkl')  # 保存token
# 有了token之后，下次登录就可以直接加载token文件了
# client.load_token('filename')
