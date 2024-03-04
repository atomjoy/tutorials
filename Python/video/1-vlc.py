# Install
# python-array, python-vlc, tk, pyaudio, playsound

# Vlc player doc
# https://www.olivieraubert.net/vlc/python-ctypes/doc/

# Vlc doc
# https://www.olivieraubert.net/vlc/python-ctypes/doc/

# Tuts
# https://copyprogramming.com/howto/python-python-play-video-with-sound-code-example
# https://www.makeuseof.com/python-video-media-player-how-to-build/
# https://www.geeksforgeeks.org/python-vlc-mediaplayer-getting-track/
# https://www.geeksforgeeks.org/python-vlc-mediaplayer-checking-if-it-is-playing-or-not/
# https://pyglet.readthedocs.io/en/latest/programming_guide/media.html
#  OpenCv
# https://copyprogramming.com/howto/python-playing-a-video-with-audio-with-opencv?utm_content=cmp-true
# https://www.tutorialspoint.com/opencv_python/opencv_python_play_video_file.htm
# https://stackoverflow.com/questions/37799847/python-playing-a-video-with-audio-with-opencv

import vlc, array, pyaudio, time, tkinter
from numpy import *
from pyaudio import *
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class Screen(Frame):
    '''
        Screen widget: Embedded video player from local or youtube
    '''
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg = 'black')
        self.settings = { # Inizialazing dictionary settings
            "width" : 512,
            "height" : 288
        }
        self.settings.update(kwargs) # Changing the default settings
        # Open the video source |temporary
        self.video_source =  'video.mp4'
        # Canvas where to draw video output
        self.canvas = Canvas(self, width = self.settings['width'], height = self.settings['height'], bg = "#fff", highlightthickness = 2)        
        self.canvas.pack(expand=True, fill='both')                
        # Creating VLC player
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
    def GetHandle(self):
        # Getting frame ID
        return self.winfo_id()
    def play(self, _source = "video.mp4"):
        # Function to start player from given source
        Media = self.instance.media_new(_source)
        Media.get_mrl()
        self.player.set_media(Media)
        # Play
        self.player.set_hwnd(self.GetHandle())
        self.player.play()
        time.sleep(1)    
    def addBg(self):
        img = ImageTk.PhotoImage(Image.open('error-small.png'))
        self.canvas.create_image(0, 0, image=img, anchor='nw')
    def generate_sample(self, ob, preview):
        print("* Generating sample...")
        tone_out = array(ob, dtype=int16)
        if preview:
            print("* Previewing audio file...")
            bytestream = tone_out.tobytes()
            pya = pyaudio.PyAudio()
            stream = pya.open(format=pya.get_format_from_width(width=2), channels=1, rate=128, output=True)
            stream.write(bytestream)
            stream.stop_stream()
            stream.close()
            pya.terminate()
            print("* Preview completed!")
        else:
            pya.write('sound.wav', 128, tone_out)
            print("* Wrote audio file!")

# if __name__ == "__main_":
root = Tk()
frm = ttk.Frame(root, padding=10)
frm = Screen(root)
frm.grid()
frm.play("video.mp4")

# frm.addBg()
# frm.player.set_position(0.01)
print("Video count", frm.player.video_get_track_count())
print("Video exist", frm.player.video_get_track())

if frm.player.is_playing():    
    print("Video count", frm.player.video_get_track_count())
    print("Video exist", frm.player.video_get_track())
    print("Playing....")    
    # ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()