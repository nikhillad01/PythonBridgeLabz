"""******************************************************************************
* Purpose: Prime Factors of number
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 22-12-2018
*
******************************************************************************"""

from Utility import utilities
u=utilities.util()
def prime_facs():
    """This method is used to take the inputs to find the prime factors in a range ."""
    try:
        a=int(input("enter number to find prime factors"))
    except ValueError:
        print("Enter integer")
    u.prime_factors(a)
if __name__=="__main__":
    prime_facs()