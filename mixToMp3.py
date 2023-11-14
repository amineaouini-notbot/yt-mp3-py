import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context
url = 'https://www.youtube.com/watch?v=QH3Fx41Jpl4&list=RDQH3Fx41Jpl4&start_radio=1'


driver = webdriver.Chrome()
driver.get(url)

elements = driver.find_elements(By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-playlist-panel-video-renderer")
# elements = WebDriverWait(driver,10).until(lambda x: x.find_elements(By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-playlist-panel-video-renderer"))
# elements = elements.find_elements('.yt-simple-endpoint .style-scope .ytd-playlist-panel-video-renderer')
print(elements)
for elemnt in elements:
    print(elemnt.get_attribute('href'))
# driver.quit()
