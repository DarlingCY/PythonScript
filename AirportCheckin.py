import json
import requests
import os
import notify

session = requests.session()
url = os.getenv("AIRPORT_URL")
email = os.getenv("AIRPORT_ACCOUNT")
passwd = os.getenv("AIRPORT_PASSWD")

login_url = '{}/auth/login'.format(url)
check_url = '{}/user/checkin'.format(url)

header = {
    'origin': url,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
data = {
    'email': email,
    'passwd': passwd
}
try:
    print('开始登录')
    response = json.loads(session.post(url=login_url, headers=header, data=data).text)
    print(response['msg'])
    # 进行签到
    result = json.loads(session.post(url=check_url, headers=header).text)
    content = result['msg']
    print(content)
    notify.send(title="机场签到", content=content)
    print('推送成功')
except:
    content = '签到失败'
    print(content)
    notify.send(title="机场签到", content=content)
    print('推送成功')
