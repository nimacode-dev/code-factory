# if you want run only this module >>> use line 4
# if you want run unit converter module >>> use line 5

# from NP4_Calculate import Calculate
from NP4_classes.NP4_Calculate import Calculate
from tkinter import *


class Yard(Calculate):
    centimeter_number = 91.4400000032
    meter_number = 0.9144
    kilometer_number = 0.0009144
    inch_number = 36.0000000011
    feet_number = 3.0000000001
    yard_number = 1
    mile_number = 0.0005681818

    def __init__(self, unit_to, value_from, entry_to):
        Calculate.__init__(self, unit_to, value_from, entry_to)
        if unit_to == Calculate.centimeter:
            result = value_from * Yard.centimeter_number
        elif unit_to == Calculate.meter:
            result = value_from * Yard.meter_number
        elif unit_to == Calculate.kilometer:
            result = value_from * Yard.kilometer_number
        elif unit_to == Calculate.inch:
            result = value_from * Yard.inch_number
        elif unit_to == Calculate.feet:
            result = value_from * Yard.feet_number
        elif unit_to == Calculate.yard:
            result = value_from * Yard.yard_number
        elif unit_to == Calculate.mile:
            result = value_from * Yard.mile_number
        else:
            result = 'Just Numbers'
        entry_to.insert(END, result)
