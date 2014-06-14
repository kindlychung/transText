#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup as bs

class SimpleUrl:
    def __init__(self, link, agent = {'User-Agent': "Mozilla/5.0"}):
        self.link = link
        self.agent = agent
        request = urllib.request.Request(self.link, headers=self.agent)
        self.webpage = urllib.request.urlopen(request).read()
    def __call__(self):
        return self.webpage
    def getsoup(self):
        return bs(self.webpage)

