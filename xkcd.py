#!/usr/bin/env python
import requests
import json
import urllib.request
import subprocess


def get_url(num = None):
    url ='http://xkcd.com/'
    base = 'info.0.json'
    tail = '/info.0.json'
    if num:
        return url + str(num) + tail
    else:
        return url + base

# format url ="https://xkcd.com/xxx/info.0.json"
#os.makedirs('xkcd',exist_ok=True)
#while not url.endswith('#'):

if __name__=='__main__':
    print(get_url())
    res = requests.get(get_url())
    json_data = json.loads(res.text)
    print(res.content)
    print (json_data['img'])

    xkcd, headers = urllib.request.urlretrieve(json_data['img'],filename="/home/mane/pscripts/00.jpg")
    subprocess.Popen(['/usr/bin/shotwell',"/home/mane/pscripts/00.jpg"])
