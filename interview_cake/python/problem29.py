# You're working with an intern that keeps coming to you
# with JavaScript code that won't run because the braces,
# brackets, and parentheses are off. To save you both some time,
# you decide to write a braces/brackets/parentheses validator.

validOpeners = ['(', '{', '[']
validClosers = [')', '}', ']']
#Stack of the encounted opening brackets
stack = []
#Stack of the required closing brackets
closer_stack = []

def validateJsStack(str):
    requiredCloser = ""
    for currChar in str:
        if(len(closer_stack) > 0):
            requiredCloser = closer_stack[-1]
            if (currChar == reqCloser):
                stack.pop()
                closer_stack.pop()
        if currChar in validOpeners:
            stack.append(currChar)
            closerIndex = validOpeners.index(currChar)
            closer_stack.append(validClosers[closerIndex])
        #debugging
        print(stack)
        print("Required closer: " + reqCloser)
        print("Current char: " + currChar)
    if (len(stack) == 0):
        return True
    return False
