import praw
import requests
import random
import os
import ctypes
import time
import json

time_begin = time.time()

path = "X:\\Code\\Projects\\BackgroundEngine\\downloads\\"
util_path = "X:\\Code\\Projects\\BackgroundEngine\\"

r = praw.Reddit('bot1')
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
			
def debug(download_speed, urls, post):
	with open('debug.json', "r") as f:
		data = json.load(f)
		if data['debug'] is False:
			return
		if data["download_speed"] is True:
			print("Download Speed : {} MB/s,".format(download_speed / 1000000))
		if data["wallpaper_list_length"] is True:
			print("Wallpaper List Length: {}".format(len(urls)))
		if data["wallpaper_url"] is True:
			print("Wallpaper set to: {}".format(post))

def setImgWallpaper():

	generateUrls()
	index = random.randint(0, len(urls) - 1)
	post = urls[index]

	with open("used.txt", "r+") as f:
		lines = f.read().splitlines()
		for i in range(len(lines)):
			if post == lines[i]:
				urls.pop(index)
				post = urls[random.randint(0, len(urls) - 1)]
		f.write("{}\n".format(post))
	
	unix_time = time.time()
	
	download_start = time.time()
	open(path + "{}.jpg".format(int(unix_time)), 'wb').write(requests.get(post, allow_redirects=False).content)
	download_ready = time.time()
	
	size = requests.get(post, stream=True).headers['Content-length']
	
	download_speed = float(size) / (download_ready - download_start)
	
	ctypes.windll.user32.SystemParametersInfoW(20, 0, path + "{}.jpg".format(int(unix_time)) , 0)
	removeDownloadsFolderContents(10)
	debug(download_speed, urls, post)
	exit()
	
setImgWallpaper()
