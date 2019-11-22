__author__ = "Tinashe Tagarisa"
__email__ = "tagaritt@mail.uc.edu"

"""Four Required Questions for Lab 1"""

## Boolean Operators ##
# RQ1
def both_negative(x, y):
    """Returns True if and only if both x and y are negative.
 
    >>> both_negative(-1, 1)
    False
    >>> both_negative(1, 2)
    False
    >>> both_negative(-1, -2)
    True
    """
    
    "*** YOUR CODE HERE ***"

    ## The purpose of this function is to check all of the input x-values and the input y-values to see whenever they're both positive. ##

    # The code below is executed if the x-values and the y-values are both positive (>0).
    if ((x < 0) and (y < 0)):

      # If the x-values and the y-values are both positive, then the function will return the boolean value "True".
      return True

    # The code below is executed if either one (or both) of the x-value(s) or the y-value(s) are negative.  
    else:

      # If either one (or both) of the x-value(s) or the y-values are negative, then the function will return the boolean value "False".
      return False

## While Loops ##
# RQ2
def not_factor (n):
    """Prints out all of the numbers less than n which do not divide `n` evenly.
 
    >>> not_factor(10)
    9
    8
    7
    6
    4
    3
    """

    "*** YOUR CODE HERE ***"

    ## The purpose of this function is to print all values that (a) are less than the nth term and (b) are unable to evenly divide the nth term. ##
    
    # Initializes starting point of the while loop that appears later.
    i = n 

    # A while loop is created in order to evaluate all numbers less than the nth term (not including 0). 
    while (i > 0):
      
      # Incrementally decreases the comparator by 1.
      i -= 1
      
      # Exception Handling: If comparator reaches zero, the code below is executed.
      if (i == 0):
      
        # The function stops processing once i = 0.
        break
      
      # The code below is executed if the nth term cannot be evenly devided by the comparator at its current incremental value.
      if (n % i != 0):

        # The comparator (at its current incremental value) will be printed.
        print(i)
 
# RQ3
def lucas(n):
    """Returns the nth Lucas number.
      Lucas numbers form a series similar in pattern to the Fibonacci sequence:
      2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843,...
 
    >>> lucas(0)
    2
    >>> lucas(1)
    1
    >>> lucas(2)
    3
    >>> lucas(3)
    4
    >>> lucas(11)
    199
    >>> lucas(100)
    792070839848372253127
    """
    "*** YOUR CODE HERE ***"

    ## The purpose of this function is to calculate a Lucas number sequence to the nth term. ##

    # Starts the Lucas number sequence with the integers 2 and 1, respectively.
    x, y = 2, 1
     
    # A while loop is created to emulate the number sequence building upon itself 'n' number of times.
    while n > 0:

      # Initializes the x- and y-values.
      x, y = y, x + y
      
      # Incrementally decreases the nth term. 
      n -= 1

    # The return statement below fetches the final term of the Lucas number sequence to the nth term.
    return x

#RQ4
def gets_discount(p1, p2, p3):
    """ Returns True if p1 is an adult (age at least 18) and p2 and p3 are both children (age 12 or below), 
    False otherwise. Do not use if statement.
    >>> gets_discount(15, 12, 11)
    False
    >>> gets_discount(90, 7, 12)
    True
    >>> gets_discount(18, 18, 18)
    False
    >>> gets_discount(40, 7, 15)
    False
    """

    return ((p1 >= 18) and (p2 <= 12) and (p3 <= 12))

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)