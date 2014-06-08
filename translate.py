#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib
import urllib2
import urlparse
import subprocess
from .reportError import newError
from .reportError import newReport
from itertools import chain
import re
from bs4 import BeautifulSoup

class Translate:
    def __init__(self, orig_str, from_lang, to_lang):
        self.orig_str = orig_str
        self.orig_str = self.orig_str.replace("\n", " ").replace("\r", "")
        # important, extracts the unicode string from QString
        self.orig_str = unicode(orig_str)
        # self.orig_str = re.compile(r"[,.!:;?]").split(self.orig_str)
        self.orig_str = re.compile(r"(?:\. |\! |\; |\? )").split(self.orig_str)
        self.orig_str = [x.strip() for x in self.orig_str]
        self.orig_str_all = "____".join(self.orig_str)
        self.n_sentence = len(self.orig_str)
        self.trans_str = [None] * self.n_sentence
        self.from_lang = unicode(from_lang)
        self.to_lang = unicode(to_lang)

        agents = {'User-Agent': "Mozilla/4.0"}
        linkroot = "http://translate.google.com/m?sl=%s&hl=%s&q=" % \
            (self.from_lang, self.to_lang)
        # important, in python2 you need to encode this string in utf8 manually
        # , essentially, it's just break down a multi-byte char into single bytes
        query = urllib.quote(self.orig_str_all.encode("utf8"))
        link = linkroot + query
        print("from in Translate: ", self.from_lang)
        print("to in Translate: ", self.to_lang)
        print(link)
        request = urllib2.Request(link, headers=agents)
        webpage = urllib2.urlopen(request).read()
        soup = BeautifulSoup(webpage)
        res = soup.find_all("div", class_="t0")[0]
        res = res.string.strip()
        res = res.replace("\n", " ").replace("\r", "")
        res = unicode(res)
        res = res.split("____")
        for i in range(self.n_sentence):
            self.trans_str[i] = res[i]



    def __call__(self):
        newReport(self.trans_str[0])
        return self.trans_str

    def prettify(self):
        if len(self.trans_str) < 1:
            error_str = "You get an empty result. Something wrong with original text, or something wrong with google?"
            newError(error_str)
            raise Exception(error_str)
        list_sen = [["<div>" + self.orig_str[i] + "</div>",
                     "<div style='background-color: gray'>" + self.trans_str[i] + "</div>"] for i in range(self.n_sentence)]
        list_sen = chain.from_iterable(list_sen)
        list_sen = "".join(list_sen)
        return list_sen

            
            

# testfr = u"""
# Plus de 762 000.  candidats au baccalauréat. 
# Ces augmentations.  s'expliquent par la hausse.
# """
# x = Translate(testfr, "fr", "en")
# newReport(x.prettify())
