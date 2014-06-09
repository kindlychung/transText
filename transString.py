#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import urllib
from .simpleurl import SimpleUrl

def transString(orig_str, from_lang, to_lang):
    orig_str = unicode(orig_str)
    linkroot = "http://translate.google.com/m?sl=%s&hl=%s&q=" % \
        (from_lang, to_lang)
    # important, in python2 you need to encode this string in utf8 manually
    # , essentially, it's just break down a multi-byte char into single bytes
    query = urllib.quote(orig_str.encode("utf8"))
    link = linkroot + query
    soup = SimpleUrl(link).getsoup()
    res = soup.find_all("div", class_="t0")[0]
    res = res.string.strip()
    return res
