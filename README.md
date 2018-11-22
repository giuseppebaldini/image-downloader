# Image Downloader

A Python script to download images from Google, operating completely in the background. 

### Introduction

Given at least one <code>search term</code> and a <code>number</code> of images (max 100) the program:

1. Creates new folder in the given download path

2. Searches for specified search term in Google Images

3. Download all the images found in the newly created folder

### Dependencies

* [urllib3](https://github.com/urllib3/urllib3) (HTTP library)

* [Selenium](https://github.com/asweigart/pyperclip) (Browser automation)

To install: <code>pip install <name_module></code>
  
**Important**: Selenium here requires a browser driver to work. You can download it [here](https://www.seleniumhq.org/download/).

### Usage

<code>python image_downloader.py [search_term_1] .. [search_term_n] [number]  </code>

Alternatively, if the required number is missing, the script will download a set default number of images. 

### Improvements
 
I assume the limit of 100 downloads per query can be bypassed by having Selenium scroll down the search results page. 

### Copyright

Copyright of downloaded images remains property of the rightful owners.
