import requests
import pretty_errors
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)

headers = {
    'User-Agent':ua.random,
    'x-requested-with': 'XmlHttpRequest',
    'referer': 'https://shimo.im/login?redirect_url=https%3A%2F%2Fshimo.im%2Fdashboard%2Fused',

}

print(headers)
data = {
    'email': '1065968861@qq.com',
    'mobile': '+86undefined',
    'password': 'test123456',
    
}

s = requests.Session()

login_url = 'https://shimo.im/lizard-api/auth/password/login'

# res = s.post(url=login_url, headers=headers, data=data)
# print(res.text)
# if res.status_code == 204:
#     print('登录成功！')

# 访问个人工作台
url = 'https://shimo.im/profile'
response = s.get(url, headers=headers).content.decode()

with open('./task2/shimo.html', 'w', encoding='utf-8') as f1:
    f1.write(response)