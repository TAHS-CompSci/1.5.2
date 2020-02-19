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
