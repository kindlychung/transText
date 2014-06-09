#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from datetime import datetime
from transText.simpleurl import SimpleUrl
from pygmail.Pygmail import Pygmail
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as ss
from transText.transString import transString


lemond_worldnews = SimpleUrl("http://www.lemonde.fr/international/1.html")
page = lemond_worldnews()
filterclass = ss("article")
soup = bs(page, "html.parser", parse_only=filterclass)
soup.span.decompose()
soupstr = soup.get_text()
soupstr_list = re.split(r"\n+", soupstr)
soupstr_list = [x.strip() for x in soupstr_list if len(x.strip()) > 15]
listlen = len(soupstr_list)
trans_list = [None] * listlen

for i in range(listlen):
    trans_list[i] = transString(soupstr_list[i], "fr", "en")

markuplist = [None] * listlen
for i in range(listlen):
    # source markup
    s1 = """
    <div
    style='
    padding: 7px;
    margin-top: 20px;
    background-color: PeachPuff'>
    %s
    </div>""" % soupstr_list[i]
    # translation markup
    s2 = """
    <div
    style='
    padding: 7px;
    background-color: LightCyan'>
    %s
    </div>""" % trans_list[i]
    s = s1 + s2
    markuplist[i] = s
markup = "".join(markuplist)

now = datetime.now()
subj = "LeMonde.fr International %04d-%02d-%02d %02d:%02d" % (
    now.year, now.month, now.day,
    now.hour, now.minute
    )
gmailtask = Pygmail()
gmailtask.sendConfirmation("emma.dessin.belle@gmail.com",
                           subj,
                           markup.encode("utf8"))
