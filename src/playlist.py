import youtube_dl
import sys
import os


class Plist():
    def __init__(self, url):
        ydl_opts = {
            'format':'best',
            'outtmpl': '%(playlist)s/%(playlist_index)s __%(title)s',
            'yesplaylist':True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as pdl:
            pdl.download([url])
