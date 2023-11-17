import pytube  
import os
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

url = str(input('Insert mix link => '))
playList = pytube.Playlist(url)

# get videos download destintion 
print("Enter the destination (leave blank for current directory)") 
destination = str(input(">> ")) or '.'


for video in playList.videos:
    # retrieve audio
    audio = video.streams.filter(only_audio=True).first()
    
    # download file
    out_file = audio.download(output_path=destination) 

    # change file extention
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 

    print(video.title + " has been successfully downloaded.")