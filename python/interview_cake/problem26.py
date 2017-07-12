#Write a function to reverse a string in-place

def inplaceStringReversal(string):
    lst = list(string)
    if(len(lst)%2 == 0):
        limit = len(lst)/2
    else:
        limit = (len(lst) - 1)/ 2

    for i in range(limit):
        a = lst[i]
        b = lst[-(i+1)]
        lst[i] = b
        lst[-(i+1)] = a

    return str(lst)
