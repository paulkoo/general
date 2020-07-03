from pytube import YouTube
from selenium import webdriver
from bs4 import BeautifulSoup


#Enter link to playlist
playlist = 'https://www.youtube.com/playlist?list=PLAkwTma2FqEBVPWnibiwMHMiQn2jQkmdW'

#Makes browser run not on screen
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options = options)

#Loads page and parses html
print("Loading Page")
driver.get(playlist)
print("Page Loaded")
code = driver.page_source
soup = BeautifulSoup(code, 'html.parser')

#Download audio for each video in playlist
for html in soup.find_all("a", class_='yt-simple-endpoint style-scope ytd-playlist-video-renderer'):
    link = "https://www.youtube.com/watch?v=" + html.get('href')[9:20]
    yt = YouTube(link)
    audio=yt.streams.get_audio_only()
    audio.download('/home/pi/Desktop/music')
    print(f'Successfully Downloaded: {yt.title}')
