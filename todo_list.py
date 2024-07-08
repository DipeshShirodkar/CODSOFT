from tkinter import *
task_to_do = ["sleep" , "coding"]

def add():
    
    def task():       
        added_task = task_entry.get()
        task_to_do.append(added_task)
        r23 = Toplevel()
        r23.title()
        r23.geometry("250x150")
        add_value = Label(r23 , text=task_to_do ,font="Helvetica 10" , bg="grey" , fg="red" 
                       )
        add_value.pack(pady= 5)
        r23.mainloop()

    r1 = Tk()
    r1.geometry("250x150")
    r1.title("add")

    #jab koi string leni ho  to sidha esa likho
    task_entry = Entry(r1 , bg="grey" , fg="pink" , font="Helvetica 12")
    task_entry.grid(row=2 , column = 2 , pady=5) 

    add_button = Button(r1 , text="add" ,command=task , bg="red" , fg="pink" , font="Helvetica 12" )
    add_button.grid(row=4 , column=2)
    r1.mainloop()

def remove():
    def removetask():
       remove_value = task_entry.get()
       task_to_do.remove(remove_value)
       r22 = Toplevel()
       r22.title()
       r22.geometry("250x150")
       remove_value = Label(r22 , text=task_to_do ,font="Helvetica 10" , bg="grey" , fg="red" 
                       )
       remove_value.pack(pady=5)
       r22.mainloop()

    r3 = Tk()
    r3.title()
    r3.geometry("250x150")

    task_entry = Entry(r3 , bg="grey" , fg="pink" , font="Helvetica 12")
    task_entry.grid(row=2 , column = 2 , pady=5) 

    remove_button = Button(r3 , text="remove" ,command=removetask , bg="red" , fg="pink" , font="Helvetica 12" )
    remove_button.grid(row=4 , column=2)

    r3.mainloop()

def view():
    print(task_to_do)
    r2 = Toplevel()
    r2.title()
    r2.geometry("250x150")
    view_value = Label(r2 , text=task_to_do ,font="Helvetica 10" , bg="grey" , fg="red" 
                       )
    view_value.pack(pady=5)
    r2.mainloop()

root = Tk()
root.title("To-Do List")
root.geometry("250x150")

l1 = Label(root , text="To-Do List :- " , font="Helvetica 12 bold" , fg="purple")
l1.grid(row=1 , column=1 , padx=7 , pady=5)

b1 = Button(root , text= "ADD", font="Helvetica 10" , bg="grey" , fg="red"
            ,command=add)
b2 = Button(root , text= "REMOVE", font="Helvetica 10" , bg="grey" , fg="red"
            ,command=remove)
b3 = Button(root , text= "VIEW", font="Helvetica 10" , bg="grey" , fg="red"
            ,command=view)

b1.grid(row=3 , column=2 , pady=4)
b2.grid(row=5 , column=2 , pady=4)
b3.grid(row=7 , column=2 , pady=4)
root.mainloop()