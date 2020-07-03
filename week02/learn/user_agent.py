from fake_useragent import UserAgent
import requests
import pretty_errors

ua = UserAgent(verify_ssl=False)

header = {
    'User-Agent':ua.Firefox
}

print(header)
response = requests.get('https://www.douban.com', headers=header)
print(response.status_code)
