"""******************************************************************************
* Purpose: Prime Factors of number
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 22-12-2018
*
******************************************************************************"""

from Utility import utilities
try:

    a=int(input("enter number to find prime factors"))
    utilities.prime_factors(a)
except ValueError:
    print("Enter integer")