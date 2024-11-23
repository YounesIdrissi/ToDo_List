#Let's clean up the code
import tkinter as tk
from functools import partial

#All functions and variables must be at the top

t_list = []
d_list = []

def destroy(frame, lst):#should destroy widgets and wipe out t_list // could we just have a destroy method in a class???
    for widget in frame.winfo_children():
        widget.destroy()
    lst.clear()
    space = tk.Label(frame, text="", font=("Ariel", 20))#sets todo_frame grid to just one row space
    space.grid(row=0, column=0, sticky=tk.W+tk.E)

def t_iter():
    for n in t_list:#iterate todo list
        index = t_list.index(n)
        check = tk.Button(todo_frame, text="Check", font=("Ariel", 20))
        check.config(command=partial(check_done, index))
        check.grid(row=index, column=0, sticky=tk.W+tk.E)
        task = tk.Label(todo_frame, text=n, font=("Ariel", 20))
        task.grid(row=index, column=1, sticky=tk.W+tk.E)
        delete = tk.Button(todo_frame, text="Delete", font=("Ariel", 20)) #d means delete
        delete.config(command=partial(dlt, todo_frame, t_list, index))
        delete.grid(row=index, column=2 ,sticky=tk.W+tk.E)
        print(f"t_list: {t_list}")

def d_iter():
    for n in d_list:#iterate done list
        index = d_list.index(n)
        task_done = tk.Label(done_frame, text=n, font=("Ariel", 20))
        task_done.grid(row=index, column=1, sticky=tk.W+tk.E)
        delete = tk.Button(done_frame, text="Delete", font=("Ariel", 20)) #d means delete
        delete.config(command=partial(dlt, done_frame, d_list, index))
        delete.grid(row=index, column=2, sticky=tk.W+tk.E)

def add(t):#iterate a todo row every time add todo is clicked:
    global t_list
    if t.get() == "":#if user did not enter anything, return (exit function)
        return
    if t.get() not in t_list:
        t_list.append(t.get())
        t_iter()

def check_done(ind):#check off a task and append it to done list
    global t_list
    global d_list
    for widget in todo_frame.winfo_children():
        widget.destroy()
    #append the row to done list before deleting it
    if t_list[ind] not in d_list:
        d_list.append(t_list[ind])
    print(f"d_list: {d_list}")
    t_list.pop(ind)#should pop corresponding text from row
    t_iter()
    d_iter()     

def dlt(frame, lst, ind):#deletes a single todo task/row
    for widget in frame.winfo_children():
        widget.destroy()
    lst.pop(ind)
    if lst == t_list:
        t_iter()
    else:
        d_iter()



root = tk.Tk()


root.geometry("700x700")
root.title("To-Do")

#let's just put everything in a master frame

master_frame = tk.Frame(root) #we will have 4 master rows, 0)todo, 1)todo sub grid, 2)add a todo, 3)done, 4)done subgrid

master_frame.columnconfigure(0, weight=1) #maximum of 2 columns within whole master frame
master_frame.columnconfigure(1, weight=1)

todo_frame = tk.Frame(master_frame) #part of master_frame ***

todo_frame.columnconfigure(0, weight=1) #maximum of 3 columns inside todo sub frame
todo_frame.columnconfigure(1, weight=1)
todo_frame.columnconfigure(2, weight=1)

done_frame = tk.Frame(master_frame)

done_frame.columnconfigure(0, weight=1) #maximum of 2 columns within done subframe
done_frame.columnconfigure(1, weight=1)

#todo label and delete button /// row 0 of master_frame
todo_label = tk.Label(master_frame, text="To-Do", font=("Times New Roman", 30))
todo_label.grid(row=0, column=0, sticky=tk.W+tk.E)

todo_clear = tk.Button(master_frame, text="Clear", font=("Ariel", 30))
todo_clear.config(command=partial(destroy, todo_frame, t_list))
todo_clear.grid(row=0, column=1, sticky=tk.W+tk.E)

#"add to do button" which iterates a new to-do row to the todo_frame under master_frame (this is the INITIATOR)
text = tk.Entry(master_frame, text="", font=("Ariel", 20)) #this is row 2 of master_frame
text.grid(row=3, column=1, sticky=tk.W+tk.E)
add_todo = tk.Button(master_frame, text="Add +", font=("Ariel", 30))
add_todo.config(command=partial(add, text)) #submits text entry to return_func
add_todo.grid(row=3, column=0, sticky=tk.W+tk.E)

#done label and delete button /// row 3 of master_frame
done_label = tk.Label(master_frame, text="Done", font=("Times New Roman", 30))
done_label.grid(row=4, column=0, sticky=tk.W+tk.E)

done_clear = tk.Button(master_frame, text="Clear", font=("Ariel", 30))
done_clear.config(command=partial(destroy, done_frame, d_list))
done_clear.grid(row=4, column=1, sticky=tk.W+tk.E)


todo_frame.grid(row=1, column=0, pady=5)

done_frame.grid(row=5, column=0, pady=5)

master_frame.pack(fill='x')


root.mainloop() 