#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.parse
from .simpleurl import SimpleUrl


def transString(orig_str, from_lang, to_lang):
    linkroot = "http://translate.google.com/m?sl=%s&hl=%s&q=" % \
        (from_lang, to_lang)
    # important, in python2 you need to encode this string in utf8 manually
    # , essentially, it's just break down a multi-byte char into single bytes
    query = urllib.parse.quote(orig_str)
    link = linkroot + query
    soup = SimpleUrl(link).getsoup()

    res = soup.find_all("div", class_="t0")[0]
    res = res.string.strip()
    return res
