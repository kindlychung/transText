#!/bin/bash

packdir=$(pwd)
packbase=$(basename "$packdir")
cd ..
sudo rsync -avu "$packdir" /usr/lib/python2.7/dist-packages/
ln -s "/usr/lib/python2.7/dist-packages/$packbase/tt.py" "$HOME/bin/tt.py"
ln -s "/usr/lib/python2.7/dist-packages/$packbase/scrapeSites.py" "$HOME/bin/scrapeSites.py"
