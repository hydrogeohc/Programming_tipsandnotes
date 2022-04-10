##Retuns number of vowels in provided string.
##Use a regular expression to count the number of vowels(A, E, I, O, U) in a string.

import re


def count_vowels(str):
    return len(len(re.findall(r'[aeiou]', str, re.IGNORECASE)))


## count_vowels('foobar') # 3
## count_vowels('gym')  # 0
