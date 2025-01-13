#Import the library needed
import tkinter as Tk

#Creating the object and setting the GUI's dimensions
root = Tk.Tk()
root.geometry = ("2000x2000")

#Simple widgets for design purposes
title = Tk.Label(root,  text = "Login Page", font = ("Arial", 20))
title.pack()

def get_input():
    text_to_be_accessed = textbox.get("1.0","end")
    text2_to_be_accessed = textbox_2.get("1.0","end")
    print(text_to_be_accessed)
    print(text2_to_be_accessed)
    if (text_to_be_accessed == "Jet the best\n") and (text2_to_be_accessed == "password\n"):
        label_4.config(text = "Thats Correct!")
    elif (text_to_be_accessed != "Jet the best\n") and (text2_to_be_accessed == "password\n"):
        label_4.config(text="Invalid Username!")
    elif (text2_to_be_accessed != "password\n") and (text_to_be_accessed == "Jet the best\n"):
        label_4.config(text="Invalid password!")
    else:
        label_4.config(text="Both username and password is wrong!")


label_2 = Tk.Label(root, text="Username:", font=("Arial", 12))
label_2.place(x=900, y=245)
textbox = Tk.Text(root, height=1, width=100, font = ("Arial", 12))
textbox.pack(padx=1000, pady=200)
textbox.bind()

label_3 = Tk.Label(root, text="Password:", font=("Arial", 12))
label_3.place(x=900, y=300)
textbox_2 = Tk.Text(root, height=1, width=62, font = ("Arial", 12))
textbox_2.place(x=1000, y=300)

label_4 = Tk.Label(root, text="", font=("Arial", 12))
label_4.place(x=900, y=100)

button = Tk.Button(root, text = "Enter", height=2, width=20, command=get_input)
button.place(x=1650, y=400)

root.mainloop()




































































































