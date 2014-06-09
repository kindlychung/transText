#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
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
    s1 = "<div>%s</div>" % soupstr_list[i]
    s2 = "<div style='background-color: gray'><b>%s<b></div>" % trans_list[i]
    s = s1 + s2
    markuplist[i] = s
markup = "".join(markuplist)

gmailtask = Pygmail()
gmailtask.sendConfirmation("emma.dessin.belle@gmail.com",
                           "articles a la une",
                           markup.encode("utf8"))
