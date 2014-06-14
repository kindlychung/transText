#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
from .reportError import newError
from .reportError import newReport
from .transString import transString
from itertools import chain
import re

class Translate:
    def __init__(self, orig_str, from_lang, to_lang):
        self.orig_str_copy = orig_str
        self.orig_str = orig_str
        self.orig_str = self.orig_str.replace("\n", " ").replace("\r", "")
        # important, extracts the string from QString
        self.orig_str = re.compile(r"(?:\. |\! |\; |\? )").split(self.orig_str)
        self.orig_str = [x.strip() for x in self.orig_str]
        self.orig_str_marked = "____".join(self.orig_str)
        self.n_sentence = len(self.orig_str)
        self.trans_str = [None] * self.n_sentence
        self.from_lang = from_lang
        self.to_lang = to_lang

        res = transString(self.orig_str_marked, self.from_lang, self.to_lang)
        res = res.replace("\n", " ").replace("\r", "")
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
