### https://github.com/PaulleDemon/tkVideoPlayer ###

import tkinter as tk
from tkVideoPlayer import TkinterVideo

root = tk.Tk()
root.geometry("1920x1080+0+0")
#root.attributes('-alpha',0.65)

fn = 'test2.mp4'
#fn = 'i.mov'
#fn = 'out01.mov'
#fn = 'out03.mkv'

#def loop(e): videoplayer.play()

#videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer = TkinterVideo(master=root)
videoplayer.load(fn)
videoplayer.pack(expand=True, fill="both")
#videoplayer.bind("<<Ended>>", loop)

videoplayer.play() # play the video

root.mainloop()

### end ###
