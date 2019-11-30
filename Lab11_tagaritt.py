__Author__ = "Tinashe Tagarisa"
__Email__ = "tagaritt@mail.uc.edu"

##################################################
# Lab 11: Higher-Order Generators and CoRoutines #
##################################################

#RQ1
def merge(s0, s1):
  """Yield the elements of strictly increasing iterables s0 and s1, removing repeats. Assume that s0 and s1 have no repeats. You can also assume that s0 and s1 represent infinite sequences.
  
  >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
  >>> type(m)
  <class 'generator'>
  >>> list(m)
  [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
  >>> def big(n):
  ...    k = 0
  ...    while True: yield k; k += n
  >>> m = merge(big(2), big(3))
  >>> [next(m) for _ in range(11)]
  [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
  """
  i0, i1 = iter(s0), iter(s1)
  e0, e1 = next(i0, None), next(i1, None)

  while True:
    # If there is no value in both the E0 and E1 lists, the function will stop.
    if ((e0 == None) and (e1 == None)):
      return 0

    # If there is no value in the E0 list, the function will refer to the E1 list.
    elif (e0 == None):
      yield e1
      e1 = next(i1, None)
    
    # If there is no value in the E1 list, the function will refer to the E0 list.
    elif (e1 == None):
      yield e0
      e0 = next(i0, None)
    
    # If there is a value in both the E0 and E1 lists, the function will sort both lists and print a new list in increasing order, skipping all repeating values.
    else:
      yield min(e0, e1)
      if (e0 < e1):
        e0 = next(i0, None)
      elif (e1 < e0):
        e1 = next(i1, None)
      else:
        e0, e1 = next(i0, None), next(i1, None)
    
#RQ2
def residues_generator(m):
    """
    Takes in an integer m, and yields m different generators, 
    each one returns the numbers in a distinct residue class of m.

    >>> res_mod_four = residues_generator(4)
    >>> for res_group in res_mod_four:
    ...     for _ in range(3):
    ...         print(next(res_group))
    0
    4
    8
    1
    5
    9
    2
    6
    10
    3
    7
    11
    """
    def res_group(residue):
        val = residue
        while True:
            yield val
            val += m

    for residue in range(m):
        yield res_group(residue)

#RQ3
def zip(*iterables):
  """
  Takes in any number of iterables and zips them together.
  Returns a generator that outputs a series of lists, each containing the nth items of each iterable.
  >>> z = zip([1, 2, 3], [4, 5, 6], [7, 8])
  >>> for i in z:
  ...     print(i)
  ...
  [1, 4, 7]
  [2, 5, 8]
  """
  endTerm = object()
  iterator = [iter(i) for i in iterables]
  while iterator:
    lst = []
    for i in iterator:
      var = next(i, endTerm)
      if var is endTerm:
        return
      lst.append(var)
    yield lst

# Extra Credit Question
def supplier(ingredients, chef):
    for ingredient in ingredients:
        try:
            chef.send(ingredient)
        except StopIteration as e:
            print(e)
            break
    chef.close()


def customer():
    served = False
    while True:
        try:
            dish = yield
            print('Yum! Customer got a {}!'.format(dish))
            served = True
        except GeneratorExit:
            if not served:
                print('Customer never got served.')
            raise

def chef(customers, dishes):
    """
    >>> cust = customer()
    >>> next(cust)
    >>> c = chef({cust: 'hotdog'}, {'hotdog': ['bun', 'hotdog']})
    >>> next(c)
    >>> supplier(['bun', 'hotdog'], c)
    Yum! Customer got a hotdog!
    Chef went home.

    >>> cust = customer()
    >>> next(cust)
    >>> c = chef({cust: 'hotdog'}, {'hotdog': ['bun', 'hotdog']})
    >>> next(c)
    >>> supplier(['bun'], c)
    Chef went home.
    Customer never got served.

    >>> cust = customer()
    >>> next(cust)
    >>> c = chef({cust: 'hotdog'}, {'hotdog': ['bun', 'hotdog']})
    >>> next(c)
    >>> supplier(['bun', 'hotdog', 'mustard'], c)
    Yum! Customer got a hotdog!
    No one left to serve!
    """
    custQueued = dict(customers)
    lstIng = set()
    
    while True:
        try:
            ingredient = yield
        except GeneratorExit:
            print('Chef went home.')
            for cust in customers:
                cust.close()
            raise

        lstIng.add(ingredient)

        if not custQueued:
            return 'No one left to serve!'

        for customer, meal in dict(custQueued).items():
            if not set(dishes[meal]) - lstIng:
                customer.send(meal)
                del custQueued[customer]

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose = True)
