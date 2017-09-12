import os
import time
from selenium import webdriver
startTime = time.time()
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://stackoverflow.com")
print("Time waiting")
for x in range(0,9):
    print(str(1+x)+' sec',)
    time.sleep(1)
driver.quit()
endTime=time.time()
print("took %s seconds total" % (endTime-startTime))
