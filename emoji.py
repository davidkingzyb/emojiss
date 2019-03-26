# -*- coding: utf-8 -*-
# python3
# 2017/9/14 by DKZ
import os
import json
from PIL import Image

def findSurrogatePair(point):
    offset = point - 0x10000
    lead = 0xd800 + (offset >> 10)
    trail = 0xdc00 + (offset & 0x3ff)
    return hex(lead)+hex(trail)

def unicodeToString(point):
    c=json.dumps({'d':chr(point)}).replace('\\u','0x')[7:-2]
    return c

def convertUnicodeEmoji():
    files=os.listdir('./emoji_src')
    for file in files:
        if 'type' not in file and file != '.DS_Store' and '.png' in file:
            print(file)
            unicode_name=file.split('_').pop().split('.').pop(0).split('-').pop(0)
            utf8_name=unicodeToString(int(unicode_name,16))
            print(unicode_name,utf8_name)
            src_image = Image.open('./emoji_src/'+file);  
            src_image.resize((35,35),Image.ANTIALIAS).save('./emoji_dist/'+utf8_name+'.png')

def test():
    print(findSurrogatePair(int('1f436',16)))
    print(unicodeToString(int('1f436',16)))
    print(findSurrogatePair(int('262f',16)))
    print(unicodeToString(int('262f',16)))
    # convertUnicodeEmoji()

if __name__ == '__main__':
    convertUnicodeEmoji()
    # test()