import re

class NotStringError(Exception):pass
class InvalidStringError(Exception):pass
class OutputError(Exception):pass
def check(s,t,m):
     
     if m!=0 and m!=1:
        if s==t:
             return ''
        else:
             return False
         
     else:
        return True  
def palin(a):
    if type(a) != str:raise NotStringError,"checking only string palindrome"
    match=re.search(r'\W+',a)
    if match:raise InvalidStringError,"the string contains invaid characters"
    c=len(a)
    y=0
    z=c-1
    while True:
        v=a[y]
        r=a[z]
        j=check(v,r,c)
        if j==True or j==False:
            print j
            return j
        y+=1
        z-=1
        c-=2 
    

h=raw_input('enter the string\n')
x=len(h)
palin(h)
