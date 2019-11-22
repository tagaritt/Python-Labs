## Lab 5: Required Questions - Dictionaries Questions ##

__author__ = "Tinashe Tagarisa"
__email__ = "tagaritt@mail.uc.edu"

# RQ1
def merge(dict1, dict2):
  """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

  >>> merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
  {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
  """
  for i in dict2.keys():
    dict1[i] = dict2[i]
  listKeys = [i for i in dict1.keys()]
  for i in range(len(listKeys) - 1):
    for j in range(len(listKeys) - i - 1):
      if (listKeys[j] > listKeys[j + 1]):
        listKeys[j], listKeys[j + 1] = listKeys[j + 1], listKeys[j]
  dict2.clear()
  for i in listKeys:
    dict2[i] = dict1[i]
  return dict2
  

# RQ2
def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    
    tokens = message.split()

    temp = list(set(tokens))
    i = 0
    new = {}

    while i < len(temp):
      new[temp[i]] = tokens.count(temp[i])
      i += 1

    return new


# RQ3
def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    
    for i in d:
      if d[i] == x:
        d[i] = y

# RQ4
import collections

def sumdicts(lst):
  """ 
  Takes a list of dictionaries and returns a single dictionary which contains all the keys value pairs. And 
  if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned as the value for that key
  >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
  >>> d == sumdicts ([{'b': 88, 'c': 100, 'a': 140, 'd': 19}])
  True
  """
  "*** YOUR CODE HERE ***"
  count = collections.Counter()

  for i in lst:
    count.update(i)
  result = dict(count)

#RQ5
def middle_tweet(word, table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and returns the one string that is of length right in middle of the 5.
    Returns a string that is a random sentence of average length starting with word, and choosing successors from table.
    """
    "*** YOUR CODE HERE ***"

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose = True)
