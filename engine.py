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
        for post in r.subreddit("Wallpaper").top():
            url = post.url
            if url[-1] == 'g' and url[-2] == 'p' and url[-3] == 'j' and url[-4] == '.':
                urls.append(url)
            print(url)


generate_urls()

random = random.randint(0, len(urls))
post = urls[random]
download = requests.get(post, allow_redirects=False)
print(" Post URL {}".format(post))

urls.pop(random)

open('X:\\Code\\Projects\\BackgroundEngine\\download.jpg', 'wb').write(download.content)

ctypes.windll.user32.SystemParametersInfoW(20, 0, "X:\\Code\\Projects\\BackgroundEngine\\download.jpg" , 0)
print(" Set wallpaper")


time.sleep(1)
os.remove("X:\\Code\\Projects\\BackgroundEngine\\download.jpg")
print(" Removed download.jpg")
time.sleep(2)
exit()
