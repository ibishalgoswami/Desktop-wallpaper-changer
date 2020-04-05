"""Here I am using Pexels API for downloading different images.
Visit this page https://www.pexels.com/api/ and get your auth code from there.
Once you Put your auth code below in the code you are good to go."""

import requests
import pprint
import ctypes
import time
import os
import sys
from os.path import join
from glob import glob


def connected(host='http://google.com'):  # Checking the internet connection
    try:
        requests.get(host)
        return True
    except:
        return False


files = []
cur_dir = os.getcwd()
for ext in ('*.gif', '*.png', '*.jpg'):  # Types of images extension
    files.extend(glob(join(cur_dir, ext)))


def wallpaper_downloader_and_changer():
    try:
        search_query = input('Enter your Search Image : ')
        url = f"https://api.pexels.com/v1/search?query={search_query}+query&per_page=15&page=1"
        auth_key = "Provide your auth key here(within quotes)"
        res = requests.get(url, headers={
                           'Authorization': auth_key})
        data = res.json()
        no_Of_Pic = int(input('Enter No of Pictures you want : '))
        for i in range(0, no_Of_Pic):
            img = data['photos'][i]['src']['original']
            url = img
            # filename = url.split('/')[-1]
            filename = str(i)+'.jpg'
            r = requests.get(url, allow_redirects=True)
            open(filename, 'wb').write(r.content)
    except:
        print("Oops! Your query can not be processed.Try with another search.")
        sys.exit()

    files = []
    cur_dir = os.getcwd()
    for ext in ('*.gif', '*.png', '*.jpg'):  # Types of images extension
        files.extend(glob(join(cur_dir, ext)))

    while True:
        for i in files:
            SPI_SETDESKWALLPAPER = 20
            # Setting up the wallpaper in the background
            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 0, i, 3)
            time.sleep(3)


def wallpaper_changer():
    while True:
        for i in files:
            SPI_SETDESKWALLPAPER = 20
            # Setting up the wallpaper in the background
            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 0, i, 3)
            time.sleep(3)


if not files:
    if connected() == True:
        wallpaper_downloader_and_changer()  # calling the function
    else:
        print("Oops! No Internet Connection")

else:
    if files:
        wallpaper_changer()
    else:
        wallpaper_downloader_and_changer()
