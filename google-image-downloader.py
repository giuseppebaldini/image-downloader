#! python3

# Google Images Downloader using Selenium

# Usual: Check - Comments - Readme

import os
import sys
import json
import urllib3
from selenium import webdriver

# Initial arguments
search_term = ' '.join(sys.argv[1:-1]).title()
search_line = search_term.replace(" ","_")

try:
    num_images = int(sys.argv[-1])
except (IndexError, ValueError):
    num_images = 10                     # Default

http = urllib3.PoolManager()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Specify download path / url / extensions
main_dir = r'C:\Users\Giuseppe\Documents\Images'
download_dir = main_dir + '\\' + search_line

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

url = 'https://www.google.com/search?tbm=isch&q=' + search_term
extensions = [".png", ".jpg", ".jpeg", ".gif", ".bmp"]

# Use Selenium to access Google Images
os.environ['MOZ_HEADLESS'] = '1'
browser = webdriver.Firefox()
browser.get(url)

counter = 0
size = 0

# Find images using XPath
images = browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')

for img in images:

    counter += 1

    img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
    img_ext = img_url[-4]

    if img_ext not in extensions:
        img_ext = '.jpg'

    img_req = http.request('GET', img_url, preload_content = False)

    file_name = os.path.join(download_dir, search_line + str(counter) + img_ext)

    with open(file_name, 'wb') as f:
        img_file = img_req.read()
        f.write(img_file)

    size += os.path.getsize(file_name)

    if counter >= num_images:
        break

    img_req.release_conn()

print('''Download completed. %d images downloaded in %s.
Total size: %d MB.
''' % (counter, download_dir, (size / (1024 * 1024))))

browser.quit()
