import praw
import requests
import random
import os
import ctypes
import time
import threading

time_begin = time.time()

path = "X:\\Code\\Projects\\BackgroundEngine\\downloads\\"
util_path = "X:\\Code\\Projects\\BackgroundEngine\\"

r = praw.Reddit('bot2')
urls = []


def generateUrls():
    global gen, gen_e
    gen = time.time()
    for post in r.subreddit("Wallpaper").top(limit=10) and r.subreddit("Wallpaper").hot(limit=10):
        url = post.url
        if url[-1] == 'g' and url[-2] == 'p' and url[-3] == 'j' and url[-4] == '.':
            urls.append(url)

    if len(urls) == 0:
        generateUrls()
    gen_e = time.time()

def removeDownloadsFolderContents(rule):
    folder = os.listdir(path)
    if len(folder) >= rule:
        for file in folder:
            try:
                os.remove(path + file)
            except:
                pass
            
def setImgWallpaper():

    generateUrls()
    print(len(urls))
    post = urls[random.randint(0, len(urls) - 1)]
    print(post)

    unix_time = time.time()

    d_time_s = time.time()
    open(path + "{}.jpg".format(int(unix_time)), 'wb').write(requests.get(post, allow_redirects=False).content)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + "{}.jpg".format(int(unix_time)) , 0)

    removeDownloadsFolderContents(10)
    
    with open(util_path + "time.txt", "a") as f:
        f.write("\n{} : {} : {}".format(time.time() - time_begin, d_time_o, gen_e - gen))

    exit()
setImgWallpaper()
