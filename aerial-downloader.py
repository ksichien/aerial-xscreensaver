#!/usr/bin/python3
"""
This script will download the Apple TV Aerial videos to an 'Aerial' folder in the home directory.
Inspired by https://gist.github.com/Dhertz/9dd69eaad092d0c0fe96 and https://github.com/graysky2/xscreensaver-aerial
"""
import json
import os
import shutil
import requests

DLDIR = os.getenv("HOME") + '/Aerial/'

if not os.path.exists(DLDIR):
    os.makedirs(DLDIR)

RSP = requests.get('http://a1.phobos.apple.com/us/r1000/000/Features/atv/AutumnResources/' +
                   'videos/entries.json')

ARL = json.loads(RSP.text)
for aerial in ARL:
    for asset in aerial['assets']:
        filename = (asset['accessibilityLabel'].replace(" ", "-") + '-' +
                    asset['timeOfDay'] + '-' + asset['id'] + '.mov')
        filepath = DLDIR + filename
        if not os.path.isfile(filepath):
            print("Downloading %s" % (asset['url'],))
            video = requests.get(asset['url'], stream=True)
            with open(filepath, "wb") as videoFile:
                print("Writing %s to %s" % (filename, DLDIR))
                for chunk in video.iter_content(chunk_size=1024):
                    if chunk:
                        videoFile.write(chunk)

shutil.copy2('./aerial-player.sh', '/usr/lib/xscreensaver/aerial')
