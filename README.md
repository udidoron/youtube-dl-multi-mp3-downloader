# youtube-dl-multi-mp3-downloader
Small wrapping script in Python, which allows downloading multiple YouTube files' audio into mp3 files. Uses youtube-dl, ffmpeg and ffprobe.

Currently works only for Windows (sorry). Tested on Windows 7.

Requirements
====
* youtube-dl.exe
* ffmpeg.exe
* ffprobe.exe

(All in same folder)  
Also, Python (2.7 or 3), either available via the PATH environment variable (preferable) or via copying the program to the down.py location.

ffmpeg and ffprobe can be downloaded together from same ffmpeg build.  
I personally used Zeranoe FFmpeg:
http://ffmpeg.zeranoe.com/builds/

Usage instructions:
===
From the command line interface:  
<code> down.py [links file]...[links file] </code>  
Where a links file contains valid YouTube links, line-separated. At least one links file must be submitted to the script.

