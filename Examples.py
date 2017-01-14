""" FINDING THE PRIME NUMBER BETWEEN 1 AND 100"""

#non_prime={j*n for n in range(2,10) for j in range(2,100)}
#prime={x for x in range(2,100) if x not in non_prime}
#print prime

""" FINDING THE DIVISOR for any number"""
#x=100
#divisors=filter(lambda j: x%j==0, range(1,x))
#print divisors

""" Finding the sum of digit"""
#x=23456
#def sum_of_digit(x):
#    sum_digit=0
#    for n in str(x): #Converted the digit into a string as string behaves in a order sequence
#        sum_digit += int(n) # now converted the index 0 value of the string back to integer so that we can do airthmentic operation in it.
#    print sum_digit    


"""Farmyard Problem
 20 heads and 56 legs
 Find out, how many chickes and how many pigs are there in the farm? 
"""
"""
def solve(numHeads,numLegs):
    for numChicks in range(numHeads+1):
        numPigs=numHeads-numChicks
        totLegs=4*numPigs+2*numChicks
        if (numLegs==totLegs):
            return [numPigs,numChicks]
    return [None,None]
def farm():
    heads=int(raw_input("Enter total number of heads "))   
    legs=int(raw_input("Enter total number of legs "))   
    Pigs,Chickens,Spiders=solve1(heads,legs)
    if Pigs==None:
        print "There is no solution"
    else:
        print "The solution for the given problem is, {} number of Pigs, {} number of Chickens and {} number of spiders are in the farm.".format(Pigs,Chickens,Spiders)

## IF we add spiders too in the farm, now what will be the solution
def solve1(numHeads,numLegs):
    for numSpiders in range(0,numHeads+1):
        for numChicks in range(0,numHeads-numSpiders+1):
            numPigs=numHeads-numChicks-numSpiders
            totLegs=4*numPigs+2*numChicks+8*numSpiders
            if (totLegs==numLegs):
                return [numPigs,numChicks,numSpiders]
    return [None,None,None]      

farm()

"""

"""
RECURSIVE PROGRAMMING EXAMPLE
EXP:1 PALINDROME
num=[1,2,3,4,5,4,3,2,1]
NUM IS PALINDROME

EXP:2 Fibonacci
"""

""" ##Example 1
def isPalindrome(s):
    if len(s)<=1:
        return True
    else: 
        return s[0]==s[-1] and isPalindrome(s[1:-1]) # we are checking the first and last number whether they are equal or not and after that reducing the list by removing the last number
print isPalindrome('abcdcba')
"""

 ##Example 2
def isFibonacci(n):
    global numCalls
    numCalls+=1
    if n==0 or n==1:
        return 1
    else: return isFibonacci(n-1)+isFibonacci(n-2)
numCalls=0
print isFibonacci(20), numCalls 



###EXAMPLE 3: FAST FIBONNACI
### In this we will store the valuse of the number whose Fibonnaci we have already calculated so instrad of calculating the fibonnaci 
### of the same number more than once, as it is in recursive programming, we will just reccover it from the memory.

def fastfib(n,memo): ##memo is a dictionary which has both n<- number and it's fibonnaci value too.
    global numcalls
    numcalls +=1
    if n not in memo:
        memo[n]=fastfib(n-1,memo)+fastfib(n-2,memo)
    return memo[n]
def fib(n):
    memo={0:1,1:1}
    return fastfib(n,memo)
numcalls=0
print fib(20),numcalls

"""
def fact(n):
    # Recursive factorial definition
    if n < 0:
        # Just a check to make sure we don't call (-n)!
        return "Error - cannot accept neg numbers."
    elif n == 0:
        # Base case: 0! = 1
        return 1
    else:
        # Recursive case: n! = n*(n-1)!
        return n * fact(n-1)
print fact(10)
"""