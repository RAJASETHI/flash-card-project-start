import random
from tkinter import *
import pandas
from tkinter import messagebox
import time

BACKGROUND_COLOR = "#B1DDC6"
lang_dict = {row.French: row.English for (index, row) in pandas.read_csv("data/french_words.csv").iterrows()}

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=810, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
img_front = PhotoImage(file="images/card_front.png")
img_back = PhotoImage(file="images/card_back.png")
text_img = canvas.create_image(400, 270, image=img_front)
canvas.grid(column=0, row=0, columnspan=2)
french_txt = "trouve"
text_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
text_word = canvas.create_text(400, 263, text=french_txt, font=("Arial", 60, "bold"))


# ******************************** Buttons And Functions *************************************** #
def change_ans():
    canvas.itemconfig(text_word, text=lang_dict[french_txt], fill="white")
    canvas.itemconfig(text_title, text="English", fill="white")
    canvas.itemconfig(text_img, image=img_back)


def next_card():
    global french_txt
    canvas.itemconfig(text_title, text="French", fill="black")
    french_txt = random.choice(list(lang_dict))
    canvas.itemconfig(text_word, text=french_txt, fill="black")
    canvas.itemconfig(text_img, image=img_front)
    window.after(3000, func=change_ans)


window.after(3000, func=change_ans)


def right_fun():
    if len(lang_dict) == 0:
        messagebox.showinfo("Flusshy", "You have Successfully learned all the words, Congratulation!!!")
        exit()
    lang_dict.pop(french_txt)
    next_card()
    print("done")


def wrong_fun():
    if len(lang_dict) == 0:
        messagebox.showinfo("Flusshy", "You have Successfully learned all the words, Congratulation!!!")
        exit()
    next_card()


my_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=my_image, highlightthickness=0, command=wrong_fun)
wrong.grid(column=0, row=1)

my_image1 = PhotoImage(file="images/right.png")
right = Button(image=my_image1, highlightthickness=0, command=right_fun)
right.grid(column=1, row=1)

window.mainloop()
