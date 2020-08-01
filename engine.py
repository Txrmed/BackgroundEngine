import praw
import requests
import time
import random
import os
import ctypes

r = praw.Reddit('bot2')
urls = []

def generate_urls():
    if len(urls) == 0:
        for post in r.subreddit('Earthporn').top():
            if post[-1] == 'g' and post[-2] == 'p' and post[-3] == 'j' and post[-4] == '.':
                url = post.url
                urls.append(url)
        print(urls)


while 1:
    time = time.time()
    # if len(urls) == 0:
    generate_urls()
    # elif time % 14400:
    #     generate_urls()

    # if time % 1800:
    download = None
    post = urls[random.randint(0, len(urls))]
    download = requests.get(post, allow_redirects=False)
    urls.pop(post)

    open('download.jpg', 'wb').write(download.content)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "download.jpg" , 0)
    time.sleep(1)
