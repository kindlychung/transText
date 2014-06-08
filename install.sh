#!/bin/bash

packdir=$(pwd)
packbase=$(basename "$packdir")
cd ..
sudo cp -av "$packdir" /usr/lib/python3/dist-packages/
ln -s /usr/lib/python3/dist-packages/$packbase/tt.py $HOME/bin/
