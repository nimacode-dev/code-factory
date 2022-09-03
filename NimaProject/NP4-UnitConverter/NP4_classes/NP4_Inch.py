# if you want run only this module >>> use line 4
# if you want run unit converter module >>> use line 5

# from NP4_Calculate import Calculate
from NP4_classes.NP4_Calculate import Calculate
from tkinter import *


class Inch(Calculate):
    centimeter_number = 2.54
    meter_number = 0.0254
    kilometer_number = 0.0000254
    inch_number = 1
    feet_number = 0.0833333333
    yard_number = 0.0277777778
    mile_number = 0.0000157828

    def __init__(self, unit_to, value_from, entry_to):
        Calculate.__init__(self, unit_to, value_from, entry_to)
        if unit_to == Calculate.centimeter:
            result = value_from * Inch.centimeter_number
        elif unit_to == Calculate.meter:
            result = value_from * Inch.meter_number
        elif unit_to == Calculate.kilometer:
            result = value_from * Inch.kilometer_number
        elif unit_to == Calculate.inch:
            result = value_from * Inch.inch_number
        elif unit_to == Calculate.feet:
            result = value_from * Inch.feet_number
        elif unit_to == Calculate.yard:
            result = value_from * Inch.yard_number
        elif unit_to == Calculate.mile:
            result = value_from * Inch.mile_number
        else:
            result = 'Just Numbers'
        entry_to.insert(END, result)
