from pytube import YouTube
import os
downloads_path = "download"
with open('bulk.txt') as f:
    output = f.readlines()
    for i in output:
        print(i)
        get_link = YouTube(i)
        get_link.streams.get_highest_resolution().download(output_path=os.path.join(downloads_path, 'YoutubeVideo'))
        print("Download Complete!")