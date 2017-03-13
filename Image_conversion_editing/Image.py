'''
Created on 12-Mar-2017
# How to convert many JPG images to PNG by single code  
@author: Ayush
'''

from PIL import Image
import webbrowser
import os

for f in os.listdir('.'):
    if f.endswith('.JPG'):
        i = Image.open(f)
        fn, ftext = os.path.splitext(f)
        i.save('png\{}.png'.format(fn))

#image1 = Image.open('DSC_0231.jpg')
# webbrowser.open('DSC_0231.jpg')
