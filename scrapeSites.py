#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
from transText.simpleurl import SimpleUrl
from pygmail.Pygmail import Pygmail
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as ss
from transText.marksoup import marksoup

def sendnews(subj, markup):
    now = datetime.now()
    datestring = " %04d-%02d-%02d %02d:%02d" % (
        now.year, now.month, now.day,
        now.hour, now.minute
        )
    subj += datestring
    gmailtask = Pygmail()
    gmailtask.sendConfirmation("emma.dessin.belle@gmail.com",
                               subj,
                               markup)

def scrapeFun1(lemonde_url, from_lang, to_lang):
    lemond_worldnews = SimpleUrl(lemonde_url)
    page = lemond_worldnews()
    filtertag = ss("article")
    titletag = ss("title")
    souptitle = bs(page, "html.parser", parse_only=titletag)
    subj = souptitle.get_text()
    soup = bs(page, "html.parser", parse_only=filtertag)
    soupstr = soup.get_text()
    markup = marksoup(soupstr, from_lang, to_lang)
    sendnews(subj, markup)

# scrape LeMonde international
lemonde_urls = [
"http://www.lemonde.fr/international/1.html",
"http://www.lemonde.fr/sciences/1.html",
"http://www.lemonde.fr/economie/1.html"
    ]
for lemonde_url in lemonde_urls:
    scrapeFun1(lemonde_url, "fr", "en")

# scrape AD.nl
ad_urls = [
"http://www.ad.nl/ad/nl/1012/Nederland/index.dhtml",
"http://www.ad.nl/ad/nl/1013/Buitenland/index.dhtml",
"http://www.ad.nl/ad/nl/5595/Digitaal/index.dhtml",
"http://www.ad.nl/ad/nl/4561/Wetenschap/index.dhtml"
    ]
for ad_url in ad_urls:
    scrapeFun1(ad_url, "nl", "en")



