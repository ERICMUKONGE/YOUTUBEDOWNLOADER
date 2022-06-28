from tkinter import *
from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

canv = Tk()
canv.geometry("400x350")
canv.title("YouTubeDownloader")
Label(canv,text="Welcome to youtube downloader!!!").pack()
lvar = StringVar()
lvar.set("Enter the Youtube Video URL")
Label(canv, textvariable=lvar).pack()
url = StringVar()
Entry(canv, textvariable=url, width=30).pack(pady=10)

def download():
    try:
        lvar.set("Downloading...")
        canv.update()
        YouTube(url.get()).streams.first().download()
        lvar.set("Video Downloaded Successfully")
    except Exception as e:
        lvar.set("Error:" + str(e))
        canv.update()

Button(canv, text="Download", command=download).pack()
canv.mainloop()            
