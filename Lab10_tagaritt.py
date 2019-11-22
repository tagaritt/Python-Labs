__Author__ = "Tinashe Tagarisa"
__Email__ = "tagaritt@mail.uc.edu"

# Lab 10

#############
# Iterators #
#############

#RQ1
class Cheer:
    """
    >>> UC = Cheer("Bearcats")
    >>> for c in UC:
    ...     print(c)
    ...
    Give me an B
    Give me an e
    Give me an a
    Give me an r
    Give me an c
    Give me an a
    Give me an t
    Give me an s
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, chant):
      self.chant = chant
    def __iter__(self):
      self.i = -1
      return self
    def __next__(self):
      self.i += 1
      if self.i >= len(self.chant):
        raise StopIteration
      return "Give me an " + self.chant[self.i]

#RQ2
class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    
    "*** YOUR CODE HERE ***"
    def __init__(self, num):
      self.num = num
    def __iter__(self):
      self.end = 0
      return self
    def __next__(self):
      if self.num < self.end:
        raise StopIteration
      self.num -= 1
      return self.num + 1


##############
# Generators #
##############

# RQ3
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    n = 1
    while True:
      yield n
      n += 1

#RQ4
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    for i in s:
      yield i*k

# RQ5
def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    while n >= 0:
      yield n
      n -= 1

# RQ6
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    while n > 1:
      if n % 2 == 0:
        yield int(n)
        n = n/2
      else:
        yield int(n)
        n = (n*3) + 1
    yield int(n)

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose = True)
