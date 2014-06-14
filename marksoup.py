#!/usr/bin/python3
# -*- coding: utf-8 -*-

from transText.transString import transString
import re

def marklist(soupstr_list, trans_list):
    listlen = len(soupstr_list)
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
    return markuplist

def marksoup(soupstr, from_lang, to_lang, countlimit=25):
    soupstr_list = re.split(r"\n+", soupstr)
    soupstr_list = [x.strip() for x in soupstr_list if len(x.strip()) > countlimit]
    listlen = len(soupstr_list)
    trans_list = [None] * listlen

    for i in range(listlen):
        trans_list[i] = transString(soupstr_list[i], from_lang, to_lang)

    markuplist = marklist(soupstr_list, trans_list)
    markup = "\n".join(markuplist)
    return markup

def translist(soupstr, from_lang, to_lang):
    soupstr_list = re.split(r"\n+", soupstr)
    soupstr_list = [x.strip() for x in soupstr_list]
    soupstr_list = [x for x in soupstr_list if x]
    listlen = len(soupstr_list)
    trans_list = [None] * listlen
    for i in range(listlen):
        trans_list[i] = transString(soupstr_list[i], from_lang, to_lang)

    return "\n".join(trans_list)

def markToFile(infn, outfn, from_lang, to_lang, countlimit=25):
    with open(infn) as infh:
        soupstr = infh.read()
    trans_str = marksoup(soupstr, from_lang, to_lang, countlimit)
    with open(outfn, "w") as outfh:
        outfh.write(trans_str)
    
