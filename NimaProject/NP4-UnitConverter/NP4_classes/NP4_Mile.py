# if you want run only this module >>> use line 4
# if you want run unit converter module >>> use line 5

# from NP4_Calculate import Calculate
from NP4_classes.NP4_Calculate import Calculate
from tkinter import *


class Mile(Calculate):
    centimeter_number = 160934.3979894787
    meter_number = 1609.3439798948
    kilometer_number = 1.6093439799
    inch_number = 63359.9992082028
    feet_number = 5279.9999340169
    yard_number = 1759.999977952
    mile_number = 1

    def __init__(self, unit_to, value_from, entry_to):
        Calculate.__init__(self, unit_to, value_from, entry_to)
        if unit_to == Calculate.centimeter:
            result = value_from * Mile.centimeter_number
        elif unit_to == Calculate.meter:
            result = value_from * Mile.meter_number
        elif unit_to == Calculate.kilometer:
            result = value_from * Mile.kilometer_number
        elif unit_to == Calculate.inch:
            result = value_from * Mile.inch_number
        elif unit_to == Calculate.feet:
            result = value_from * Mile.feet_number
        elif unit_to == Calculate.yard:
            result = value_from * Mile.yard_number
        elif unit_to == Calculate.mile:
            result = value_from * Mile.mile_number
        else:
            result = 'Just Numbers'
        entry_to.insert(END, result)
