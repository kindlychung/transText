#!/bin/bash

packdir=$(pwd)
packbase=$(basename "$packdir")
cd ..
sudo rsync -avu "$packdir" /usr/lib/python3/dist-packages/
ln -s "/usr/lib/python3/dist-packages/$packbase/tt.py" "$HOME/bin/tt.py"
ln -s "/usr/lib/python3/dist-packages/$packbase/scrapeSites.py" "$HOME/bin/scrapeSites.py"
