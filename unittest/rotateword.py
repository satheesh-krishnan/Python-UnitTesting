class TypeError(Exception):pass

def rotate(x,y):
    if type(x) != str or type(y) != int: raise TypeError, "invalid input"
    a='abcdefghijklmnopqrstuvwxyz'
    r=''
    for c in x:
        d=ord(c)
        n=d-97
        e=(n+y)%26
        r +=a[e]
    return r



