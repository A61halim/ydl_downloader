import youtube_dl
import sys

class video():
    def __init__(self, url):
        ydl_options = {
            'format':'best',
            'outtmpl': '/home/topo/Desktop/COURSE/%(title)s',
            'noplaylist':True,
        }
        with youtube_dl.YoutubeDL(ydl_options) as vdl:
            vdl.download([url])