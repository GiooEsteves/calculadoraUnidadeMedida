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
img_0 = img_0.resize((40,40), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)
b_0 = Button(left_frame, text=' Massa', image=img_0, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', font=('Ivy 11 bold'), bg = color3, fg=color1)
b_0.grid(row = 0, column=0, sticky=NSEW, pady=5, padx=5)

img_1 = Image.open('images/tempo.png')
img_1 = img_1.resize((40,40), Image.ANTIALIAS)
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(left_frame, text=' Tempo', image=img_1, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', font=('Ivy 11 bold'), bg = color3, fg=color1)
b_1.grid(row = 0, column=1, sticky=NSEW, pady=5, padx=5)

img_2 = Image.open('images/comprimento.png')
img_2 = img_2.resize((40,40), Image.ANTIALIAS)
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(left_frame, text='Comprimento', image=img_2, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', font=('Ivy 11 bold'), bg = color3, fg=color1)
b_2.grid(row = 0, column=2, sticky=NSEW, pady=5, padx=5)

img_3 = Image.open('images/area.png')
img_3 = img_3.resize((40,40), Image.ANTIALIAS)
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(left_frame, text='  Área', image=img_3, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', font=('Ivy 11 bold'), bg = color3, fg=color1)
b_3.grid(row = 1, column=0, sticky=NSEW, pady=5, padx=5)

img_4 = Image.open('images/quantidade.png')
img_4 = img_4.resize((40,40), Image.ANTIALIAS)
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(left_frame, text='Quantidade', image=img_4, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', font=('Ivy 11 bold'), bg = color3, fg=color1)
b_4.grid(row = 1, column=1, sticky=NSEW, pady=5, padx=5)

img_5 = Image.open('images/velocidade.png')
img_5 = img_5.resize((40,40), Image.ANTIALIAS)
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(left_frame, text=' Velocidade', image=img_5, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', font=('Ivy 11 bold'), bg = color3, fg=color1)
b_5.grid(row = 1, column=2, sticky=NSEW, pady=5, padx=5)

img_6 = Image.open('images/temperatura.png')
img_6 = img_6.resize((40,40), Image.ANTIALIAS)
img_6 = ImageTk.PhotoImage(img_6)
b_6 = Button(left_frame, text='Temperatura', image=img_6, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', font=('Ivy 11 bold'), bg = color3, fg=color1)
b_6.grid(row = 2, column=0, sticky=NSEW, pady=5, padx=5)

img_7 = Image.open('images/energia.png')
img_7 = img_7.resize((40,40), Image.ANTIALIAS)
img_7 = ImageTk.PhotoImage(img_7)
b_7 = Button(left_frame, text='Energia', image=img_7, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', font=('Ivy 11 bold'), bg = color3, fg=color1)
b_7.grid(row = 2, column=1, sticky=NSEW, pady=5, padx=5)

img_8 = Image.open('images/pressao.png')
img_8 = img_8.resize((40,40), Image.ANTIALIAS)
img_8 = ImageTk.PhotoImage(img_8)
b_8 = Button(left_frame, text=' Pressão', image=img_8, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', font=('Ivy 11 bold'), bg = color3, fg=color1)
b_8.grid(row = 2, column=2, sticky=NSEW, pady=5, padx=5)

window.mainloop()
