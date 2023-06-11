from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import font
import random


#Данные переменных для проекта
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
chars2 = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
chars1 = '1234567890'
number = int()


#Основной виджет окна
window = Tk()
window["bg"] = "pink"
window.title("Генератор твоих паролей")
window.geometry('161x117')


#Создание дополнительного окна если нажать на кнопку генерации любых паролей
def clicked():
    window1 = Tk()
    window1["bg"] = "pink"
    window1.title("Твои любые пароли, пупсик")
    window1.geometry("330x120")

    #Оформление сгенерированных трёх паролей
    lbl1 = Label(window1, text=passw(), font=font2, foreground="mediumpurple", background="midnightblue")
    lbl2 = Label(window1, text=passw(), font=font2, foreground="mediumpurple", background="midnightblue")
    lbl3 = Label(window1, text=passw(), font=font2, foreground="mediumpurple", background="midnightblue")

    # Создание переменной, хранящей текст оформлений 3 паролей
    text_lbl1 = lbl1['text']
    text_lbl2 = lbl2['text']
    text_lbl3 = lbl2['text']


    #Функция сохранения в файл
    def clicked1():
        filepath = fd.asksaveasfilename(defaultextension=".txt")
        if filepath != "":
            textlabel1 = text_lbl1.get("1.0", END)
            textlabel2 = text_lbl2.get("1.0", END)
            textlabel3 = text_lbl3.get("1.0", END)
            with open(filepath, "w") as file:
                file.write(textlabel1)
                file.write(textlabel2)
                file.write(textlabel3)

    #Кнопка сохранения паролей
    btn2 = Button(window1, text="Сохранить пароли\nв файл", command=clicked1, font=font2, foreground="midnightblue", background="mediumpurple")

    #Разметка табла и кнопки
    lbl1.pack(anchor="nw", fill= 'x')
    lbl2.pack(anchor="w", fill= 'x')
    lbl3.pack(anchor="sw", fill= 'x')
    btn2.pack(anchor='s', fill= 'x')

    window1.mainloop()

#Создание дополнительного окна если нажать на кнопку генерации циферок
def clicked_1():
    window2 = Tk()
    window2["bg"] = "pink"
    window2.title("Твои циферки, пупсик")
    window2.geometry("330x120")


    #Оформление сгенерированных трёх паролей
    lbl1 = Label(window2, text=passw1(), font=font2, foreground="pink", background="#DB7093")
    lbl2 = Label(window2, text=passw1(), font=font2, foreground="pink", background="#DB7093")
    lbl3 = Label(window2, text=passw1(), font=font2, foreground="pink", background="#DB7093")

    # Создание переменной, хранящей текст оформлений 3 паролей
    text_lbl1 = lbl1['text']
    text_lbl2 = lbl2['text']
    text_lbl3 = lbl2['text']

    # Функция сохранения в файл
    def clicked1():
        filepath = fd.asksaveasfilename(defaultextension=".txt")
        if filepath != "":
            textlabel1 = text_lbl1.get("1.0", END)
            textlabel2 = text_lbl2.get("1.0", END)
            textlabel3 = text_lbl3.get("1.0", END)
            with open(filepath, "w") as file:
                file.write(textlabel1)
                file.write(textlabel2)
                file.write(textlabel3)



    # Кнопка сохранения паролей
    btn2 = Button(window2, text="Сохранить пароли\nв файл", command=clicked1, font=font2, foreground="#DB7093", background="pink")

    #Разметка табла и кнопки
    lbl1.pack(anchor="nw", fill= 'x')
    lbl2.pack(anchor="w", fill= 'x')
    lbl3.pack(anchor="sw", fill= 'x')
    btn2.pack(anchor='s', fill= 'x')

    window2.mainloop()

#Создание дополнительного окна если нажать на кнопку генерации паролей без спец символов
def clicked_2():
    window3 = Tk()
    window3["bg"] = "pink"
    window3.title("Пароли без спец. символов, пупсик")
    window3.geometry("330x120")


    #Оформление сгенерированных трёх паролей
    lbl1 = Label(window3, text=passw2(), font=font2, foreground="#ADD8E6", background="steelblue")
    lbl2 = Label(window3, text=passw2(), font=font2, foreground="#ADD8E6", background="steelblue")
    lbl3 = Label(window3, text=passw2(), font=font2, foreground="#ADD8E6", background="steelblue")

    # Создание переменной, хранящей текст оформлений 3 паролей
    text_lbl1 = lbl1['text']
    text_lbl2 = lbl2['text']
    text_lbl3 = lbl2['text']

    # Функция сохранения в файл
    def clicked1():
        filepath = fd.asksaveasfilename(defaultextension=".txt")
        if filepath != "":
            textlabel1 = text_lbl1.get("1.0", END)
            textlabel2 = text_lbl2.get("1.0", END)
            textlabel3 = text_lbl3.get("1.0", END)
            with open(filepath, "w") as file:
                file.write(textlabel1)
                file.write(textlabel2)
                file.write(textlabel3)

    # Кнопка сохранения паролей
    btn2 = Button(window3, text="Сохранить пароли\nв файл", command=clicked1, font=font2, foreground="steelblue",background="#ADD8E6")

    #Разметка табла и кнопки
    lbl1.pack(anchor="nw", fill= 'x')
    lbl2.pack(anchor="w", fill= 'x')
    lbl3.pack(anchor="sw", fill= 'x')
    btn2.pack(anchor='s', fill= 'x')

    window3.mainloop()


#Дополнительные виджеты
#Обозначение стиля для текста
font1 = font.Font(family = "Comic Sans MS", size = 8, weight = "bold", slant = "italic", underline = False, overstrike = False)
font2 = font.Font(family = "Comic Sans MS", size = 3, weight = "bold", slant = "italic", underline = False, overstrike = False)


#1 строчка
lbl = Label(window, text="Какая длина пароля?",font = font1, foreground="#F0FFF0", background="#DB7093")
lbl.grid(row=0, column=0)

txt1 = Entry(window, width=5, background="#F0FFF0")
txt1.grid(row=0, column=1,ipadx=1, ipady=1, padx=1, pady=1)


#2 строчка
chk1 = Button(window, text="     3 Набора циферок     ", command=clicked_1, font = font1, foreground="hotpink", background="pink")
chk1.grid(row=1, column=0, columnspan=10 , ipadx=1, ipady=1, padx=1, pady=1)


#3 строчка
chk2= Button(window, text="   3 Без '+-/*!&$#?=@<>  ", command=clicked_2, font = font1, foreground="steelblue", background="#ADD8E6")
chk2.grid(row=2, column=0, columnspan=10 , ipadx=1, ipady=1, padx=1, pady=1)

#4 строчка
btn1 = Button(window, text="      Любые 3 пароля      ", command=clicked, font = font1, foreground="midnightblue", background="mediumpurple")
btn1.grid(row=3, column=0, columnspan=10 , ipadx=1, ipady=1, padx=1, pady=1)


# Условия генерации варианта пароля без спец символов
def passw2(password=''):
    for n in range(int(txt1.get())):
           password += random.choice(chars2)
    return password

# Условия генерации варианта пароля только с циферками
def passw1(password=''):
    for n in range(int(txt1.get())):
           password += random.choice(chars1)
    return password

# Условия генерации любых три пароля
def passw(password=''):
    for n in range(int(txt1.get())):
           password += random.choice(chars)
    return password

window.mainloop()




