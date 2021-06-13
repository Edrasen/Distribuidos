import tkinter as tk
import urllib.request
from PIL import Image, ImageTk
import io


def ImgFromUrl(url):
    global image
    with urllib.request.urlopen(url) as connection:
        raw_data = connection.read()
    im = Image.open(io.BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    return image

root = tk.Tk()
url = "http://imgs.xkcd.com/comics/python.png"
widget = tk.Label(root, image=ImgFromUrl(url))
widget.grid(row=0, column=0)

root.mainloop()