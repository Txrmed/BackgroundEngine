import praw
import requests
import random
import os
import ctypes
import time
import threading

time_begin = time.time()

path = "X:\\Code\\Projects\\BackgroundEngine\\downloads\\"

r = praw.Reddit('bot2')
urls = []


def generate_urls():
    if len(urls) == 0:
        for post in r.subreddit("Wallpaper").top():
            url = post.url
            if url[-1] == 'g' and url[-2] == 'p' and url[-3] == 'j' and url[-4] == '.':
                urls.append(url)

def removeDownloadsFolderContents(rule):
    folder = os.listdir("./downloads")
    if len(folder) >= rule:
        for file in folder:
            try:
                os.remove("./downloads/" + file)
            except:
                pass
            
def setWallpaper():

    global random

    generate_urls()

    post = urls[random.randint(0, len(urls))]

    unix_time = time.time()

    open(path + "{}.jpg".format(int(unix_time)), 'wb').write(requests.get(post, allow_redirects=False).content)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + "{}.jpg".format(int(unix_time)) , 0)

    removeDownloadsFolderContents(10)

    unix_time = time.time()
    with open("X:\Code\Projects\BackgroundEngine\logs.log", "a") as f:
        f.write("\n[{}] Set Wallpaper to {}".format(int(unix_time), post))
    
    time_end = time.time()
    with open("time.txt", "a") as f:
        f.write("\n{}".format(time_end - time_begin))

    exit()

setWallpaper()
