import praw
import requests
import time
import random
import os
import ctypes
from dotenv import load_dotenv
import time

path = "X:\\Code\\Projects\\BackgroundEngine\\downloads\\"

r = praw.Reddit('bot2')
urls = []


def generate_urls():
    if len(urls) == 0:
        for post in r.subreddit("Wallpaper").top() and r.subreddit("Wallpaper").hot():
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
    random = random.randint(0, len(urls))
    post = urls[random]

    download = requests.get(post, allow_redirects=False)
    unix_time = time.time()

    open(path + "{}.jpg".format(int(unix_time)), 'wb').write(download.content)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + "{}.jpg".format(int(unix_time)) , 0)

    with open("X:\Code\Projects\BackgroundEngine\logs.log", "a") as f:
        f.write("\n[{}] Set Wallpaper to {}".format(int(unix_time), post))

    removeDownloadsFolderContents(10)

    exit()

setWallpaper()
