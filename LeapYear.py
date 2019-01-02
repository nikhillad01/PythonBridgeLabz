"""******************************************************************************
* Purpose: Leap Year
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 21-12-2018
*
******************************************************************************
"""

from Utility import utilities
try:
    year=int(input("Enter Year to check leap Year"))
    utilities.leap_year(year)
except ValueError:
    print("Enter integer value")