import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

# Search No 表示要查詢的資料
SearchNo = 2330

# 開啟網頁
browser.get('https://www.tdcc.com.tw/portal/zh/smWeb/qryStock')

# 找到輸入框, 輸入要查詢的股號
stockNo = browser.find_element_by_name('stockNo')
stockNo.send_keys(SearchNo)

# 點擊查詢
button = browser.find_element_by_css_selector('tr:nth-child(4) input')
button.click()

# 抓取原始碼
pagesource = browser.page_source

# beautifulsoup抓取列表
soup = BeautifulSoup(pagesource, 'html.parser')
table = soup.select('.table')[0]

# 從檢查中可以發現，標題跟資料是被分開的，因此我們用thead跟tbody分開抓取
for thead in table.select('thead'):
    print(thead.select('th')[0].text, thead.select('th')[1].text, thead.select('th')[2].text, thead.select('th')[3].text, thead.select('th')[4].text)
    pass

for tbody in table.select('tbody'):
    for tr in tbody.select('tr'):
        print(tr.select('td')[0].text, tr.select('td')[1].text, tr.select('td')[2].text, tr.select('td')[3].text, tr.select('td')[4].text)
        pass
    pass

# 睡眠後，關閉視窗
time.sleep(3)
browser.quit()
