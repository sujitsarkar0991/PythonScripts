import requests
import os
from  bs4 import BeautifulSoup
from  selenium import webdriver

def getAllVideoLinks(playlist):
    source_code = requests.get(playlist)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    song_list = []
    for link in soup.findAll('a', {'class': 'pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link '}):
        song_list.append(r'https://www.youtube.com'+link.get('href'))
    for x in song_list:
        print x
def main():
    #playlist = raw_input("Enter the link for playlist: ")
    chromedriver = "C:\Python27\Scripts"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get('https://www.youtube.com/playlist?list=PL6dydJby22DjcYcWwnukPw2lxi8PeQScX')
    elem = driver.find_elements_by_class_name('load-more-text')
    elem.click()
    getAllVideoLinks('https://www.youtube.com/playlist?list=PL6dydJby22DjcYcWwnukPw2lxi8PeQScX')

if __name__ == '__main__':
    main()
