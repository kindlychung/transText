#!/usr/bin/python3

import urllib.request
import urllib.parse
import subprocess
from .reportError import newError
from .reportError import newReport
from itertools import chain

class Translate:
    def __init__(self, orig_str, from_lang, to_lang):
        orig_str = orig_str.replace("\n", " ").replace("\r", "")
        self.orig_str = orig_str.split(". ")
        self.n_sentence = len(self.orig_str)
        self.trans_str = [None] * self.n_sentence
        self.from_lang = from_lang
        self.to_lang = to_lang
        agents = {'User-Agent': "Mozilla/4.0"}
        linkroot = "http://translate.google.com/m?sl=%s&hl=%s&q=" % \
            (from_lang, to_lang)
        for i in range(self.n_sentence):
            query = urllib.parse.quote(self.orig_str[i])
            link = linkroot + query
            print(link)
            request = urllib.request.Request(link, headers=agents)
            webpage = urllib.request.urlopen(request).read()
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(webpage)
            res = soup.find_all("div", class_="t0")[0]
            print("res", i, res)
            res = res.string.strip()
            res = res.replace("\n", " ").replace("\r", "")
            self.trans_str[i] = res



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
        print(list_sen)
        list_sen = "".join(list_sen)
        print(list_sen)
        return list_sen

            
            

# testfr = """
# Plus de 762 000.  candidats au baccalauréat. 
# Ces augmentations.  s'expliquent par la hausse.
# """
# x = Translate(testfr, "fr", "en")
# newReport(x.prettify())
