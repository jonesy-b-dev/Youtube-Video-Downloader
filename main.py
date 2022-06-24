from pytube import YouTube
import os
from platform import system
import argparse

def clear_console():
    user_os = system().lower()
    if(user_os == "windows"):
        os.system('cls')
    else:
        os.system('clear')

if(__name__ == "__main__"):
    clear_console()

    error = False

    parser = argparse.ArgumentParser(description='Youtube video downloader.')
    parser.add_argument('--url',type=str,help='Url of the video (put the url in between of "" please)')

    args = parser.parse_args()
    print("Downloading file...")

    try:
        yt = YouTube(args.url)
        streams = yt.streams.filter(progressive=True,file_extension="mp4")
        
        if(os.path.exists("OUTPUT") is False):
            os.mkdir("OUTPUT")
        yt.streams.get_by_itag(streams[0].itag).download(output_path="OUTPUT/")
    except OSError:
        error = True
        clear_console()
        assert False, "ERROR WHILE DOWNLOADING VIDEO!!!"
        
    if(error is False):
        clear_console()
        print('Download ended!!!')