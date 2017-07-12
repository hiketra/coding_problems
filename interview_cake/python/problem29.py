# You're working with an intern that keeps coming to you
# with JavaScript code that won't run because the braces,
# brackets, and parentheses are off. To save you both some time,
# you decide to write a braces/brackets/parentheses validator.

### Partial solution...
### TODO: Need to remove index-based logic in validateJsBraces, needs
## to iterate through every character to account for inner-brackets!

validOpeners = ['(', '{', '[']
validClosers = [')', '}', ']']

def getCorrespondingCloser(char):
    limit = len(validOpeners)
    i = 0
    flag = True
    while i < limit:
        if (validOpeners[i] == char):
            return validClosers[i]
        else:
            i+=1

# Loops through a supplied string's characters checking for openers
# and then splits the string into a substring from that index on-wards
# to check for a corresponding closer.

def validateJsBraces(str):
    limit = len(str)
    i = 0
    while i < limit:
        ## Trying to emulate conventional C-style for loops since index-heavy
        currentChar = str[i]
        if currentChar in validOpeners:
            hasCloser = validateSubstring(str[i:], getCorrespondingCloser(currentChar))
            if(hasCloser == -1):
                return False
            else:
                i = hasCloser
        else:
            i+=1
    return True
# Takes a substring, checks for a relevant opener/closer and returns
# the index at which the closing character is found, or -1 if not found

def validateSubstring(str, char):
    for currChar in str:
        if (currChar == char):
            return str.index(currChar)
    ##if there is no closer, return -1
    return -1
