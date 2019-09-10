from pytube import YouTube
from sys import argv
import os   
import pprint       
from subprocess import call          

downloadsDir = "./Downloads"
convertedDir = "./Converted"
vidUrl = "https://www.youtube.com/watch?v=txFEMT-3zSc" #funny Odd1sout video is default

def show_progress(stream, chunk, file_handle, bytes_remaining):
    #need to add something here to actually show progress
    return 

def convert_files():
    _files = [] 
    try:
        flist = [ f for f in os.listdir(downloadsDir) if f.endswith(".mp4") ]
        for f in flist:
            basename = os.path.basename(f) 
            fname = os.path.splitext(basename)[0]
            if not os.path.exists("{}/{}.mp3".format(convertedDir, fname) ):
                _files.append(fname)
    except OSError as e:
        pprint.pprint(e)
        exit(e)

    for fname in _files:
        call(["mplayer", "-novideo", "-nocorrect-pts", "-ao", "pcm:waveheader", downloadsDir + "/" + fname + ".mp4"])
        call(["lame", "-v", "audiodump.wav", convertedDir + "/" + fname + ".mp3"])
        os.remove("audiodump.wav")

if len(argv) > 1:
    vidUrl = argv[1]
    
yt = YouTube(vidUrl)
yt.register_on_progress_callback(show_progress)
yt.streams.filter(subtype='mp4', progressive=True).first().download(downloadsDir)

convert_files()