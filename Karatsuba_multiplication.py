## Theory behind it
## Normal n digit multiplication with n digit are of order (n^2)
## karatsuba algorithm reduces the time to O(n^1.59)
## it uses divide and conquer
## let the base be 10 so we can right n digit number into two x= (x1*(10^(n/2))+x0) :x1<- higher half, x0<- low half
## similarly y=(y1*(10^(n/2))+y0)  :y1<- high half and y0<- low half

## So now assume z0=x0*y0, z2=x1*y1, z1=(x0+x1)*(y0+y1)-z0-z2
## Z=z2*10^n + z1*10^(n/2) + z0
## S overall instead of taking 4 multiplication this algo using just three hence it is faster

## It is availble in gmpy package
import math
print('Karatsuba multiplication in Python of order complexity O(n^1.59)')
def karatsuba(x,y):
    x=str(x)
    y=str(y)
    len_x=len(x)
    len_y=len(y)
    if len_x==1 or len_y==1:
        return int(x)*int(y)
    else:
        exp1=int(math.ceil(len_x/2.0))
        exp2=int(math.ceil(len_y/2.0))
        if exp1>exp2:
            exp=exp2
        else:
            exp=exp1
        m1=len_x-exp
        m2=len_y-exp
        z2=karatsuba(int(x[0:m1]),int(y[0:m2]))
        z0=karatsuba(int(x[m1:len_x]),int(y[m2:len_y]))
        z1=karatsuba((int(x[m1:len_x])+int(x[0:m1])),(int(y[0:m2])+int(y[m2:len_y])))-z0-z2
        result=z2*math.pow(10,2*exp)+z1*math.pow(10,exp)+z0
        return int(result)
    

terminate=True
while terminate:
    x=raw_input()
    y=raw_input()
    print karatsuba(x,y)
    t=raw_input("input 0 to terminate: ")
    if t=='0':
        terminate=False

