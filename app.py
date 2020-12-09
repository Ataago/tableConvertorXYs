import tkinter as tk
from tkinter import filedialog
from main import main as convertor

root=tk.Tk()
root.geometry('400x400')

a = tk.Label(root, text = "").grid(row = 0,column = 0)
file_lab = tk.Label(root, text = "File Path:").grid(row = 2,column = 1)
file_ent = tk.Entry(root,font=50)
file_ent.grid(row=2,column=2)


def browsefunc():
    filename = filedialog.askopenfilename()
    file_ent.insert(tk.END, filename) # add this

    return filename

b1=tk.Button(root,text="Browse",font=40,command=browsefunc)
b1.grid(row=2,column=4)

X_lab = tk.Label(root, text="X Column:").grid(row=3, column=1)
X_ent = tk.Entry(root, font=50)
X_ent.grid(row=3,column=2)

Y_lab = tk.Label(root, text="Y Column:").grid(row=4, column=1)
Y_ent = tk.Entry(root, font=50)
Y_ent.grid(row=4,column=2)

V_lab = tk.Label(root, text="Value Column:").grid(row=5, column=1)
V_ent = tk.Entry(root, font=50)
V_ent.grid(row=5,column=2)

sf_lab = tk.Label(root, text="Save sheet as:").grid(row=6, column=1)
sf_ent = tk.Entry(root, font=50)
sf_ent.grid(row=6,column=2)

variable = tk.StringVar(root)
variable.set("convertor_1") # default value
select_convertor = tk.Label(root, text="Select Convertor:").grid(row=7, column=1)
convertor_options = tk.OptionMenu(root, variable, "convertor_1", "convertor_2").grid(row=7, column=2)

def clicked():
    convertor(
        file_path=file_ent.get(),
        X=X_ent.get(),
        Y=Y_ent.get(),
        V=V_ent.get(),
        convertor=variable.get(),
        saveAs=sf_ent.get()
    )

btn = tk.Button(root ,text="Submit", command=clicked).grid(row=10,column=2)


root.mainloop()
