"""******************************************************************************
* Purpose: Harmonic Number
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 21-12-2018
*
******************************************************************************
"""
from Utility import utilities
try:
    a=int(input("Enter number to find nth harmonic "))
    utilities.harmonic(a)
except(ZeroDivisionError,ValueError):
    print("Enter valid number")