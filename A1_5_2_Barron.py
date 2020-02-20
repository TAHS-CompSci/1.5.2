import Tkinter 
root = Tkinter.Tk 
root = mainloop()
drawpad = Canvas(root, background='black')
drawpad.grid(row=0, column=1)
item = drawpad.create_oval(10, 50, 100, 100, fill='green')
drawpad.move(item, 100, 0) 
box= Checkbutton(root, text="Check here")
box.grid(row=0, column=0)
slider = Scale(root, from_=1, to-10, 
label="Speed", variable=speed) 
slider.grid(row=2, column=0)
speed.get()
editor = Text(width=30, height=4)
editor.grid(row=2, column=1, rowspan=2, sticky=SE)
speed = IntVar()
slider = Scale(root, from_=1, to=10, 
label+"Speed", variable=speed)
slider.grid(row=2, column=0)
times_pressed = 0
def pressed(): 
global times_pressed 
times_pressed = times_pressed + 1 
editor.insert(END, times_pressed)
editor.see(END)
button = Button(root, text+'Click me.',
                command=pressed)
button.grid(row=1, column=0) 

Canvas (window, width, height) 
my_canvas.create_image(x1, y1, image) 
my_canvas.create_arc(0, 50, 600, 650, start = 30, extend = 120, width = 68, style = ARC)
my_canvas.create_line(200, 250, 100, 150)
my_canvas.create_oval(0, 100, 200, 250)
my_canvas.create_rectangle(100, 200, 50, 100)
my_canvas.create_text(100, 200, 100, 200) 

canvas.intemconfig(circles[2], outline='black')
a, b, c, d = canvas.coords(circles[2])
canvas.coords(circles[2], a, b-5, c, d-5) 

import os.path 
directory = os.path.dirname(os.path.abspath(_file_))
filename = os.path.join(directory, 'canopyIcon.jpg')
import PIL.Image, PTL.ImageTk 
img = PIL.Image.open(filename)
tkimg = PIL.ImageTk.PhotoImage(img)
icon = canvas.create_image(tkimg, 150, 250)
icon = canvas.create_image(150, 250, image=tkimg)

canvas.tag_lower(icon, check) 

root.main_loop() 