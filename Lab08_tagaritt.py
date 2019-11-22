## Lab 8: Trees

__Author__ = "Tinashe Tagarisa"
__Email__ = "tagaritt@mail.uc.edu"

## Functions from Lecture
def tree (root, branches=[]):
  for b in branches:
    assert is_tree(b), "branches must be trees"
  return [root] + list(branches)

def root(t):
  return t[0]

def branches(t):
  return t[1:]

def is_tree(t):
  if type(t) != list or len(t) < 1:
    return False
  for b in branches(t):
    if not is_tree(b):
      return False
  return True

def countLeaves(t):
  if branches == []:
    return 1
  else:
    sum = 0
    for b in branches(t):
      sum += countLeaves(b)
    return sum

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

#RQ1
def make_pytunes(username):
    """Return a pyTunes tree as shown in the diagram with USERNAME as the value
    of the root.

    >>> pytunes = make_pytunes('i_love_music')
    >>> print_tree(pytunes)
    i_love_music
      pop
        justin bieber
          single
            what do you mean?
        2015 pop mashup
      trance
        darude
          sandstorm
    """
    return tree(username,[tree('pop',[tree('justin bieber',[tree('single',[tree('what do you mean?')])]),tree('2015 pop mashup')]),tree('trance',[tree('darude',[tree('sandstorm')])])])

#RQ2
## Based off of countLeaves function
def num_songs(t):
    """Return the number of songs in the pyTunes tree, t.

    >>> pytunes = make_pytunes('i_love_music')
    >>> num_songs(pytunes)
    3
    """
    sum = 0
    if branches(t) == []:
      return 1
    for b in branches(t):
        sum += num_songs(b)
    return sum

#RQ3
def add_song(t, song, category):
    """Returns a new tree with SONG added to CATEGORY. Assume the CATEGORY
    already exists.

    >>> indie_tunes = tree('indie_tunes',
    ...                  [tree('indie',
    ...                    [tree('vance joy',
    ...                       [tree('riptide')])])])
    >>> new_indie = add_song(indie_tunes, 'georgia', 'vance joy')
    >>> print_tree(new_indie)
    indie_tunes
      indie
        vance joy
          riptide
          georgia

    """
    if root(t) == category:
        return tree(root(t), branches(t) + [tree(song)])
    totTree = [add_song(b, song, category) for b in branches(t)]
    return tree(root(t), totTree)

#RQ4
def delete(t, target):
    """Returns the tree that results from deleting TARGET from t. If TARGET is
    a category, delete everything inside of it.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    """
    restOfTree = [delete(b, target) for b in branches(t) if root(b) != target]
    return tree(root(t), restOfTree)

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose = True)
