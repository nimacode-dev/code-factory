# if you want run only this module >>> use line 4
# if you want run unit converter module >>> use line 5

# from NP4_Calculate import Calculate
from NP4_classes.NP4_Calculate import Calculate
from tkinter import *


class Feet(Calculate):
    centimeter_number = 30.4800000001
    meter_number = 0.3048
    kilometer_number = 0.0003048
    inch_number = 12
    feet_number = 1
    yard_number = 0.3333333333
    mile_number = 0.0001893939

    def __init__(self, unit_to, value_from, entry_to):
        Calculate.__init__(self, unit_to, value_from, entry_to)
        if unit_to == Calculate.centimeter:
            result = value_from * Feet.centimeter_number
        elif unit_to == Calculate.meter:
            result = value_from * Feet.meter_number
        elif unit_to == Calculate.kilometer:
            result = value_from * Feet.kilometer_number
        elif unit_to == Calculate.inch:
            result = value_from * Feet.inch_number
        elif unit_to == Calculate.feet:
            result = value_from * Feet.feet_number
        elif unit_to == Calculate.yard:
            result = value_from * Feet.yard_number
        elif unit_to == Calculate.mile:
            result = value_from * Feet.mile_number
        else:
            result = 'Just Numbers'
        entry_to.insert(END, result)
