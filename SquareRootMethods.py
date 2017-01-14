"""Calculating square root
   First method is shown for calculating perfect square roots.
"""
#def square_root(x):
    ###Return the square root of x, if x has a perfect square root.
#    ans=0
#    if (x>0) :
#        while(ans*ans<x):
#            ans+=1
#        if (ans*ans!=x):
#            print "The number doesn't has a perfect square root"
#            return None
#        else:
#            print "The square root for {} is {}.".format(x,ans)
#            return ans
#   else: 
#        print "Number is non-negative integer"
#        return None
#square_root(64)

"""Second Method to calculate square root of any number by Bisection method"""
#import math
#def squareRootBi(x):
#    assert x>=0
#    epsilon=0.0001
#    low=0
#    high=max(x,1.0)  ## If x is less than 1 then square rootof x will be greater than x so high bound should be higher than x but less than 1.
#    guess=(high+low)/2.0
#    ctrl=1
#    while abs(guess**2-x)>epsilon and ctrl<500:
#        if guess**2<x:
#            low=guess
#        else:
#            high=guess
#        guess=(low+high)/2.0
#        ctrl +=1
#    print "By using this method the square root of {} is {} in {} guess.".format(x,guess,ctrl)
#squareRootBi(math.pi)

"""Third Method to calculate square root of any number by Newton's method"""
def squareRootNr(x):
    assert x>=0
    epsilon=0.0001
    ## If x is less than 1 then square rootof x will be greater than x so high bound should be higher than x but less than 1.
    guess=float(x/2.0)
    diff=guess**2-x
    ctrl=1
    while abs(diff)>epsilon and ctrl<500:
        guess=guess - diff/(2*guess)
        diff=guess**2-x
        ctrl+=1
    print "By using this method the square root of {} is {} in {} guess.".format(x,guess,ctrl)
squareRootNr(10)