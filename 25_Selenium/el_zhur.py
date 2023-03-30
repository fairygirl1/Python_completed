'''
Напишите программу которая автоматически собирает ваше расписание в Элжуре. и сохраняет в json файл в виде:
{день недели: {Предмет: Аудитория}
'''

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

url = "https://class.sirius.ru/authorize"

options = Options()
driver = webdriver.Chrome(options = options)
driver.get(url)

log = getenv('ELLOG')
psswd = getenv('ELPSSWD')

driver.find_element(By.XPATH, '//*[@id="inputEQd1AOadbB3"]"]').send_keys(log)
driver.find_element(By.XPATH, '//*[@id="inputjrixZ7QIDkg"]').send_keys(psswd)
driver.find_element(By.XPATH, '//*[@id="loginviewport"]/div/div[1]/form/div[2]/button').click()