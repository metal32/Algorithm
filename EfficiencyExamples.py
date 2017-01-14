"""CALCULATING EXPONENT BY USING BRUTE FORCE"""
""" METHOD 1 HAVING LINEAR BIG O time"""
#def exp(a,b):
#    ans=1
#    while(b>0):
#        ans=ans*a
#        b=b-1
#    return ans

""" METHOD 2 again having linear BIG O time"""
#def exp2(a,b):
#    if b==1:
#        return a
#    else:
#        return a*exp2(a,b-1)

""" METHOD 2 cutting linear BIG O time in half"""
#def exp3(a,b):
#    if b==1:
#        return a;
#    elif b%2==0:
#        return exp3(a*a,b/2)
#    else:
#        return a*exp3(a,b-1)
#
#print exp3(4,5)





