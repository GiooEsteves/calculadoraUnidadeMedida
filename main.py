from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

#colors
color1 = '#3b3b3b'      #black
color2 = '#ffffff'      #white
color3 = '#48b3e0'      #blue

window = Tk()
window.title('conversor de medidas')
window.geometry('650x260')
window.configure(bg=color1)

#frames
up_frame = Frame(window, width=450, height=50, bg=color2, pady=0, padx=3, relief='flat')
up_frame.place(x=2, y=2)

left_frame = Frame(window, width=450, height=220, bg=color2, pady=0, padx=3, relief='flat')
left_frame.place(x=2, y=54)

right_frame = Frame(window, width=198, height=260, bg=color2, pady=0, padx=3, relief='flat')
right_frame.place(x=454, y=2)

up_right_frame = Frame(window, width=198, height=50, bg=color2, pady=0, padx=3, relief='flat')
up_right_frame.place(x=454, y=2)

#window style
style = ttk.Style(window)
style.theme_use("clam")

#labels
l_app_name = Label(up_frame, text='Calculadora de Unidade de Medidas', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=color2, fg=color3)
l_app_name.place(x=50, y=10)

l_unity_choose = Label(up_right_frame, text='Massa', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=color2, fg=color1)
l_unity_choose.place(x=60, y=10)

#buttons
img_0 = Image.open('images/massa.png')
img_0 = img_0.resize((50,50), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)

b_0 = Button(left_frame, text='Massa', image=img_0, width=16, height=3, relief='flat', overrelief='solid', font=('Ivy 10 bold'), bg = color3, fg=color2)
b_0.grid(row = 0, column=0, sticky=NSEW, pady=4, padx=5)

b_1 = Button(left_frame, text='Tempo', width=16, height=3, relief='flat', overrelief='solid', font=('Ivy 10 bold'), bg = color3, fg=color2)
b_1.grid(row = 0, column=1, sticky=NSEW, pady=4, padx=5)

b_2 = Button(left_frame, text='Comprimento', width=16, height=3, relief='flat', overrelief='solid', font=('Ivy 10 bold'), bg = color3, fg=color2)
b_2.grid(row = 0, column=2, sticky=NSEW, pady=4, padx=5)

b_3 = Button(left_frame, text='Área', width=16, height=3, relief='flat', overrelief='solid', font=('Ivy 10 bold'), bg = color3, fg=color2)
b_3.grid(row = 1, column=0, sticky=NSEW, pady=4, padx=5)

b_4 = Button(left_frame, text='Quantidade', width=16, height=3, relief='flat', overrelief='solid', font=('Ivy 10 bold'), bg = color3, fg=color2)
b_4.grid(row = 1, column=1, sticky=NSEW, pady=4, padx=5)

b_5 = Button(left_frame, text='Velocidade', width=16, height=3, relief='flat', overrelief='solid', font=('Ivy 10 bold'), bg = color3, fg=color2)
b_5.grid(row = 1, column=2, sticky=NSEW, pady=4, padx=5)

b_6 = Button(left_frame, text='Temperatura', width=16, height=3, relief='flat', overrelief='solid', font=('Ivy 10 bold'), bg = color3, fg=color2)
b_6.grid(row = 2, column=0, sticky=NSEW, pady=4, padx=5)

b_7 = Button(left_frame, text='Energia', width=16, height=3, relief='flat', overrelief='solid', font=('Ivy 10 bold'), bg = color3, fg=color2)
b_7.grid(row = 2, column=1, sticky=NSEW, pady=4, padx=5)

b_8 = Button(left_frame, text='Pressão', width=16, height=3, relief='flat', overrelief='solid', font=('Ivy 10 bold'), bg = color3, fg=color2)
b_8.grid(row = 2, column=2, sticky=NSEW, pady=4, padx=5)

window.mainloop()
