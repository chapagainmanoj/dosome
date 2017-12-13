#!/usr/bin/env python

import os
import json
import urllib
import requests
from PIL import Image
from datetime import date
from subprocess import run,PIPE

#area=(1366,1366,768,768) Screen Resolution
WIDTH = 1366
HEIGHT = 768
CURRENT_DIR = os.getcwd()
TODAY = date.today()

try:
    raw_ = run(['xdpyinfo | grep dimensions:'], shell=True, stdout=PIPE)
    dimension = raw_.stdout.split()[1].decode().split('x')
    dimension = list(map(int,dimension))
    WIDTH, HEIGHT = dimension
except:
    print("Screen size can't extracted")

# Get BingXML file which contains the URL of the Bing Photo of the day
# idx = Number days previous the present day. 0 means current day, 1 means       yesterday, etc
# n = Number of images predious the day given by idx
# mkt denotes your location. e.g. en-US means United States. Put in your  country code

if __name__=='__main__':
    img_dir ='{}/{}'.format(CURRENT_DIR,'image')

    if not os.path.isdir(img_dir):
        os.makedirs(img_dir)

    """http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=2&mkt=en-ID"""
    BingURL = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=2&mkt=en-ID"

    page = requests.get(BingURL)
    data = json.loads(page.text)
    url = data['images'][0]['url']
    img_name = url.split('/')[-1].split('_')[0]

    image_url = '{}/{}.{}'.format('https://www.docx.us/bing',img_name,'jpg')


    #image_path= "/home/mane/pscripts/image/bing_today.jpg"
    image_path = '{}/{}'.format(img_dir,img_name)
    # For extracting complete URL of the image


    urllib.request.urlretrieve(image_url, image_path)

    img = Image.open(image_path)
    new_img = img.resize((WIDTH,HEIGHT), Image.NEAREST)
    new_img.save("image/{0}.jpg".format(TODAY.isoformat()))
    print("New wallpaper from Bing saved to {}/image/".format(CURRENT_DIR))
    os.system("rm "+ image_path)
