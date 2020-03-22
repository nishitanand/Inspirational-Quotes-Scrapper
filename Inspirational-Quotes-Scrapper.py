#!/usr/bin/env python
# coding: utf-8




from bs4 import BeautifulSoup
import requests

from tqdm import tqdm
import time
import math
import mimetypes


b=input("Enter the name which you want to give to the file ")
url="https://www.passiton.com/inspirational-quotes"
r=requests.get(url)
r.url
soup=BeautifulSoup(r.content,features="html.parser")
r.content
products = soup.findAll('div', attrs = {"class": "col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top"})
i=0
for product in products:
        img_tag = product.find('img')
        if 'alt' in img_tag.attrs:
            img_text = img_tag.attrs['alt']
            img_text=img_text.split("#")[0]
            i+=1
            with open("Inspirational_Quotes/"+ b +".txt","a+") as file: # Write binary file mode
                file.write("Quote number "+ str(i) +"\n")
                file.write(img_text)
                file.write("\n")






