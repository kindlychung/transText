#!/bin/bash

packdir=$(pwd)
packbase=$(basename "$packdir")
cd ..
sudo rsync -avu "$packdir" /usr/lib/python2.7/dist-packages/
write_it=true
ttpy=$HOME/bin/tt.py
echo $ttpy
if [[ -e $ttpy ]]; then
    kdialog --title "Confirm overwrite file" --yesno "$ttpy already exists, overwrite?"
    if [[ $? != 0 ]]; then
        write_it=false
    fi
fi

# only overwrite with permission
if $write_it; then
    rm "$ttpy"
    ln -s /usr/lib/python2.7/dist-packages/$packbase/tt.py $ttpy
fi
