#!/usr/bin/python3

import subprocess

def newError(msg):
    subprocess.Popen(["kdialog",
                      "--title", "transText error",
                      "--passivepopup",
                      """<font color="red">""" + msg + """</font>"""])
    raise Exception(msg)

def newReport(msg):
    subprocess.Popen(["kdialog",
                      "--title", "transText msg",
                      "--passivepopup", msg])

