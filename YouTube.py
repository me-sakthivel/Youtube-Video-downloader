# Let's import pytube module
from pytube import YouTube
from pytube.request import stream

url = input("Type down the credentials :")
video = YouTube(url)

# Get the video title
print(video.title)

#set a resolution 
for streams in video.streams :
    print(stream)

video = video.streams.get_highest_resolution()
 
video.download()