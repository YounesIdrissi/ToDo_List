import tkinter as tk
#from functools import partial

root = tk.Tk()

root.geometry("700x700")
root.title("To-Do")

#let's just put everything below in a master frame

master_frame = tk.Frame(root) #we will have 5 master rows, 1)todo, 2)todo sub grid, 3)add a todo, 4)done, 5)done subgrid

master_frame.columnconfigure(0, weight=1) #maximum of 2 columns within whole master frame
master_frame.columnconfigure(1, weight=1)

t_list = []
d_list = []

def destroyt():#should destroy widgets and wipe out t_list // could we just have a destroy method in a class???
    global t_list
    for widget in todo_frame.winfo_children():
        widget.destroy()
    t_list.clear()
    tspace = tk.Label(todo_frame, text="", font=("Ariel", 20))#sets todo_frame grid to just one row space
    tspace.grid(row=0, column=0, sticky=tk.W+tk.E)

def destroyd():#should destroy widgets and wipe out t_list
    global d_list
    for widget in done_frame.winfo_children():
        widget.destroy()
    d_list.clear()
    dspace = tk.Label(done_frame, text="", font=("Ariel", 20))#sets done_frame grid to just one row space
    dspace.grid(row=0, column=0, sticky=tk.W+tk.E)

def return_func3(ind):
    def tdelete():#deletes a single todo task/row
        global t_list
        for widget in todo_frame.winfo_children():
            widget.destroy()
        t_list.pop(ind)
        for n in t_list:#then reiterate new todo list
            index = t_list.index(n)
            check = tk.Button(todo_frame, text="Check", font=("Ariel", 20))
            check.config(command=return_func2(index))
            check.grid(row=index, column=0, sticky=tk.W+tk.E)
            task = tk.Label(todo_frame, text=n, font=("Ariel", 20))
            task.grid(row=index, column=1, sticky=tk.W+tk.E)
            td = tk.Button(todo_frame, text="Delete", font=("Ariel", 20)) #d means delete
            td.config(command=return_func3(index))
            td.grid(row=index, column=2 ,sticky=tk.W+tk.E)
            print(f"t_list: {t_list}")
    return tdelete

def return_func4(ind):
    def ddelete():#deletes a single done task/row
        global d_list
        for widget in done_frame.winfo_children():
            widget.destroy()
        d_list.pop(ind)
        for n in d_list:#iterate done list
            index = d_list.index(n)
            task_done = tk.Label(done_frame, text=n, font=("Ariel", 20))
            task_done.grid(row=index, column=1, sticky=tk.W+tk.E)
            dd = tk.Button(done_frame, text="Delete", font=("Ariel", 20)) #d means delete
            dd.config(command=return_func4(index))
            dd.grid(row=index, column=2, sticky=tk.W+tk.E)
            print(f"d_list: {d_list}")
    return ddelete


        

#todo label and delete button /// row 0 of master_frame
todo_label = tk.Label(master_frame, text="To-Do", font=("Times New Roman", 30))
todo_label.grid(row=0, column=0, sticky=tk.W+tk.E)

todo_clear = tk.Button(master_frame, text="Clear", font=("Ariel", 30))
todo_clear.config(command=destroyt)
todo_clear.grid(row=0, column=1, sticky=tk.W+tk.E)




#todo sub frame /// row 1 of master_frame
todo_frame = tk.Frame(master_frame) #part of master_frame ***

todo_frame.columnconfigure(0, weight=1) #maximum of 3 columns inside todo sub frame
todo_frame.columnconfigure(1, weight=1)
todo_frame.columnconfigure(2, weight=1)

#allow text entry and iterate a todo row every time add todo is clicked:



def return_func2(ind):
    def check_done():#check off a task and append it to done list
        global t_list
        global d_list
        for widget in todo_frame.winfo_children():
            widget.destroy()
        #append the row to done list before deleting it
        if t_list[ind] not in d_list:
            d_list.append(t_list[ind])
        print(f"d_list: {d_list}")
        t_list.pop(ind)#should pop corresponding text from row

        for n in t_list:#then reiterate new todo list
            index = t_list.index(n)
            check = tk.Button(todo_frame, text="Check", font=("Ariel", 20))
            check.config(command=return_func2(index))
            check.grid(row=index, column=0, sticky=tk.W+tk.E)
            task = tk.Label(todo_frame, text=n, font=("Ariel", 20))
            task.grid(row=index, column=1, sticky=tk.W+tk.E)
            td = tk.Button(todo_frame, text="Delete", font=("Ariel", 20)) #d means delete
            td.config(command=return_func3(index))
            td.grid(row=index, column=2 ,sticky=tk.W+tk.E)
            print(f"t_list: {t_list}")
        
        for n in d_list:#iterate done list
            index = d_list.index(n)
            task_done = tk.Label(done_frame, text=n, font=("Ariel", 20))
            task_done.grid(row=index, column=1, sticky=tk.W+tk.E)
            dd = tk.Button(done_frame, text="Delete", font=("Ariel", 20)) #d means delete
            dd.config(command=return_func4(index))
            dd.grid(row=index, column=2, sticky=tk.W+tk.E)     

    return check_done

def return_func(t): #nested function for returning a value properly/not immediately executing and being stuck
    global t_list
    def add_row():
        if t.get() == "":#if user did not enter anything, return (exit function)
            return
        if t.get() not in t_list:
            t_list.append(t.get())
            for n in t_list:
                index = t_list.index(n)
                check = tk.Button(todo_frame, text="Check", font=("Ariel", 20))
                check.config(command=return_func2(index))
                check.grid(row=index, column=0, sticky=tk.W+tk.E)
                task = tk.Label(todo_frame, text=n, font=("Ariel", 20))
                task.grid(row=index, column=1, sticky=tk.W+tk.E)
                td = tk.Button(todo_frame, text="Delete", font=("Ariel", 20)) #d means delete
                td.config(command=return_func3(index))
                td.grid(row=index, column=2 ,sticky=tk.W+tk.E)
                print(f"t_list: {t_list}")

    return add_row

todo_frame.grid(row=1, column=0, pady=5) #this should NOT be incremented, it is part of master_frame *** // end of row 1
##################################################################




#"add to do button" which iterates a new to-do row to the todo_frame (falls under master frame), after user enters text
text = tk.Entry(master_frame, text="", font=("Ariel", 20)) #this is row 2 of master_frame
text.grid(row=3, column=1, sticky=tk.W+tk.E)
add_todo = tk.Button(master_frame, text="Add +", font=("Ariel", 30))
add_todo.config(command=return_func(text)) #submits text entry to return_func
add_todo.grid(row=3, column=0, sticky=tk.W+tk.E)




##################################################################




#done label and delete button /// row 3 of master_frame
done_label = tk.Label(master_frame, text="Done", font=("Times New Roman", 30))
done_label.grid(row=4, column=0, sticky=tk.W+tk.E)

done_clear = tk.Button(master_frame, text="Clear", font=("Ariel", 30))
done_clear.config(command=destroyd)
done_clear.grid(row=4, column=1, sticky=tk.W+tk.E)




#done subframe /// row 4 of master_frame; final row
done_frame = tk.Frame(master_frame)

done_frame.columnconfigure(0, weight=1) #maximum of 2 columns within done subframe
done_frame.columnconfigure(1, weight=1)

#text and delete button in a row (under Done subframe)

done_frame.grid(row=5, column=0, pady=5)


master_frame.pack(fill='x')

root.mainloop() 