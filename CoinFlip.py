"""******************************************************************************
* Purpose: Coin Filp
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 21-12-2018
*
******************************************************************************
"""

from Utility import utilities

try:

    a=int(input("Enter number of times to flip coin "))
    utilities.flip_coin(a)
except Exception :
    print(Exception)