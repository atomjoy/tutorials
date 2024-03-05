# https://stackoverflow.com/questions/69017940/when-i-scan-dragto-to-pan-my-canvas-all-canvas-items-move-properly-but-their
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
# https://python-course.eu/tkinter/events-and-binds-in-tkinter.php?ref=driverlayer.com/web
# https://www.geeksforgeeks.org/python-find-the-tuples-containing-the-given-element-from-a-list-of-tuples/
# https://python.hotexamples.com/examples/Tkinter/Canvas/scan_dragto/python-canvas-scan_dragto-method-examples.html

import customtkinter

from tkinter import Canvas
from PIL import Image, ImageTk

global selected

def make():
    global bug1, bug2
    bug1=my_canvas.create_rectangle(0,0,50,50,fill="#55cc55",tags="wall")
    bug2=my_canvas.create_rectangle(50,50,150,150,fill="#ff5500",tags="player")

def winfo_height(self):
        return self.canvas.winfo_height()

def winfo_width(self):
    return self.canvas.winfo_width()

def move(event):
    global selected
    print("Drag canvas", event.widget)
    # my_canvas.moveto(my_image,event.x-50,event.y-50)
    # Start position of a rectangle when we click to move it  
    # convert (event.x, event.y) to canvas coordinates
    x, y = my_canvas.canvasx(event.x), my_canvas.canvasy(event.y)
    # Get all ids
    # selected = my_canvas.find_all()    
    # Get all selected objects ids with tag
    # selected = my_canvas.find_withtag("player")
    # Get all selected objects ids in box
    selected = my_canvas.find_overlapping(x-5, y-5, x+5, y+5)
    if selected:
        for i in selected:
            # Get selected objects tags
            tags = my_canvas.gettags(i)
            # Count tags with tag player
            if len(list(filter(lambda x: 'player' in x, tags))) > 0:
                my_canvas.tag_raise(selected) # Move to top
                my_canvas.selected = selected[-1]  # Select the top-most item
                my_canvas.startxy = (x, y)
                print("Moved", my_canvas.selected, my_canvas.startxy)
            else:
                my_canvas.selected = None
                print("None")   
    else:
        my_canvas.selected = None
        print("None")

def drag(event):
    display_coords(event)
    global selected
    # Position of rectangle while dragging it
    if my_canvas.selected:
        print(f"Coords are: {my_canvas.coords(my_image)}")
        # Convert (event.x, event.y) to canvas coordinates
        x, y = my_canvas.canvasx(event.x), my_canvas.canvasy(event.y)
        # Calculate distance moved from last position
        dx, dy = x-my_canvas.startxy[0], y-my_canvas.startxy[1]
        # Move the selected item
        my_canvas.move(my_canvas.selected, dx, dy)
        # Update last position
        my_canvas.startxy = (x, y)
    else:
        my_canvas.selected==None

def pan_click(event):
    my_canvas.scan_mark(event.x,event.y)

def pan_move(event):
    # pan_move
    my_canvas.scan_dragto(event.x, event.y, gain=1)
    print(f" Pan Image: {my_canvas.coords(my_image)}")

def display_coords(event):
    my_label.configure(text=f"X: {event.x} Y:{event.y}")

app = customtkinter.CTk()
app.geometry('500x500')

frame1 = customtkinter.CTkFrame(master=app)
frame1.pack(padx=40,pady=40, expand=True, fill="both")

my_canvas = Canvas(master=frame1,width=500,height=500,bg="#fff")
my_canvas.pack(expand=True, fill="both")
make()

#Resize image(originally 512 x 512)
img = Image.open("error.png")
resized_image = img.resize((130,130))
image = ImageTk.PhotoImage(resized_image)
frame1.image = image

# Always set image as global (tkinter errors)
global my_image
my_image = my_canvas.create_image(0, 0, image=image, anchor="nw", tags="player")

# Move left button
my_canvas.bind("<Button-1>",move,add="+")
my_canvas.bind("<B1-Motion>",drag,add="+")

# Pan right button
my_canvas.bind("<Button-3>", pan_click)
my_canvas.bind("<Button3-Motion>", pan_move)

# Or add events only for canvas objects with tag
# my_canvas.tag_bind("player","<Button-1>",move,add="+")
# my_canvas.tag_bind("player","<B1-Motion>",drag,add="+")

# Follow cursor
# my_canvas.bind("<Motion>", cursor_follow)

# Restrict canvas area (pan_move)
# my_canvas.configure(scrollregion=my_canvas.bbox(my_image))

# Provides X-Y coordinates of mouse cursor when canvas object is selected
my_label = customtkinter.CTkLabel(master=my_canvas, text="X: None Y: None")
my_label.pack(padx="10px", pady="10px", anchor="se")

app.mainloop()