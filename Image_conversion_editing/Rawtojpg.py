'''
Created on 12-Mar-2017
# COnverting RAW format into JPG
@author: Ayush
'''
import rawpy
from PIL import Image
import os

for f in os.listdir('.'):
    if f.endswith('NEF'):
        raw = rawpy.imread(f)
        rbg = raw.postprocess()
        img = Image.fromarray(rbg)
        fn, ftext = os.path.splitext(f)
        img.save('jpg\{}.png'.format(fn))
        print fn
