# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nNtRq9yovCwQmXpYk6Ugq1Uufz7tMthT
"""

from newsplease import NewsPlease
import time
url1='https://timesofindia.indiatimes.com/india/bengaluru-firm-to-build-moon-lander-for-nasa-2020-mission/articleshow/69684821.cms'
url2='https://www.nytimes.com/2017/02/23/us/politics/cpac-stephen-bannon-reince-priebus.html?hp'
url=[]
for i in range(100):
    url.append(url2)

tic=time.time()
a=NewsPlease.from_urls(url)
toc=time.time()
print(toc-tic)
print(a[url2].title)

