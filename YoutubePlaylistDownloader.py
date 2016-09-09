import requests
from bs4 import BeautifulSoup
from pytube import YouTube
import os


def getAllVideoLinks(playlist):
    source_code = requests.get(playlist)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    video_list = []
    for link in soup.findAll('a', {'class': 'pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link '}):
        video_list.append(r'https://www.youtube.com'+link.get('href'))
    return video_list

def downloadVideos(video_url_list):
    video = None
    folderName = "YouTubePlaylist"
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    for video_url in video_url_list:
        try:
            yt = YouTube(video_url)
            try:
                video = yt.get('mp4','720p')
            except Exception:
                video = yt.get('mp4','360p')
        except Exception as e:
            pass
        video.download(folderName)

def main():
    playlist = raw_input("Enter the link for playlist: ")
    video_links = getAllVideoLinks(playlist)
    downloadVideos(video_links)

if __name__ == '__main__':
    main()
