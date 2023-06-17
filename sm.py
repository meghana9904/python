#1 upper
def upper1(x):
    y=""
    for z in x:
        if ord(z)>=97 and ord(z)<=122:
            y+=chr(ord(z)-32)
        else:
            y+=z
    return y

#2 lower()
def lower1(x):
    y=""
    for z in x:
        if ord(z)>=65 and ord(z)<=90:
            y+=chr(ord(z)+32)
        else:
            y+=z
    return y

#3 isuuper()
def isupper1(x):
    y=""
    for z in x:
        if ord(z)>=97 and ord(z)<=122:
            y+=chr(ord(z)-32)
            return False
        else:
            y+=z
            return True
            
#4 islower()
def islower1(x):
    y=""
    for z in x:
        if ord(z)>=65 and ord(z)<=90:
            y+=chr(ord(z)+32)
            return False
        else:
            y+=z
            return True
        
#5 isalpha()
def isalpha1(x):
    for z in x:
        if ord(z)>=65 and ord(z)<=122:
            return True
        else:
            return False
        
#6 isdigit()
def isdigit1(x):
    for z in x:
        if ord(z)>=48 and ord(z)<=57:
            return True
        else:
            return False
        
#7 isalnum()
def isalnum1(x):
    for z in x:
        if ord(z)>=48 and ord(z)<=122:
            return True
        else:
            return False
        
        
#8 swapcase()
def swapcase1(x):
    z=""
    for y in x:
        if ord(y)>=65 and ord(y)<=90:
            z+=chr(ord(y)+32)
        elif ord(y)>=97 and ord(y)<=122:
            z+=chr(ord(y)-32)
        else:
            z+=y
    return z


#9 capitalize()
def capitalize1(y):
    s=""
    for x in range(len(y)):
        if x==0:
            if ord(y[0])<=122 and ord(y[0])>=97:
                s+=chr(ord(y[0])-32)
            else:
                s+=y[x]
        else:
            if y[x-1]==" ":
                if ord(y[x])<=122 and ord(y[x])>=97:
                    s+=chr(ord(y[x])-32)
                    continue
                else:
                    s+=y[x]
                    continue
            elif ord(y[x])>=65 and ord(y[x])<=90:
                s+=chr(ord(y[x])+32)
            else:
                s+=y[x]
    return s
    
        
#10 title()
def title1(x):
    result = ""
    capitalize1 = True
    for y in x:
        if ord(y) >= 97 and ord(y) <= 122:
            if capitalize1:
                y = chr(ord(y) - 32)
                capitalize1 = False
        elif y in [" ", "-", ""]:
            capitalize1 = True
        result += y

    return result

            