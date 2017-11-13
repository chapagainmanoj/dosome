import os
import time
from selenium import webdriver

url = 'https://quay.io/customtrigger/setup/chapagainmanoj/tester'

startTime = time.time()
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(url)


print("Time waiting")

for x in range(0,9):
    print(str(1+x)+' sec',)
    time.sleep(1)

print(driver)
