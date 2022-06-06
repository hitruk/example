
import tkinter as tk

h = 300
w = 600

win = tk.Tk()
win.geometry(f"{w}x{h}+100+200")
win.title('hello world')

tk.Label(win, text='Введите поисковое слово:').grid(row=1, column=0)
tk.Entry(win).grid(row=1, column=1)
tk.Button(win, text='Добавить').grid(row=1, column=2)
tk.Button(win, text='Удалить').grid(row=1, column=3)

win.mainloop()
