'''
Created on 12-Mar-2017
#Re-size your images
@author: Ayush
'''
from PIL import Image
import webbrowser
import os
size_1000 = (500, 500)

for f in os.listdir('.'):
    if f.endswith('.JPG'):
        i = Image.open(f)
        fn, ftext = os.path.splitext(f)
        i.thumbnail(size_1000)
        i.save('resize\{}.png'.format(fn))

#image1 = Image.open('DSC_0231.jpg')
# webbrowser.open('DSC_0231.jpg')
