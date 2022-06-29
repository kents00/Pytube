import os
from pytube import YouTube
from pathlib import Path
from os import *

def main():
    print("""

██████╗░██╗░░░██╗████████╗██╗░░░██╗██████╗░███████╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░░██║██╔══██╗██╔════╝
██████╔╝░╚████╔╝░░░░██║░░░██║░░░██║██████╦╝█████╗░░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░
██║░░░░░░░░██║░░░░░░██║░░░╚██████╔╝██████╦╝███████╗
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░░╚═════╝░╚═════╝░╚══════╝

    """)
    downloads_path = "download"
    link = str(input("Enter url to download:"))
    get_link = YouTube(link)
    select_format = int(input("Please select a format:\n[1] Video \n[2] Audio\n"))
    if select_format == 1:
        get_link.streams.get_highest_resolution().download(output_path=os.path.join(downloads_path, 'YoutubeVideo'))
        print("Download Complete!")
    elif select_format == 2:
        stream = get_link.streams.filter(only_audio=True).first().download(output_path=os.path.join(downloads_path, 'YoutubeAudio'))
        base, ext = path.splitext(stream)
        new_file = base + '.mp3'
        rename(stream, new_file)
        print("Download Complete!")
    else:
        print("Please select 1 or 2")


if __name__ == "__main__":
    main()