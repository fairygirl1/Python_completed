"""
Напишите программу которая автоматически собирает ваше расписание в Элжуре. и сохраняет в json файл в виде:
{день недели: {Предмет: Аудитория}
"""

# у меня не получилось спарсить элжур, сделала авторизацию на гите

from os import getenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import lxml
import urllib.request as urllib2
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from urllib.parse import urlparse
import requests

load_dotenv()

url = "https://github.com/login"

options = Options()
driver = webdriver.Chrome(options = options)
driver.get(url)

log = getenv('LOG')
psswd = getenv('PSSWD')

driver.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(log)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(psswd)
driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[11]').click()



page = requests.get(cur_url)

page = requests.get('https://github.com/fairygirl1?tab=repositories')
bs = BeautifulSoup(page.content, features='lxml')

for headers in bs.find_all('div', attrs = {'class': 'position-relative'}):
    
    if '^[h\d]' in headers:
        print(headers)
