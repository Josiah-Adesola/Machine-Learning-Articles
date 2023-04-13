import os
from pytube import YouTube
from urllib.request import urlretrieve
from progressbar import ProgressBar, Percentage, Bar, ETA
from sys import argv

link = input("Enter the YouTube video URL: ")

try:
    yt = YouTube(link)
except KeyError:
    print("Error: Unable to get video data. Please input another video URL.")
    exit()

# get all the available video streams
streams = yt.streams

resolution = '480p' # Replace with the desired resolution
stream = streams.filter(resolution=resolution).first()

# Define the download path and name for the downloaded video
if len(argv) > 2:
    download_path = argv[2]
else:
    download_path = os.getcwd()
if not os.path.exists(download_path):
    os.makedirs(download_path)


# Define the file path and name for the downloaded video
file_path = os.getcwd()
file_name = stream.default_filename
file_url = stream.url

# Use progressbar to display a progress bar while downloading the video
pbar = ProgressBar(widgets=[Percentage(), Bar(), ETA()], maxval=stream.filesize * 2 ).start()
urlretrieve(file_url, file_path + file_name, lambda blocknum, blocksize, totalsize: pbar.update(blocknum * blocksize))
pbar.finish()
print("Download complete!")