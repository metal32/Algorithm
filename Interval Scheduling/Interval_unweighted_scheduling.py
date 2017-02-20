""" http://farazdagi.com/blog/2013/weighted-interval-scheduling/ """
# Greedy algorithm is a myopic algorithm that processes the input one piece at a time with no apparent look-ahead.
# Greedy Interval Scheduling
# STEP1: Use a simple rule to select a request i.
# STEP2: Reject all requests that are incompatible with i.
# Repeat to step 1 and step 2

## For rule: shortest and numerical doesn't work
## This also doesn't work: Find the number of incompatible request for each request and then select the request with the least incompatible requests.

## Complexicity is for sorting O(nlogn) and for selection is O(n) so overall complexicity is O(nlogn)


import time
from datetime import datetime

class Interval(object):
    def __init__(self,title,start,finish):
        self.title=title
        self.start=int(time.mktime(datetime.strptime(start,'%d %b, %y').timetuple()))
        self.finish=int(time.mktime(datetime.strptime(finish,'%d %b, %y').timetuple()))

    def __str__(self):
        return str((self.title, self.start, self.finish))

 
def schedule(I):
    I.sort(lambda x,y: x.finish-y.finish)
    o=[]
    finish=0
    for i in I:
        if finish<=i.start:
            finish=i.finish
            o.append(i)
    return o

I=[]
I.append(Interval("Summer School" , "14 Jan, 13", "24 Feb, 13"))
I.append(Interval("Semester 1" , "1 Mar, 13", "4 Jun, 13"))
I.append(Interval("Semester 2" , "18 Aug, 13", "24 Nov, 13"))
I.append(Interval("Trimester 1" , "22 Mar, 13", "16 May, 13"))
I.append(Interval("Trimester 2" , "22 May, 13", "24 Jul, 13"))
I.append(Interval("Trimester 3" , "28 Aug, 13", "16 Nov, 13"))
O=schedule(I)
for i in O:
    print i


