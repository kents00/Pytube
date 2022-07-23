import os
from pytube import YouTube

def bulk_download():
    
    downloads_path = "download"
    try:
        with open('bulk.txt', 'r') as f:
            output = f.readlines()
            select = int(input("Please select a format:\n[1] Video \n[2] Audio\n"))
            if select == 1:
                for i in output:
                    get_link = YouTube(i)
                    get_link.streams.get_highest_resolution().download(output_path=os.path.join(downloads_path, 'YoutubeVideo'))
                    print("Download Complete!")
            elif select == 2:
                for i in output:
                    get_link = YouTube(i)
                    stream = get_link.streams.filter(only_audio=True).first().download(output_path=os.path.join(downloads_path, 'YoutubeAudio'))
                    base, ext = os.path.splitext(stream)
                    new_file = base + '.mp3'
                    os.rename(stream, new_file)
                    print("Download Complete!")
            else:
                print("Please select 1 or 2")
    except FileNotFoundError:
        print("Please create a file named bulk.txt")

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
    select_format = int(input("Please select a format:\n[1] Video \n[2] Audio\n[3] Bulk Download\n"))

    if select_format == 1:
        link = str(input("Enter url to download:"))
        get_link = YouTube(link)
        get_link.streams.get_highest_resolution().download(output_path=os.path.join(downloads_path, 'YoutubeVideo'))
        print("Download Complete!")
    elif select_format == 2:
        link = str(input("Enter url to download:"))
        get_link = YouTube(link)
        stream = get_link.streams.filter(only_audio=True).first().download(output_path=os.path.join(downloads_path, 'YoutubeAudio'))
        base, ext = os.path.splitext(stream)
        new_file = base + '.mp3'
        os.rename(stream, new_file)
        print("Download Complete!")
    elif select_format == 3:
        bulk_download()
    else:
        print("Please select 1, 2 or 3")

if __name__ == "__main__":
    main()