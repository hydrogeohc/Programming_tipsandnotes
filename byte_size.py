## Returns the length of a string in bytes.
## utf-8 encodes a given string and find its length.

def byte_size(string):
    return(len(string.encode('utf-8')))

## byte_size('😀') # 4
## byte_size('Hello World') # 11

