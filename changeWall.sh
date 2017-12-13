#!/usr/bin/env bash

echo $(nm-online) $? connection problems
date=`date +%Y-%m-%d`
source venv.sh
echo "ENV changed"
echo "Downloading New Wallpaper ... "
python bing.py
path="/home/manoj/projects/dosome/image/$date.jpg"
echo Wallpaper tiled from $path
nitrogen --set-auto $path
deactivate
