#!/usr/bin/env bash
python blog_icon_generator.py
convert -background none blog_icon.svg blogo_256.png
convert -background none -resize 512x512 blog_icon.svg blogo_512.png
convert -background none -resize 128x128 blog_icon.svg blogo_128.png
convert -background none -resize 64x64 blog_icon.svg blogo_64.png
convert -background none -resize 32x32 blog_icon.svg blogo_32.png
