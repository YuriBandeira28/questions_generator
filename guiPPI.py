import tkinter as tk
from tkinter import Canvas
import gpt

win = tk.Tk()
win.configure(bg='white')
win.geometry("640x480")


def send(e):
    msg = str(box.get())
    if msg != '':
        box.delete(0, len(str(box.get())))
        #print(msg)
        mesageLabel = gpt.chat(msg)
    else:
        print('por favor, insira algo na caixa de texto')
    #l1 = tk.Label(win, text = main.chat(msg))
    #l1.grid(row = 2, column= 3)
    #faça 10 questoes sobre banco de dados numerados de 1 a 10
    j= 100
    for i in mesageLabel:

        tk.Checkbutton(win, text=i).place(x = 100, y=j)
        j+=30


box = tk.Entry(win)
box.grid(row = 0, column=0)

b1 = tk.Button(win, text="enviar", command=lambda:send(e=None))
win.bind('<Return>', send)
b1.grid(row=1, column=1)


#msg = tk.

win.mainloop()