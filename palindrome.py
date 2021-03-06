#Returns True if the given string is a palindrome, False otherwise.

#Convert string str.lower() and use re.sub to remove non-alphanumeric characters from it. Then compare the new string to the reversed.
def palindrome(string):
    from re import sub
    s = sub('[\W_]', '', string.lower())
    return s == s[::-1]

###############################################################################
#palindrome('taco cat') # True
#palindrome('taco cat!') # False

###############################################################################