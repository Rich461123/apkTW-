#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

userName = "XXXX"
userPassword = "ZZZZ"

chrome = webdriver.Chrome() 
chrome.get("https://apk.tw/forum.php")
chrome.maximize_window() 

chrome.sleep(3) 

chrome.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/a").click()
chrome.sleep(2)


chrome.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/div[1]/div/input").send_keys(userName)
chrome.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/div[2]/div/input").send_keys(userPassword)


chrome.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/button/em").click()
time.sleep(5)

chrome.find_element_by_xpath("/html/body/div[4]/div/div[3]/a[1]/img").click()
time.sleep(15)

chrome.quit() 



