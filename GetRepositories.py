#!python3
#encoding:utf-8

import requests
from furl import furl

username = 'username'
token = '0123456789012345678901234567890123456789'
timezone = 'Asia/Tokyo'
headers = {'Authorization': 'token ' + token, 'Time-Zone': timezone}

url = 'https://api.github.com/user/repos'
f = furl(url)
f.args['type'] = 'owner'
f.args['sort'] = 'created'
f.args['direction'] = 'desc'
f.args['per_page'] = '1000'
res = requests.get(f.url, headers=headers)

filename = "GitHub.{0}.Repositories.json".format(username)
file = open(filename, 'w', encoding="UTF-8")
file.write(res.text)
file.close()
