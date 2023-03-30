"""
Напишите программу которая автоматически зайдет на https://store.steampowered.com/ в поле поиска отправит стратегии
и соберет названия всех стратегий на 1 странице.
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import lxml
import time
from bs4 import BeautifulSoup

options = Options()
driver = webdriver.Chrome(options = options)
driver.get("https://store.steampowered.com/?l=russian")
search = driver.find_element(By.XPATH, '//*[@id=\"store_nav_search_term"]')
search.send_keys('стратегии')
search.send_keys(Keys.ENTER)
page_source = driver.page_source

soup = BeautifulSoup(page_source, 'lxml')
container = soup.find('div', 'search_results')
names = container.find_all('span', attrs = {'class': 'title'})

results = {}
k = 1
for i in names:
    results[i.text] = k
    k += 1
print(results)



