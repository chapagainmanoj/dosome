#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
from PIL import Image
import json
import requests,urllib
from bs4 import BeautifulSoup

# Get BingXML file which contains the URL of the Bing Photo of the day
# idx = Number days previous the present day. 0 means current day, 1 means       yesterday, etc
# n = Number of images predious the day given by idx
# mkt denotes your location. e.g. en-US means United States. Put in your  country code

if __name__=='__main__':

    """http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=2&mkt=en-ID"""
    BingURL = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=2&mkt=en-ID"

    page = requests.get(BingURL)
    data = json.loads(page.text)
    url = data['images'][0]['url']
    img_name = url.split('/')[-1].split('_')[0]

    image_url = "https://www.docx.us/bing/"+ img_name + ".jpg"


    image_path= "/home/mane/pscripts/image/bing_today.jpg"
    # For extracting complete URL of the image

    #area=(1366,1366,768,768)
    width = 1366
    height = 768

    urllib.request.urlretrieve(image_url, image_path)

    img = Image.open(image_path)
    new_img = img.resize((width,height), Image.NEAREST)
    new_img.save("image/bing_wallpaper.jpg")
    os.system("rm "+ image_path)
