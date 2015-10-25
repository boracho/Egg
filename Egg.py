#!/usr/bin/env python


'''
The MIT License (MIT)

Copyright (c) [2015] [Eric M Stinger]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


#Grabs yer podcasts from the supplied rss feeds, deletes them after the 
#specified time has passed.

#Obtain xml from rss URL in rss list.  If none in rss, end.
#Parse for download urls and return a list of them
#for auto dl, check to see if most recent has already been dl'd
#if not, download, then add filename and dl date 'Egg' tuple to dl list
#if Egg is expired, per user provided timeframe, delete it.

import requests
from xml.etree import ElementTree as Etree
import json



class Egg(object):
    
    def __init__(self, carton, url):
        self.carton = carton
        self.url = url
    
    
    def carton_unpack(self):
        for egg in self.carton:
            yield egg
    
    
    