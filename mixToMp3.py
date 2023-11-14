import os
from selenium import webdriver
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context
url = 'https://www.youtube.com/watch?v=QH3Fx41Jpl4&list=RDQH3Fx41Jpl4&start_radio=1'


driver = webdriver.Chrome()

driver.get(url)


driver.quit()
