# Flash Card App

from tkinter import *
from gtts import gTTS
import pandas
import random
import os
import playsound

# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #
to_learn = {}
current_card = {}
total_words_amount = 0
learned_words_amount = 0

try:
    data = pandas.read_csv("data/ielts_words_to_learn.csv")
    original_data = pandas.read_csv("data/ielts_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/ielts_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    total_words_amount = len(original_data)
    learned_words_amount = total_words_amount - len(data)


def next_card():
    language = "en"
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    window.after_cancel(flip_timer)
    canvas.itemconfig(words_count, text=f"Words mastered: {learned_words_amount}/{total_words_amount}")
    canvas.itemconfig(word_term, text="English", fill="black")
    canvas.itemconfig(word_definition, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    # TODO: Play audio sound (Text-To-Speech)
    window.after(100)
    audio_output = gTTS(text=current_card["English"], lang=language)
    audio_output.save("english_word.mp3")
    playsound.playsound("english_word.mp3", True)
    os.remove("english_word.mp3")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    language = "vi"
    canvas.itemconfig(word_term, text="Vietnamese", fill="white")
    canvas.itemconfig(word_definition, text=current_card["Vietnamese"], fill="white")
    canvas.itemconfig(card_background, image=card_back)
    window.after(100)
    audio_output = gTTS(text=current_card["Vietnamese"], lang=language)
    audio_output.save("vietnamese_word.mp3")
    playsound.playsound("vietnamese_word.mp3", True)
    os.remove("vietnamese_word.mp3")


def is_known():
    global learned_words_amount, total_words_amount
    to_learn.remove(current_card)
    words_to_learn_data = pandas.DataFrame.from_dict(to_learn)
    learned_words_amount = total_words_amount - len(words_to_learn_data)
    words_to_learn_data.to_csv("data/ielts_words_to_learn.csv", index=False)
    canvas.itemconfig(words_count, text=f"Words mastered: {learned_words_amount}/{total_words_amount}")
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title(f"The Flashcard Game for Tùng Gấu")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front)
word_term = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_definition = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
words_count = canvas.create_text(400, 450,
                                 text=f"",
                                 font=("Arial", 20, "normal"),
                                 fill="aquamarine")
canvas.grid(column=0, row=1, columnspan=2)

right_button = Button(image=right_image, command=is_known, highlightthickness=0)
right_button.grid(column=1, row=2)

wrong_button = Button(image=wrong_image, command=next_card, highlightthickness=0)
wrong_button.grid(column=0, row=2)

next_card()

window.mainloop()
