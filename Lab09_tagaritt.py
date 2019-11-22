# Lab 09: Mutable Linked Lists

__Author__ = "Tinashe Tagarisa"
__Email__ = "tagaritt@mail.uc.edu"

class Link:
 
    empty = ()
 
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

def print_link(link):
    """Print elements of a linked list link.
 
    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' +helper(link).rstrip() +'>')
 
def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' +helper(link.first).rstrip() + '> '+ helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

# RQ1
def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> print_link(reverse(Link(1)))
    <1>
    >>> link = Link(1, Link(2, Link(3)))
    >>> new = reverse(link)
    >>> print_link(new)
    <3 2 1>
    >>> print_link(link)
    <1 2 3>
    """
    new = Link(link.first)
    while link.rest is not Link.empty:
        link = link.rest
        new = Link(link.first, new)
    return new

# RQ2
def add_links(link1, link2):
    """Adds two Links, returning a new Link

    >>> l1 = Link(1, Link(2))  
    >>> l2 = Link(3, Link(4, Link(5)))
    >>> new = add_links(l1,l2)
    >>> print_link(new)
    <1 2 3 4 5>
    """
    result = Link.empty
    while link1 is not Link.empty:
        result = Link(link1.first, result)
        link1 = link1.rest
    while link2 is not Link.empty:
        result = Link(link2.first, result)
        link2 = link2.rest
    return reverse(result)    

# RQ3
def slice_link(link, start, end):
    """Slices a Link from start to end (as with a normal Python list).

    >>> link = Link(3, Link(1, Link(4, Link(1, Link(5, Link(9))))))
    >>> new = slice_link(link, 1, 4)
    >>> print_link(new)
    <1 4 1>
    """
    if end == 0:
        return Link.empty
    elif start == 0:
        return Link(link.first, slice_link(link.rest, 0, end-1))
    else:
        return slice_link(link.rest, start-1, end-1)

# RQ4
def rep_link(link):
  """  Modified print_link to return string  """
  return('<' +helper(link).rstrip() +'>')

def mygetitem(s, i):
        if i == 0:
            return s.first
        elif isinstance(i,slice):
            return slice_link(s, i.start, i.stop)
        else:
            return mygetitem(s.rest, i-1)
        
def mysetitem(s, i, x):
        if i==0:
            s.first = x
        else:
            mysetitem(s.rest, i-1, x)

Link.__repr__ = rep_link
Link.__neg__ = reverse
Link.__add__ = add_links 
Link.__getitem__ = mygetitem # write to return Link item 
Link.__setitem__ = mysetitem # write to set Link item  

def magic_test():
  """
  >>> s = Link(3, Link(1, Link(4, Link(1, Link(5, Link(9))))))
  >>> s
  <3 1 4 1 5 9>
  >>> -s
  <9 5 1 4 1 3>
  >>> --s
  <3 1 4 1 5 9>
  >>> s[0]=30
  >>> s
  <30 1 4 1 5 9>
  >>> s+s
  <30 1 4 1 5 9 30 1 4 1 5 9>
  >>> s[1:3]
  <1 4>
  """

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose = True)
