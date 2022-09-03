# CHECK LINE 3 or NP4-ReadMe >>> for introduction of app

# when you run app
# a window will open
# there are 2 lists and 2 inputs
# you must select one item in each lists
# and you must enter a number in left input
# after that click in button (calculate) to receive a result
# result will show in right input
#
# Warning !!!
# DON'T ENTER ANYTHING IN RIGHT INPUT

from tkinter import *
from tkinter.font import *
from NP4_classes import NP4_Centimeter, NP4_Meter, NP4_Kilometer, NP4_Inch, NP4_Feet, NP4_Yard, NP4_Mile, NP4_Calculate

# printing version of app
print('NP4-UnitConverter V1.0 running...')


# brian of this app (calculate function)
def calculate():
    unit_from = list_box_from.get(ACTIVE)
    unit_to = list_box_to.get(ACTIVE)
    value_from = int(entry_from.get())
    if unit_from == NP4_Calculate.Calculate.centimeter:
        NP4_Centimeter.Centimeter(unit_to, value_from, entry_to)
    elif unit_from == NP4_Calculate.Calculate.meter:
        NP4_Meter.Meter(unit_to, value_from, entry_to)
    elif unit_from == NP4_Calculate.Calculate.kilometer:
        NP4_Kilometer.Kilometer(unit_to, value_from, entry_to)
    elif unit_from == NP4_Calculate.Calculate.inch:
        NP4_Inch.Inch(unit_to, value_from, entry_to)
    elif unit_from == NP4_Calculate.Calculate.feet:
        NP4_Feet.Feet(unit_to, value_from, entry_to)
    elif unit_from == NP4_Calculate.Calculate.yard:
        NP4_Yard.Yard(unit_to, value_from, entry_to)
    elif unit_from == NP4_Calculate.Calculate.mile:
        NP4_Mile.Mile(unit_to, value_from, entry_to)


# window (little screen)
window = Tk()

# font and size
my_font = Font(family='Consoles', size=20)

# padding variables
pad_x, pad_y = 5, 5

# labels (names)
label_from = Label(window, text='From', font=my_font)
label_to = Label(window, text='To', font=my_font)
label_enter = Label(window, text='Enter a number', font=my_font)
label_result = Label(window, text='Result', font=my_font)

# labels grid
label_from.grid(row=0, column=0, sticky=W, padx=pad_x, pady=pad_y)
label_to.grid(row=0, column=1, sticky=W, padx=pad_x, pady=pad_y)
label_enter.grid(row=2, column=0, sticky=W)
label_result.grid(row=2, column=1, sticky=W)

# entries (inputs)
entry_from = Entry(window, font=my_font, fg='blue')
entry_to = Entry(window, font=my_font, fg='blue')

# entries grid
entry_from.grid(row=3, column=0, padx=pad_x, pady=pad_y)
entry_to.grid(row=3, column=1, padx=pad_x, pady=pad_y)

# list boxes (list)
list_box_from = Listbox(window, exportselection=False, font=my_font)
list_box_to = Listbox(window, exportselection=False, font=my_font)

# list boxes grid
list_box_from.grid(row=1, column=0)
list_box_to.grid(row=1, column=1)

# button
button = Button(window, text='calculate', font=my_font, command=calculate)

# button grid
button.grid(row=4, column=0, columnspan=2, sticky=W + E, padx=pad_x, pady=pad_y)

# list_from options
list_box_from.insert(END, 'centimeter')
list_box_from.insert(END, 'meter')
list_box_from.insert(END, 'kilometer')
list_box_from.insert(END, 'inch')
list_box_from.insert(END, 'feet')
list_box_from.insert(END, 'yard')
list_box_from.insert(END, 'mile')

# list_to options
list_box_to.insert(END, 'centimeter')
list_box_to.insert(END, 'meter')
list_box_to.insert(END, 'kilometer')
list_box_to.insert(END, 'inch')
list_box_to.insert(END, 'feet')
list_box_to.insert(END, 'yard')
list_box_to.insert(END, 'mile')

# run app function
window.mainloop()
