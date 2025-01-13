# from googletrans import Translator, constants
# from pprint import pprint

# # init the Google API translator
# translator = Translator()

# # translate a spanish text to english text (by default)
# translation = translator.translate("Hola Mundo")
# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='en', target='ja')

#use this instead of 'googletrans'

import tkinter as Tk
from tkinter import messagebox, Checkbutton
from tkinter.ttk import *

def translation(text):
    translated = GoogleTranslator(source='en', target='ja')
    translate = translated.translate(text)
    return translate

def get_input():
    text_to_be_translated = textbox.get("1.0","end")
    translated_text = translation(text_to_be_translated)
    label_widget_3.config(text = "Translated text in Japanese: "+ translated_text) 


root = Tk.Tk()
title = Tk.Label(root, text = "Translator", font= ("Arial", 18), bg="yellow", fg="red")
root.geometry = ('1500x1500')
title.pack(padx=0,pady=0,side='top')

label_widget_1 = Tk.Label(root, text = "Google translate", font=("Arial", 24))
label_widget_1.place(x=1160,y=50)

label_widget_2 = Tk.Label(root, text = "English",font=("Arial", 18))
label_widget_2.place(x= 425, y= 150)

textbox = Tk.Text(root, height = 25, font= ("Arial", 16))
# textbox.bind("<Enter>", translation)
textbox.pack(padx=10, pady=10, side= 'left')

label_widget_3 = Tk.Label(root, text = "Translated text in Japanese:", font=("Arial", 18))
label_widget_3.place(x= 1500, y= 500)

button = Tk.Button(root, text = 'Translate!', command = get_input)
button.pack(side= 'left')

root.mainloop()  


    # combo = Combobox(self)
    # combo['Languages'] = ("Korean", 1, 2, 3)
    # combo.current(0)
    # combo.grid(column=0, row=0)
    
    # root.protocol("WM_DELETE_WINDOW", on_closing)



# def on_closing(self):
#     if messagebox.askyesno(title= "Quit?", message= "Are you sure you want to quit?"):
#         root.destroy()

# def shortcut(self, event):
# #print(event)
# #print(event.state)	
#     if event.state == 12 and event.keysym == "Return":
#     #print("Jet is handsome")
#         show_message()







