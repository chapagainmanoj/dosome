#!/usr/bin/env python
import os
import requests
import json
import urllib.request
import subprocess

CURRENT_DIR = os.getcwd()

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
    print('a fresh XKCD dose for you ...')
    res = requests.get(get_url())
    print('JSON:\n')
    print(res.content)
    json_data = json.loads(res.text)
    print('\n')
    print("Opening Image ...")
    img = json_data['img'].split('/').pop()
    file_path = '{}/{}/{}'.format(CURRENT_DIR,'image',img)

    xkcd, headers = urllib.request.urlretrieve(json_data['img'],filename=file_path)
    subprocess.Popen(['/usr/bin/shotwell',file_path])
