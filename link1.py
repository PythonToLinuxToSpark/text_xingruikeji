# 1905060103 辛天宇

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv

driver = webdriver.Chrome()
url = 'https://iftp.chinamoney.com.cn/english/bdInfo/'
driver.get(url)
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="Bond_Type_select"]').click()
driver.find_element(By.XPATH, '//option[text()="Treasury Bond"]').click()
driver.find_element(By.XPATH, '//*[@id="Issue_Year_select"]').click()
driver.find_element(By.XPATH, '//option[text()="2023"]').click()
driver.find_element(By.XPATH, '//*[@onclick="searchData()"]').click()
time.sleep(2)

with open('C:/Users/86131/Desktop/测试数据爬取/test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating'])
    i = 1
    while i:
        trs = driver.find_elements(By.XPATH, f'//*[@class="san-sheet-alternating"]/tbody/tr')
        for tr in trs:
            isin = tr.find_element(By.XPATH, './/*[@data-name="isin"]/span/a').text
            bond_code = tr.find_element(By.XPATH, './/*[@data-name="bondCode"]/span/a').text
            issuer = tr.find_element(By.XPATH, './/*[@data-name="entyFullName"]/span').text
            bond_type = tr.find_element(By.XPATH, './/*[@data-name="bondType"]/span').text
            issue_Date = tr.find_element(By.XPATH, './/*[@data-name="issueStartDate"]/span').text
            latest_rating = tr.find_element(By.XPATH, './/*[@data-name="debtRtng"]/span').text
            # print(isin, bond_code, issuer, bond_type, issue_Date, latest_rating)
            writer.writerow([isin, bond_code, issuer, bond_type, issue_Date, latest_rating])
        try:
            driver.find_element(By.XPATH, '//*[@class="page-btn page-next"]').click()
        except NoSuchElementException:
            exit()
