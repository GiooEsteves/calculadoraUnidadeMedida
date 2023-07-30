from tkinter import *

#colors
color1 = '#3b3b3b'      #black

window = Tk()
window.title('conversor de medidas')
window.geometry('650x260')
window.configure(bg=color1)

#frames
up_frame = Frame(window, width=450, height=50, bg='red', pady=0, padx=3, relief='flat')
up_frame.place(x=2, y=2)

left_frame = Frame(window, width=450, height=220, bg='green', pady=0, padx=3, relief='flat')
left_frame.place(x=2, y=54)

right_frame = Frame(window, width=198, height=260, bg='white', pady=0, padx=3, relief='flat')
right_frame.place(x=454, y=2)

window.mainloop()
