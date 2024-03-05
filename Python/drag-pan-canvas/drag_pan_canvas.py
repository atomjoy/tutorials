from tkinter import *

def make():
    #makes a rectangle(for now)
    global lbl,lbl2
    lbl2=canvas.create_rectangle(50,30,70,50,fill="white",tags="tag")
    lbl=canvas.create_rectangle(20,0,40,20,fill="red",tags="tag")

def click_on_nodes(event):
    #start position of a rectangle when we click to move it(found online)
    global selected
    # convert (event.x, event.y) to canvas coordinates
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    selected = canvas.find_overlapping(x-5, y-5, x+5, y+5)
    if selected:
        canvas.tag_raise(selected)
        canvas.selected = selected[-1]  # select the top-most item
        canvas.startxy = (x, y)
        print(canvas.selected, canvas.startxy)
    else:
        canvas.selected = None
        print("none")

def drag_the_node(event):
    #position of rectangle while dragging it
    if selected:
        print(f"coords are: {canvas.coords(lbl)}")
        # convert (event.x, event.y) to canvas coordinates
        x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
        # calculate distance moved from last position
        dx, dy = x-canvas.startxy[0], y-canvas.startxy[1]
        # move the selected item
        canvas.move(canvas.selected, dx, dy)
        # update last position
        canvas.startxy = (x, y)
    else:
        canvas.selected==None

def pan_click(event):
    canvas.scan_mark(event.x,event.y)

def pan_move(event):
    canvas.scan_dragto(event.x,event.y,gain=1)
    print(f" winfox: {canvas.coords(lbl)}")

root=Tk()
canvas=Canvas(root,bg="#222222",width=500,height=500)
canvas.pack()
make()

#move the rectangles LEFT CLICK
canvas.bind("<Button-1>",click_on_nodes,add="+")
canvas.bind("<B1-Motion>",drag_the_node,add="+")

#pan the viewport RIGHT CLICK
canvas.bind("<ButtonPress-3>",pan_click)
canvas.bind("<B3-Motion>",pan_move)
# canvas.bind("<ButtonRelease-3>",mouse_up)

root.mainloop()