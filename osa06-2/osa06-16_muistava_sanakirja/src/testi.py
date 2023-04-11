import tkinter as tk
from tkinter import font

def show_answer():
    level = level_var.get()
    heikkoudet = heikkoudet_var.get()
    vahvuudet = vahvuudet_var.get()

    if level == "Aloittelija" and heikkoudet == "Huono" and vahvuudet == "Iha jees":
        answer_label.config(text="Sun pitäis treenata enemmän pohkeita")
    elif level == "Aloittelija" and heikkoudet == "Huono" and vahvuudet == "Jep":
        answer_label.config(text="Sun pitäis treenata enemmän pohkeita ja käsiä")
    # Add more elif statements for other possible combinations of inputs
    else:
        answer_label.config(text="Ei voida antaa vastausta")


root = tk.Tk()
root.title("Ristikiven Puntti")


# Create variables to store the selected values
level_var = tk.StringVar(root)
level_var.set("Aloittelija")
heikkoudet_var = tk.StringVar(root)
heikkoudet_var.set("Huono")
vahvuudet_var = tk.StringVar(root)
vahvuudet_var.set("Iha jees")

# Create the level label
level_label = tk.Label(root, text="Taso")

# 2cm = 78.74015748031496 pixels


# Create the dropdown menus
level_label.grid(row=0, column=0,sticky='W')
level_dropdown = tk.OptionMenu(root, level_var, "Aloittelija", "Keskiverto", "Pro")
level_dropdown.grid(row=1, column=0,sticky='W')
level_dropdown.config(width=10)

# Create the heikkoudet label
heikkoudet_label = tk.Label(root, text="Heikkoudet")
heikkoudet_label.grid(row=0, column=1,sticky='W')

# Create the dropdown menus
heikkoudet_dropdown = tk.OptionMenu(root, heikkoudet_var, "Huono", "Semi", "Ok", "Tyydyttävä", "Hyvä", "Paras")
heikkoudet_dropdown.grid(row=1, column=1,sticky='W')
heikkoudet_dropdown.config(width=10, font=("Arial", 9))

# Create the vahvuudet label
vahvuudet_label = tk.Label(root, text="Vahvuudet")
vahvuudet_label.grid(row=0, column=2,sticky='W')

# Create the dropdown menus
vahvuudet_dropdown = tk.OptionMenu(root, vahvuudet_var, "Iha jees", "Jep", "Näin", "Noin", "Täydellinen", "Bylly")
vahvuudet_dropdown.grid(row=1, column=2,sticky='W')
vahvuudet_dropdown.config(width=10)

# Create a button to show the selected answers
show_answer_button = tk.Button(root, text="Näytä vastaus", command=show_answer)
show_answer_button.grid(row=1, column=3, sticky='E')



# Create a label to display the answer
answer_label = tk.Label(root)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (800/1.2))
y = int((screen_height/2) - (600/2))
answer_label.place(x=x, y=y)





root.grid_columnconfigure(0, minsize=200, weight=1)
root.grid_columnconfigure(1, minsize=200, weight=1)
root.grid_columnconfigure(2, minsize=200, weight=1)






root.geometry("800x600+{}+{}".format(x, y))

root.mainloop()
