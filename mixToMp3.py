from pytube import Playlist
import os
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.youtube.com/watch?v=QH3Fx41Jpl4&list=RDQH3Fx41Jpl4&start_radio=1')
soup = BeautifulSoup(res.content, 'html.parser')
mix = soup.find_all(class_="yt-simple-endpoint style-scope ytd-playlist-panel-video-renderer")
# mix = Playlist('https://www.youtube.com/watch?v=QH3Fx41Jpl4&list=RDQH3Fx41Jpl4&start_radio=1')
print(mix)
# for video in mix:
#     audio = video.streams.filter(only_audio=True).first()
#     audio.download(output_path='/dest')
