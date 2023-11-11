import pytube 
import os

# get URL
yt = pytube.YouTube(str(input('Paste desired yt video =>'))) 

# I - to bypass auth to restricted videos:
#   1 - in C:\Python310\Lib\site-packages\pytube\__main__.py 
#   2 - at def bypass_age_gate change InnerTube => InnerTube(client='ANDROID',[don't change the other arguments values])

#retrieve audio
audio = yt.streams.filter(only_audio=True).first()

# setup other destination if desired
print("Enter the destination (leave blank for current directory)") 
destination = str(input(">> ")) or '.'

# download file
out_file = audio.download(output_path=destination) 

# change file extention
base, ext = os.path.splitext(out_file) 
new_file = base + '.mp3'
os.rename(out_file, new_file) 

# print successfully downloaded when everything is done correctly.
print(yt.title + " has been successfully downloaded.")