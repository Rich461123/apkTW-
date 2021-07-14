#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firstName = "sssss6144"#輸入帳號
firstPassword = "Riche0826"#輸入密碼

first = webdriver.Chrome() 
first.get("https://apk.tw/forum.php") #apk.tw網址
first.maximize_window() #視窗全螢幕

time.sleep(3) #等待3秒

first.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/a").click()
time.sleep(2)
#模擬點擊登錄欄位，等待2秒

first.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/div[1]/div/input").send_keys(firstName)
first.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/div[2]/div/input").send_keys(firstPassword)
#輸入帳號密碼

first.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/button/em").click()
time.sleep(5)
#按下登入鍵，等待5秒

first.find_element_by_xpath("/html/body/div[4]/div/div[3]/a[1]/img").click()
time.sleep(15)
#按下簽到按鈕並等待15秒鐘，預防簽到失敗
#簽到按鈕至少要5~7秒才會便已簽到，設定長一點預防萬一

first.quit()  #退出程式

secondName = "sssss5144"#輸入帳號
secondPassword = "Riche0826"#輸入密碼

second = webdriver.Chrome() 
second.get("https://apk.tw/forum.php") #apk.tw網址
second.maximize_window() #視窗全螢幕

time.sleep(3) #等待3秒

second.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/a").click()
time.sleep(2)
#模擬點擊登錄欄位，等待2秒

second.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/div[1]/div/input").send_keys(secondName)
second.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/div[2]/div/input").send_keys(secondPassword)
#輸入帳號密碼

second.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/button/em").click()
time.sleep(5)
#按下登入鍵，等待5秒

second.find_element_by_xpath("/html/body/div[4]/div/div[3]/a[1]/img").click()
time.sleep(15)
#按下簽到按鈕並等待15秒鐘，預防簽到失敗
#簽到按鈕至少要5~7秒才會便已簽到，設定長一點預防萬一

second.quit()  #退出程式

thirdName = "sssss4144"#輸入帳號
thirdPassword = "Zxc951753"#輸入密碼

third = webdriver.Chrome() 
third.get("https://apk.tw/forum.php") #apk.tw網址
third.maximize_window() #視窗全螢幕

time.sleep(3) #等待3秒

third.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/a").click()
time.sleep(2)
#模擬點擊登錄欄位，等待2秒

third.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/div[1]/div/input").send_keys(thirdName)
third.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/div[2]/div/input").send_keys(thirdPassword)
#輸入帳號密碼

third.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/button/em").click()
time.sleep(5)
#按下登入鍵，等待5秒

third.find_element_by_xpath("/html/body/div[4]/div/div[3]/a[1]/img").click()
time.sleep(15)
#按下簽到按鈕並等待15秒鐘，預防簽到失敗
#簽到按鈕至少要5~7秒才會便已簽到，設定長一點預防萬一

third.quit()  #退出程式


# In[ ]:




