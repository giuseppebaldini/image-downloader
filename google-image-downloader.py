#! python3

# Google Images Downloader using Selenium

import os
import sys
import json
import urllib
import selenium

search_term = sys.argv[1]

try:
    num_images = sys.argv[2]
except IndexError:
    num_images = 10             # Default

# TODO: Specify download path / url / extensions

download_dir = '...'
url = 'https://www.images.google.com/search?tbm=isch&q=' + search_term
extensions = ["jpg", "jpeg", "png", "gif"]

# TODO: Input arguments

# TODO: Use Selenium to access Google Images

# TODO: Download images in specified folder

# TODO: [OPTIONAL] Summary (number of images / path / size)
