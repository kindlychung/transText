#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib
import urllib2
import urlparse
from bs4 import BeautifulSoup as bs

class SimpleUrl:
    def __init__(self, link, agent = {'User-Agent': "Mozilla/5.0"}):
        self.link = unicode(link)
        self.agent = agent
        request = urllib2.Request(self.link.encode("utf8"), headers=self.agent)
        self.webpage = urllib2.urlopen(request).read()
    def __call__(self):
        return self.webpage
    def getsoup(self):
        return bs(self.webpage)

