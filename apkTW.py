#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

userName = "XXX"#輸入帳號
userPassword = "XXX"#輸入密碼

chrome = webdriver.Chrome() 
chrome.get("https://apk.tw/forum.php") #apk.tw網址
chrome.maximize_window() #視窗全螢幕

chrome.sleep(3) #等待3秒

chrome.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/a").click()
chrome.sleep(2)
#模擬點擊登錄欄位，等待2秒

chrome.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/div[1]/div/input").send_keys(userName)
chrome.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/div[2]/div/input").send_keys(userPassword)
#輸入帳號密碼

chrome.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/button/em").click()
time.sleep(5)
#按下登入鍵，等待5秒

chrome.find_element_by_xpath("/html/body/div[4]/div/div[3]/a[1]/img").click()
time.sleep(15)
#按下簽到按鈕並等待15秒鐘，預防簽到失敗
#簽到按鈕至少要5~7秒才會便已簽到，設定長一點預防萬一

chrome.quit()  #退出程式



