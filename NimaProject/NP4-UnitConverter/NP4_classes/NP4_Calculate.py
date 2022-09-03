from tkinter import *
class Calculate():
    centimeter = 'centimeter'
    meter = 'meter'
    kilometer = 'kilometer'
    inch = 'inch'
    feet = 'feet'
    yard = 'yard'
    mile = 'mile'

    def __init__(self, unit_to, value_from,entry_to):
        self.unit_to = unit_to
        self.value_from = value_from
        entry_to.delete(0, END)
