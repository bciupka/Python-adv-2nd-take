# coding=windows-1250

import os
import urllib.request

data_dir = r"D:\Projekty\Kursy Python\Python - Advanced - VS\S02 - zmienne i kod\PLIKI"

pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'nonexistent', 'url': 'http://www.mobilo24.eu/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]


for i in pages:
    path = os.path.join(data_dir, i.get("name")+".html")
    try:
        urllib.request.urlretrieve(i.get("url"), path)
    except Exception as e:
        print(e)
        break
else:
    print("urls downloaded")
