import praw
import requests
import time
import random
import os
import ctypes
from dotenv import load_dotenv
import time

r = praw.Reddit('bot2')
urls = []

def generate_urls():
    if len(urls) == 0:
        for post in r.subreddit("Wallpaper").top() and r.subreddit("Wallpaper").hot():
            url = post.url
            if url[-1] == 'g' and url[-2] == 'p' and url[-3] == 'j' and url[-4] == '.':
                urls.append(url)


generate_urls()

random = random.randint(0, len(urls))
post = urls[random]

download = requests.get(post, allow_redirects=False)

open('X:\\Code\\Projects\\BackgroundEngine\\download.jpg', 'wb').write(download.content)

ctypes.windll.user32.SystemParametersInfoW(20, 0, "X:\\Code\\Projects\\BackgroundEngine\\download.jpg" , 0)

with open("logs.log", "a") as f:
    current_unix = time.time()
    f.write("\n[{}] Set Wallpaper to {}".format(current_unix, post))

time.sleep(2)

os.remove("X:\\Code\\Projects\\BackgroundEngine\\download.jpg")
exit()
