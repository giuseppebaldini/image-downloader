#! python3

# Download images from Google Images using urllib3 and Selenium

import os
import sys
import json
import urllib3
from selenium import webdriver

# Allow multiple search terms and create new directory name format
search_term = ' '.join(sys.argv[1:-1])           # from first to penultimate arg
dir_name = search_term.replace(" ","_").title()  # name format = Name_Format

# Number of images to download or leave blank for default value
try:
    num_images = int(sys.argv[-1])
except (IndexError, ValueError):
    num_images = 10                              # Default value

http = urllib3.PoolManager()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Download path / URL / Extensions
main_dir = r'C:\Users\Giuseppe\Documents\Images'
download_dir = os.path.join(main_dir, dir_name)

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

url = 'https://www.google.com/search?tbm=isch&q=' + search_term
extensions = [".png", ".jpg", ".jpeg", ".gif", ".bmp"]

# Use Firefox headless to operate in background
os.environ['MOZ_HEADLESS'] = '1'
browser = webdriver.Firefox()
browser.get(url)

counter = 0
size = 0

# Find images using XPath
images = browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')

# Write each image in the folder while increasing counter and size
for img in images:

    counter += 1

    img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
    img_ext = img_url[-4]

    if img_ext not in extensions:
        img_ext = '.jpg'

    img_req = http.request('GET', img_url, preload_content = False)

    file_name = os.path.join(download_dir, dir_name + str(counter) + img_ext)

    with open(file_name, 'wb') as f:
        img_file = img_req.read()
        f.write(img_file)

    size += os.path.getsize(file_name)

    if counter >= num_images:
        break

    img_req.release_conn()

# Final output message with number of images downloaded, path and total size
print('Download completed.\n%d images downloaded in %s\nTotal size: %.2f MB'
      % (counter, download_dir, (size / (1024 * 1024))))

browser.quit()
