# tkinter, *args, **kwargs, GUI Programs

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=150, height=50)
window.config(padx=15, pady=15)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=1, row=2)

# Entry: Enter number in miles:
miles_input = Entry(width=10)
miles_input.grid(column=2, row=1)

# Label: Miles unit:
miles_unit = Label(text="Miles")
miles_unit.grid(column=3, row=1)

# Label: Km converted number:
km_converted = Label(text="0")
km_converted.grid(column=2, row=2)

# Label: Km unit:
km_unit = Label(text="Km")
km_unit.grid(column=3, row=2)


def button_clicked():
    number_miles = int(miles_input.get())
    number_km = round(number_miles * 1.609, 3)
    km_converted.config(text=number_km)


# Button: Convert:
convert_button = Button(text="Calculate", command=button_clicked)
convert_button.grid(column=2, row=3)

window.mainloop()
