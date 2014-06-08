#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import subprocess
from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from transText.translate import Translate
from transText.reportError import newError
from transText.reportError  import newReport


class Form(QWidget):
    def __init__(self, npane):
        QWidget.__init__(self)
        self.lang_opts = ["fr", "nl", "en"]
        self.to_lang_opts = ["en", "fr", "nl"]

        self.clip = QApplication.clipboard()
        self.from_textp = QPlainTextEdit()
        self.to_textp = QTextEdit()
        self.lang = "auto"
        self.lang_combo = QComboBox()
        self.to_lang = "en"
        self.to_lang_combo = QComboBox()
        self.lang_combo.addItems(self.lang_opts)
        self.to_lang_combo.addItems(self.to_lang_opts)

        grid = QGridLayout()
        if npane == 2:
            grid.addWidget(self.from_textp, 0, 0)
        elif npane == 1:
            pass
        else:
            newError("Invalid number of panes!")

        grid.addWidget(self.to_textp, 0, 1)
        grid.addWidget(self.lang_combo, 1, 1)
        grid.addWidget(self.to_lang_combo, 2, 1)
        self.setLayout(grid)

        self.clip.selectionChanged.connect(self.transSelect)
        self.lang_combo.currentIndexChanged.connect(self.updateFromLang)
        self.to_lang_combo.currentIndexChanged.connect(self.updateToLang)
        self.from_textp.textChanged.connect(self.updateTrans)

    def updateFromLang(self):
        self.lang = unicode(self.lang_combo.currentText())
        print("from in updateFromLang: ", self.lang)
        self.updateTrans()
    def updateToLang(self):
        self.to_lang = unicode(self.to_lang_combo.currentText())
        print("to in updateToLang: ", self.to_lang)
        self.updateTrans()
    def updateTrans(self):
        from_text = self.from_textp.toPlainText()
        trans_text = Translate(from_text, self.lang, self.to_lang)
        trans_html = trans_text.prettify()
        self.to_textp.setText(trans_html)

    def transSelect(self):
        selText = self.clip.text(QClipboard.Selection)
        if len(selText) < 140:
            res = Translate(selText, self.lang, self.to_lang)
            res()


def main():
    app = QApplication(sys.argv)
    form = Form(2)
    form.show()
    app.exec_()
main()

# def main():
#     app = QApplication(sys.argv)
#     form = Form(int(sys.argv[1]))
#     form.show()
#     app.exec_()

# if __name__ == '__main__':
#     main()

import feedparser

