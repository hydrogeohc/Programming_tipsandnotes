## Removes falsey values from a list.
## Use filter() to filter out falsey values(False, None, 0, and "").

def compact(lst):
    return list(filter(bool, lst))

# compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
