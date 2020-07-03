import requests
import pretty_errors
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)

headers = {
    'User-Agent':ua.random,
    'x-requested-with': 'XmlHttpRequest',
    'referer': 'https://shimo.im/login?redirect_url=https%3A%2F%2Fshimo.im%2Fdashboard%2Fused',

}

data = {
    'email': '1065968861@qq.com',
    'mobile': '+86undefined',
    'password': 'test123456',
    
}
# print(headers)

# post
s = requests.Session()


url = 'https://shimo.im/lizard-api/auth/password/login'

res = s.post(url=url, headers=headers, data=data)
print(res.status_code)
print(res.content.decode())
# cookie
# with requests.Session() as s:
#     res = s.get('https://www.douban.com', headers=headers)
#     print(res.status_code)
#     print(res.cookies)