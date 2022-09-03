# if you want run only this module >>> use line 4
# if you want run unit converter module >>> use line 5

# from NP4_Calculate import Calculate
from NP4_classes.NP4_Calculate import Calculate
from tkinter import *


class Kilometer(Calculate):
    centimeter_number = 100000
    meter_number = 1000
    kilometer_number = 1
    inch_number = 39370.07874
    feet_number = 3280.839895
    yard_number = 1093.6132983
    mile_number = 0.6213712

    def __init__(self, unit_to, value_from, entry_to):
        Calculate.__init__(self, unit_to, value_from, entry_to)
        if unit_to == Calculate.centimeter:
            result = value_from * Kilometer.centimeter_number
        elif unit_to == Calculate.meter:
            result = value_from * Kilometer.meter_number
        elif unit_to == Calculate.kilometer:
            result = value_from * Kilometer.kilometer_number
        elif unit_to == Calculate.inch:
            result = value_from * Kilometer.inch_number
        elif unit_to == Calculate.feet:
            result = value_from * Kilometer.feet_number
        elif unit_to == Calculate.yard:
            result = value_from * Kilometer.yard_number
        elif unit_to == Calculate.mile:
            result = value_from * Kilometer.mile_number
        else:
            result = 'Just Numbers'
        entry_to.insert(END, result)
