#Let's improve the iterables, clean up global variables, and improve the GUI
import tkinter as tk
from functools import partial

#all functions and objects (backend) must be before tkinter window instantiation

t_list = []
d_list = []

def destroy(frame, lst):#should destroy widgets and wipe out list
    for widget in frame.winfo_children():
        widget.destroy()
    lst.clear()
    space = tk.Label(frame)#sets todo_frame//done_frame grid to just one row space
    space.grid(row=0, column=0, sticky=tk.W+tk.E)

def t_iter():#iterate todo list
    enum = enumerate(t_list)
    if not t_list:
        space = tk.Label(todo_frame)#sets todo_frame grid to just one row space
        space.grid(row=0, column=0, sticky=tk.W+tk.E)
    for n in enum:
        index = n[0]
        text = n[1]
        check = tk.Button(todo_frame, text="Check", font=("Ariel", 20), bg="#39db49", bd=5, padx=5, pady=5)
        check.config(command=partial(check_done, index))
        check.grid(row=index, column=0, sticky=tk.W+tk.E)
        task = tk.Label(todo_frame, text=text, font=("Ariel", 30), padx=5, pady=5)
        task.grid(row=index, column=1, sticky=tk.W+tk.E)
        delete = tk.Button(todo_frame, text="Delete", font=("Ariel", 20), bg="#fc4444", bd=5, padx=5, pady=5)
        delete.config(command=partial(dlt, todo_frame, t_list, index))
        delete.grid(row=index, column=2 ,sticky=tk.W+tk.E)

def d_iter():#iterate done list
    enum = enumerate(d_list)
    if not d_list:
        space = tk.Label(done_frame)#sets done_frame grid to just one row space
        space.grid(row=0, column=0, sticky=tk.W+tk.E)
    for n in enum:
        index = n[0]
        text = n[1]
        task_done = tk.Label(done_frame, text=text, font=("Ariel", 30), padx=5, pady=5)
        task_done.grid(row=index, column=0, sticky=tk.W+tk.E)
        delete = tk.Button(done_frame, text="Delete", font=("Ariel", 20), bg="#fc4444", bd=5, padx=5, pady=5)
        delete.config(command=partial(dlt, done_frame, d_list, index))
        delete.grid(row=index, column=1, sticky=tk.W+tk.E)

def add(t):#iterate a todo row every time add todo is clicked // handles input validation and iteration
    if t.get() == "":#if user did not enter anything, return (exit function)
        return
    t_list.append(t.get())
    t_iter()

def check_done(ind):#check off a task and append it to done list
    for widget in todo_frame.winfo_children():
        widget.destroy()
    d_list.append(t_list[ind])#append the row to done list before deleting it
    t_list.pop(ind)#should pop corresponding text from row
    t_iter()
    d_iter()     

def dlt(frame, lst, ind):#deletes a single todo row or done row
    for widget in frame.winfo_children():
        widget.destroy()
    lst.pop(ind)
    if lst is t_list:#using 'is' operator tests if two variables refer to the same object
        t_iter()
    else:
        d_iter()



root = tk.Tk()#tkinter widgets (GUI) connects to backend (functions and list objects)


root.geometry("1000x700")
root.title("To-Do")

#Everything in a master frame

master_frame = tk.Frame(root) #4 master rows: 0. todo, 1. todo sub grid, 2. add a todo, 3. done, 4. done subgrid

master_frame.columnconfigure(0, weight=1) #maximum of 2 columns within whole master frame
master_frame.columnconfigure(1, weight=1)

todo_frame = tk.Frame(master_frame) #row 1 of master frame

todo_frame.columnconfigure(0, weight=1) #maximum of 3 columns inside todo sub frame
todo_frame.columnconfigure(1, weight=5)
todo_frame.columnconfigure(2, weight=1)

done_frame = tk.Frame(master_frame) #row 4 of master frame

done_frame.columnconfigure(0, weight=5) #maximum of 2 columns within done subframe
done_frame.columnconfigure(1, weight=1)

#todo label and delete button /// row 0 of master_frame
todo_label = tk.Label(master_frame, text="To-Do", font=("Ariel", 40), bg="#ffbb6e", padx=10)
todo_label.grid(row=0, column=0, sticky=tk.W+tk.E)

todo_clear = tk.Button(master_frame, text="Clear", font=("Ariel", 30), bg="#ffbb6e", bd=7, padx=10)
todo_clear.config(command=partial(destroy, todo_frame, t_list))
todo_clear.grid(row=0, column=1, sticky=tk.W+tk.E)

#add to do button iterates a new to-do row under todo_frame under master_frame // row 2 of master frame
text = tk.Entry(master_frame, text="", font=("Ariel", 30)) #user text entry
text.grid(row=2, column=1, sticky=tk.W+tk.E)

add_todo = tk.Button(master_frame, text="Add +", font=("Ariel", 30), bg="#4290f5", bd=7, padx=10)
add_todo.config(command=partial(add, text)) #submits text entry to add function
add_todo.grid(row=2, column=0, sticky=tk.W+tk.E)

#done label and delete button /// row 3 of master frame
done_label = tk.Label(master_frame, text="Done", font=("Ariel", 40), bg="#ffbb6e", padx=10)
done_label.grid(row=3, column=0, sticky=tk.W+tk.E)

done_clear = tk.Button(master_frame, text="Clear", font=("Ariel", 30), bg="#ffbb6e", bd=7, padx=10)
done_clear.config(command=partial(destroy, done_frame, d_list))
done_clear.grid(row=3, column=1, sticky=tk.W+tk.E)


todo_frame.grid(row=1, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)#row 1 of master frame

done_frame.grid(row=4, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)#row 4 of master frame

master_frame.pack(fill='x')


root.mainloop() 