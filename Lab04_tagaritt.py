##Lab04 Required Questions ##

__Author__ = "Tinashe Tagarisa"
__Email__ = "tagaritt@mail.uc.edu"

#########
# Lists #
#########

# RQ1
def cascade(lst):
  """Returns the cascade of the given list.
  
  >>> cascade([1, 2, 3, 4])
  [1, 2, 3, 4, 4, 3, 2, 1]
  """
  if (not lst):
    return []
  return lst[:1] + cascade(lst[1:]) + [lst[0]] 

# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    
    result = []
    for elem in seq:
        result += [fn(elem) * fn(elem)]
    return result

#RQ3
def filterout(pred, seq):
  """Keeps elements in seq only if they do not satisfy pred.

  >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
  [1, 3]
  """
    
  result = []

  for elem in seq:
    if pred(elem):
      result += [elem - 1]
  return result

#RQ4
def comp(n, pred):
  """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
  >>> comp(7, lambda x: x%2 ==0)
  [0, 2, 4, 6]
  """
  
  return [i for i in range(n) if pred(i)]

#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    
    return sum(([x] if not isinstance(x, list) else flatten(x) for x in lst), [])

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose = True)
