# importing the pytube module
from pytube import YouTube
from sys import argv

# passing the youtube video link as the 2nd argument inside argv
link = argv[1]

# making the youtube object from the YouTube class
youtube = YouTube(link)

# indicating the download of high resolution video
youtube_download = youtube.streams.get_highest_resolution()

# specifying the path on local machine the video to be downloaded
youtube_download.download("D:\Downloads")
