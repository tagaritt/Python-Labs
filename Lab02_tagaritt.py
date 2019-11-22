__author__ = "Tinashe Tagarisa"
__email__ = "tagaritt@mail.uc.edu"

""" 4 Required Questions for Lab 2 """

#  RQ1
from operator import add, sub

def a_plus_abs_b(a, b):

  """
  Return a+abs(b), but without calling abs.
  
  >>> a_plus_abs_b(2, 3)
  5
  >>> a_plus_abs_b(2, -3)
  5
  """
  
  if b < 0:
    f = sub
  else:
    f = add
   
  return f(a, b)

#  RQ2
def two_of_three(a, b, c):
    """
    Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    if ((((a > b) or (a > c)) and ((b > a) or (b > c))) or ((a == b) and (a > c))):
      x = a
      y = b
    elif ((((b > a) or (b > c)) and ((c > a) or (c > b))) or ((b == c) and (b > a))):
      x = b
      y = c
    elif ((((c > b) or (c > a)) and ((a > b) or (a > c))) or ((c == a) and (c > b))):
      x = c
      y = a
    else:
      x = a
      y = b

    return ((x * x) + (y * y))

#  RQ3
def largest_factor(n):
  """
  Return the largest factor of n that is smaller than n.
  
  >>> largest_factor(15) # factors are 1, 3, 5
  5
  >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
  40
  """

  largeFact = 1
  i = 2
  
  while (i < n):
    if (n % i == 0):
      largeFact = i
    i = i + 1
  
  return largeFact

#  RQ4
#  Write functions c, t, and f such that calling the with_if_statement and
#  calling the with_if_function do different things.
#  Such that the with_if_statement function returns the number 1, 
#  but calling the with_if_function function throws a ZeroDivisionError.

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return False

def t():
    return 1/0

def f():
    return 1

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
