from tkinter import *

def showing(event):
    global Svalue
# VWRY IMPORTANT YE TEXT VALI VALUE KO LETA H    
    text = event.widget.cget("text")

    if text == "= ":
         if Svalue.get().isdigit():
             values = int(Svalue.get())
         else:
             values = eval(screen.get())

         Svalue.set(values)
         screen.update()


    elif text =="C ":
      Svalue.set("")
      screen.update()
    
    else:
     Svalue.set(Svalue.get() + text)
     screen.update()    
    

root = Tk()
root.title("CALCULTOR")
root.geometry("350x440")
f7 = Frame(root , bg = "red")

Svalue = StringVar()
Svalue.set("")

screen = Entry(root , textvariable=Svalue , font="Lucida 40 bold" )
screen.grid(row = 0 , column = 0)
f7.grid()

f1 = Frame(root , bg="grey")
b1 = Button(text="9" , font="lucida 40 bold")
b1.grid(row = 2 , column=1 , pady=15)
b1.bind('<Button-1>' , showing)
b2 = Button(text="8" , font="lucida 40 bold")
b2.grid(row = 2 , column=2 , pady=15)
b2.bind('<Button-1>' , showing)
b3 = Button(text="7" , font="lucida 40 bold")
b3.grid(row = 2 , column=3 , pady=15)
b3.bind('<Button-1>' , showing)
b4 = Button(text="= " , font="lucida 40 bold")
b4.grid(row=2 , column=4  , pady= 15)
b4.bind('<Button-1>' , showing)
f1.grid()

f1 = Frame(root , bg="grey")
b1 = Button(text="6" , font="lucida 40 bold")
b1.grid(row = 3 , column=1 , pady=15)
b1.bind('<Button-1>' , showing)
b2 = Button(text="5" , font="lucida 40 bold")
b2.grid(row = 3 , column=2 , pady=15)
b2.bind('<Button-1>' , showing)
b3 = Button(text="4" , font="lucida 40 bold")
b3.grid(row = 3 , column=3 , pady=15)
b3.bind('<Button-1>' , showing)
b4 = Button(text="C " , font="lucida 40 bold")
b4.grid(row = 3 , column=4 , pady=15)
b4.bind('<Button-1>' , showing)
f1.grid()

f1 = Frame(root , bg="grey")
b1 = Button(text="3" , font="lucida 40 bold")
b1.grid(row = 4 , column=1 , pady=15)
b1.bind('<Button-1>' , showing)
b2 = Button(text="2" , font="lucida 40 bold")
b2.grid(row = 4 , column=2 , pady=15)
b2.bind('<Button-1>' , showing)
b3 = Button(text="1" , font="lucida 40 bold")
b3.grid(row = 4 , column=3 , pady=15)
b3.bind('<Button-1>' , showing)
b3 = Button(text="%" , font="lucida 40 bold")
b3.grid(row = 4 , column= 4, pady=15)
b3.bind('<Button-1>' , showing)
f1.grid()

f1 = Frame(root , bg="grey")
b1 = Button(text=" + " , font="lucida 40 bold")
b1.grid(row = 5 , column=1 , pady=15)
b1.bind('<Button-1>' , showing)
b2 = Button(text=" - " , font="lucida 40 bold")
b2.grid(row = 5 , column=2 , pady=15)
b2.bind('<Button-1>' , showing)
b3 = Button(text=" * " , font="lucida 40 bold")
b3.grid(row = 5 , column=3 , pady=15)
b3.bind('<Button-1>' , showing)
b3 = Button(text=" / " , font="lucida 40 bold")
b3.grid(row = 5 , column= 4, pady=15)
b3.bind('<Button-1>' , showing)
f1.grid()


root.mainloop()