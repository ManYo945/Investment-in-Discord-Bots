#!/usr/bin/env python
# coding: utf-8


# 跳出webdriver視窗的形式
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# # 設置 ChromeDriver 的路徑
# webdriver_service = Service('path/to/chromedriver')

# # 創建 Chrome 瀏覽器驅動
# driver = webdriver.Chrome(service=webdriver_service)

# # 發送請求並等待網頁加載完成
# url = 'https://bank.sinopac.com/MMA8/bank/html/rate/bank_ExchangeRate.html'
# driver.get(url)

# # 使用 Selenium 定位元素並獲取內容 : 最後掛牌匯率時間
# element = driver.find_element(By.ID, 'tab1_date')
# content = element.get_attribute('innerHTML')
# print('報價時間: ',content)

# element = driver.find_element(By.ID, '_JPY_rb')
# ntw_jpy = element.get_attribute('innerHTML')
# print('銀行買入: ',ntw_jpy)

# element = driver.find_element(By.ID, '_JPY_rs')
# ntw_jpy = element.get_attribute('innerHTML')
# print('銀行賣出: ',ntw_jpy)

# # 關閉瀏覽器
# driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 設置 ChromeDriver 的路徑
webdriver_service = Service('path/to/chromedriver')

# 設置 Chrome 瀏覽器選項
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 創建 Chrome 瀏覽器驅動
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# 發送請求並等待網頁加載完成
url = 'https://bank.sinopac.com/MMA8/bank/html/rate/bank_ExchangeRate.html'
driver.get(url)

# 使用 Selenium 定位元素並獲取內容 : 最後掛牌匯率時間
element = driver.find_element(By.ID, 'tab1_date')
content = element.get_attribute('innerHTML')
print('報價時間: ',content)

element = driver.find_element(By.ID, '_JPY_rb')
ntw_jpy = element.get_attribute('innerHTML')
print('銀行買入(JPY): ',ntw_jpy)

element = driver.find_element(By.ID, '_JPY_rs')
ntw_jpy = element.get_attribute('innerHTML')
print('銀行賣出(JPY): ',ntw_jpy)

# 關閉瀏覽器
driver.quit()

import matplotlib.pyplot as plt

a = [0,1,2,3,4]
b = [4,3,2,1,0]

plt.plot(a)
plt.plot(b)

