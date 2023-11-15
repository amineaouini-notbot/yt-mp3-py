import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
import pytube
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

# get url
url = str(input('Insert mix link => '))

# setup selenium driver
driver = webdriver.Chrome()
driver.get(url)

# retreive links from driver
elements = driver.find_elements(By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-playlist-panel-video-renderer")


for elemnt in elements:
    # setup yt url for pytube
    ytURL = elemnt.get_attribute('href') 
    yt = pytube.YouTube(ytURL) 

    #retrieve audio
    audio = yt.streams.filter(only_audio=True).first()

    # setup other destination if desired
    # print("Enter the destination (leave blank for current directory)") 
    # destination = str(input(">> ")) or '.'

    # download file
    out_file = audio.download(output_path='./dest') 

    # change file extention
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 

    # print successfully downloaded when everything is done correctly.
    print(yt.title + " has been successfully downloaded.")

driver.quit()