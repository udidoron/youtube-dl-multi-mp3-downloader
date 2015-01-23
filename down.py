#!/usr/bin/env

import sys #for arguments
import os #for running external program calls
import re #for (minor) link processing


# Confirming: we have at least one link file
if len(sys.argv) < 2:
    print("USAGE: down.py <links file> <possible other links files>")
    exit(1)

# Creating files directory
dirname = "Youtube_MP3s"
try:
    os.mkdir(dirname)
except OSError:
    pass

# Preparing regex for youtube ID
idReg = re.compile("\?v=(.+)")

# Reading links file and converting each link
# Links file = one link per line
linkFiles = sys.argv[1:] #disregarding first argument, which is the program name
for linkfile in linkFiles:
    print("Opening file "+str(linkfile))
    for line in open(linkfile):
        #getting youtube ID
        youtubeID = idReg.search(line)
        if youtubeID == None:
            print("Invalid Youtube Link (no ID, i.e. no ?v=...)")
            continue
        downloadLink = "https://youtube.com/watch"+youtubeID.group(0)
        print("Attempting to download "+str(downloadLink))
        #downloading and converting file via external program
        os.system("youtube-dl.exe --prefer-ffmpeg --extract-audio --audio-format mp3 "+downloadLink)
        #moving converted file to folder
        os.system("move *.mp3 "+dirname)


print("All done!")



