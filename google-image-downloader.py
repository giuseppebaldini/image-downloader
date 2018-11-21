#! python3

# Google Images Downloader using Selenium

import os
import sys
import json
import urllib3
from selenium import webdriver

# Initial arguments
search_term = sys.argv[1]

try:
    num_images = int(sys.argv[2])
except IndexError:
    num_images = 10             # Default

http = urllib3.PoolManager()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Specify download path / url / extensions
main_dir = r'C:\Users\Giuseppe\Documents\Images'
download_dir = main_dir + '\\' + search_term.replace(" ","_")

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

url = 'https://www.google.com/search?tbm=isch&q=' + search_term
extensions = [".png", ".jpg", ".jpeg", ".gif", ".bmp"]

# Use Selenium to access Google Images
driver = webdriver.Firefox()
driver.get(url)

header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }

counter = 0

# Find images using XPath
images = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')

for img in images:

    counter += 1

    img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
    img_ext = img_url[-4]

    if img_ext not in extensions:
        img_ext = '.jpg'

    img_req = http.request('GET', img_url, preload_content = False)

    with open(download_dir + ' ' + str(counter) + img_ext, 'wb') as f:
        img_file = img_req.read()
        f.write(img_file)

    if counter >= num_images:
        break

    img_req.release_conn()

# TODO: [OPTIONAL] Summary (number of images / path / size)
