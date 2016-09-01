import requests
from  bs4 import BeautifulSoup
from pytube import YouTube


def getAllVideoLinks(playlist):
    source_code = requests.get(playlist)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    song_list = []
    for link in soup.findAll('a', {'class': 'pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link '}):
        downloadVideos(r'https://www.youtube.com'+link.get('href'))

def downloadVideos(videoUrl):
    yt = YouTube(videoUrl)
    print yt.get_videos()
    try:
        video = yt.get('mp4','720p')
    except Exception as e:
        video = yt.get('mp4','360p')
        print e
    #video.download(r'C:\Users\310168881\Desktop\Videos')

def main():
    playlist = raw_input("Enter the link for playlist: ")
    getAllVideoLinks(playlist)

if __name__ == '__main__':
    main()
