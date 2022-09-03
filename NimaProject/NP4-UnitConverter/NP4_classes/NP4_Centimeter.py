# if you want run only this module >>> use line 4
# if you want run unit converter module >>> use line 5

# from NP4_Calculate import Calculate
from NP4_classes.NP4_Calculate import Calculate
from tkinter import *


class Centimeter(Calculate):
    centimeter_number = 1
    meter_number = 0.01
    kilometer_number = 0.00001
    inch_number = 0.3937007874
    feet_number = 0.032808399
    yard_number = 0.010936133
    mile_number = 0.0000062137

    def __init__(self, unit_to, value_from, entry_to):
        Calculate.__init__(self, unit_to, value_from, entry_to)
        if unit_to == Calculate.centimeter:
            result = value_from * Centimeter.centimeter_number
        elif unit_to == Calculate.meter:
            result = value_from * Centimeter.meter_number
        elif unit_to == Calculate.kilometer:
            result = value_from * Centimeter.kilometer_number
        elif unit_to == Calculate.inch:
            result = value_from * Centimeter.inch_number
        elif unit_to == Calculate.feet:
            result = value_from * Centimeter.feet_number
        elif unit_to == Calculate.yard:
            result = value_from * Centimeter.yard_number
        elif unit_to == Calculate.mile:
            result = value_from * Centimeter.mile_number
        else:
            result = 'Just Numbers'
        entry_to.insert(END, result)
