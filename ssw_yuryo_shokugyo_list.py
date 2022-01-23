from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from urllib import response
import urllib.request as req
import pandas as pd
import os
import datetime

browser = webdriver.Chrome()
browser.implicitly_wait(3)

first_url = "https://jinzai.hellowork.mhlw.go.jp/JinzaiWeb/GICB101010.do?action=initDisp&screenId=GICB101010"
browser.get(first_url)
time.sleep(1)
print("accessed home page")

btn = browser.find_element(by=By.XPATH, value='/html/body/div/div/form/div[2]/div[2]/div/div/dl[1]/dt[2]/a')
time.sleep(1)
btn.click()
print("accessed list page")

checkbox_all_pref = browser.find_element(by=By.ID, value='ID_cbZenkoku1')
time.sleep(1)
checkbox_all_pref.click()
print(checkbox_all_pref.is_selected())
time.sleep(1)

checkbox_yuryo_shokugyo = browser.find_element(by=By.ID, value='ID_cbJigyoshoKbnYu1')
time.sleep(1)
checkbox_yuryo_shokugyo.click()
print(checkbox_yuryo_shokugyo.is_selected())
time.sleep(3)

btn_to_filter = browser.find_element(by=By.XPATH, value='/html/body/form/div[2]/div[3]/div/div[3]/input')
btn_to_filter.click()
print("filter with targeted category")

## how to get table data of each pagenated one ##
