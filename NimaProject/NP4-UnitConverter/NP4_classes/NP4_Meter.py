# if you want run only this module >>> use line 4
# if you want run unit converter module >>> use line 5

# from NP4_Calculate import Calculate
from NP4_classes.NP4_Calculate import Calculate
from tkinter import *


class Meter(Calculate):
    centimeter_number = 100
    meter_number = 1
    kilometer_number = 0.001
    inch_number = 39.37007874
    feet_number = 3.280839895
    yard_number = 1.0936132983
    mile_number = 0.0006213712

    def __init__(self, unit_to, value_from, entry_to):
        Calculate.__init__(self, unit_to, value_from, entry_to)
        if unit_to == Calculate.centimeter:
            result = value_from * Meter.centimeter_number
        elif unit_to == Calculate.meter:
            result = value_from * Meter.meter_number
        elif unit_to == Calculate.kilometer:
            result = value_from * Meter.kilometer_number
        elif unit_to == Calculate.inch:
            result = value_from * Meter.inch_number
        elif unit_to == Calculate.feet:
            result = value_from * Meter.feet_number
        elif unit_to == Calculate.yard:
            result = value_from * Meter.yard_number
        elif unit_to == Calculate.mile:
            result = value_from * Meter.mile_number
        else:
            result = 'Just Numbers'
        entry_to.insert(END, result)
