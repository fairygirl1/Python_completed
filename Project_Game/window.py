

from tkinter import *

#меню
def menu():
    mainmenu = Menu(tk)
    tk.config(menu=mainmenu)

    mainmenu.add_command(label='Баланс')
    mainmenu.add_command(label='Завершить')

    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Правила игры")
    filemenu.add_command(label="Мемы про Питер")

    mainmenu.add_cascade(label="Меню",
                     menu=filemenu)



def close(): #закрываем старое окно
    tk.destroy()

def click(): #открытие нового окна
    menu()
    window = Tk()
    window.title("First Stage")
    window.geometry('700x550+600+300')

def next():
    click()
    # close()


#вопрос + кнопка 1
def que0():
    def start():
        lab['text'] = "От твоего выбора зависит дальнейшее развитие событий!"

    Label(text = ' ', bd = 40).pack()
    Label(text='Санкт-Петербург', font="Arial 22").pack()
    Label(text='Московский вокзал', font='Arial 18', bd=15).pack()
    Button(text="Начать", command=start, font="Roboto 20", bg = '#87cefa').pack()
    Button(text = 'Далее', command = next, font = 'Roboto 20'). pack()
    lab = Label(width=50, height=10, font = 'Roboto 15')
    lab.pack()



#окно приветствия


tk = Tk()
tk.title('Game')
tk.geometry('700x500+600+300')
menu()
que0()

tk.mainloop()