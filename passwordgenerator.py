from tkinter import *
import random
alphbets = ["a","b","c","d","e","f","g","h","i","j","j","k","l","m","n"
       ,"o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D",
       "E","F","G", "H","I","J", "K", "L", "M","N", "O", "P",
       "Q", "R", "S" ,"T" ,"U" ,"V", "W" ,"X" ,"Y" ,"Z"]

no = ["1","2","3","4","5","6","7","8","9"]

special_c = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

def generate():
    
    a = int(alp_value.get())
    n = int(no_value.get())
    sn = int(spec_ch_value.get())
    print(a  , n , sn)
    password = ""
    for i in range(a):
        value = random.choice(alphbets)
        password = password + value

    for j in range(n):
        value2 = random.choice(no)
        password = password + value2  

    for k in range(sn):
        value3 = random.choice(special_c)
        password = password + value3

    root1 = Tk()
    root1.geometry('150x50')
    passwords = Label(root1 , text=password ,font="bold 14 italic" , bg="white" , fg="purple")
    passwords.pack(fill=X)
    root1.mainloop()

root = Tk()
root.title(" PASSWORD GENERATOR ")
root.geometry("550x200")


t1 = Label(root , text="Enter how many alphabets u want =>" , font = "lucida 10 bold" )
t2 = Label(root , text="Enter how many numbers u want =>" , font = "lucida 10 bold")
t3 = Label(root , text="Enter how many special character's u want =>" ,font = "lucida 10 bold")

t1.grid(row = 1 , column = 1)
t2.grid(row = 3 , column = 1)
t3.grid(row = 5 , column = 1)

alp_value = StringVar()
no_value = StringVar()
spec_ch_value = StringVar()

m1 = Entry(root , textvariable=alp_value , font="bold 15" , bg = "red" , fg = "pink")
m2 = Entry(root , textvariable=no_value , font="bold 15" , bg = "red" , fg = "pink")
m3 = Entry(root , textvariable=spec_ch_value , font="bold 15" , bg = "red" , fg = "pink")

m1.grid(pady=10 , row= 1 , column= 3)
m2.grid(pady=10 ,row= 3, column= 3)
m3.grid(pady=10 , row= 5 , column= 3)

b1 = Button(root , text="Generate Password" ,command=generate ,font='bold 12' , bg= 'black' , fg='purple')
b1.grid(row=7 , column=3)

root.mainloop()