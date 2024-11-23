import tkinter as tk
from functools import partial

root = tk.Tk()

root.geometry("700x700")
root.title("To-Do")

#let's just put everything below in a master frame

master_frame = tk.Frame(root) #we will have 5 master rows, 1)todo, 2)todo sub grid, 3)add a todo, 4)done, 5)done subgrid

master_frame.columnconfigure(0, weight=1) #maximum of 2 columns within whole master frame
master_frame.columnconfigure(1, weight=1)

#todo label and delete button
todo_label = tk.Label(master_frame, text="To-Do", font=("Times New Roman", 30))
todo_label.grid(row=0, column=0, sticky=tk.W+tk.E)

todo_delete = tk.Button(master_frame, text="Delete", font=("Ariel", 30))
todo_delete.grid(row=0, column=1, sticky=tk.W+tk.E)

#todo sub frame
todo_frame = tk.Frame(master_frame)

master_frame.columnconfigure(0, weight=1) #maximum of 3 columns within todo sub frame
master_frame.columnconfigure(1, weight=1)
master_frame.columnconfigure(2, weight=1)

#allow text entry and iterate a todo row every time add todo is clicked:
    

#add check btn, text and delete button in a row (under To-Do subframe)
check = tk.Button(todo_frame, text="Check", font=("Ariel", 20))
check.grid(row=0, column=0, sticky=tk.W+tk.E)
task = tk.Label(todo_frame, text="TBD", font=("Ariel", 20))
task.grid(row=0, column=1, sticky=tk.W+tk.E)
d = tk.Button(todo_frame, text="Delete", font=("Ariel", 20)) #d means delete
d.grid(row=0, column=2, sticky=tk.W+tk.E)

todo_frame.grid(row=1, column=0, pady=5)

##################################################################

#"add to do button" which iterates a new to-do row to the todo_frame (falls under master frame), after user enters text
text = tk.Entry(master_frame, text="blablabla", font=("Ariel", 20))
text.grid(row=3, column=1, sticky=tk.W+tk.E)
text.get()
add_todo = tk.Button(master_frame, text="Add a To-Do:", font=("Ariel", 30))
add_todo.grid(row=3, column=0, sticky=tk.W+tk.E)

##################################################################

#done label and delete button
done_label = tk.Label(master_frame, text="Done", font=("Times New Roman", 30))
done_label.grid(row=4, column=0, sticky=tk.W+tk.E)

done_delete = tk.Button(master_frame, text="Delete", font=("Ariel", 30))
done_delete.grid(row=4, column=1, sticky=tk.W+tk.E)

#done subframe
done_frame = tk.Frame(master_frame)

done_frame.columnconfigure(0, weight=1) #maximum of 2 columns within done subframe
done_frame.columnconfigure(1, weight=1)

#text and delete button in a row (under Done subframe)

done_frame.grid(row=5, column=0, pady=5)


master_frame.pack(fill='x')

root.mainloop() 