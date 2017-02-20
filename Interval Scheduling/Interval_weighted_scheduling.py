import time
from datetime import datetime
import bisect
import collections

class Interval(object):
    def __init__(self,title,start,finish):
        self.title=title
        self.start=int(time.mktime(datetime.strptime(start,'%d %b, %y').timetuple()))
        self.finish=int(time.mktime(datetime.strptime(finish,'%d %b, %y').timetuple()))
        self.weight=self.finish-self.start

    def __str__(self):
        return str((self.title, self.start, self.finish))


def compute_previous_intervals(I):
    ''' For every interval j compute the compatible intervals i, where i<j
        we are computing all the right most interval before j in which the Sj>=Fi
    '''
    ''' I is a sorted list of Intervals instances, sorted on the basis of their finish time'''

    start=[i.start for i in I]
    finish=[i.finish for i in I]

    p=[]
    for j in xrange(len(I)):
        # The right most point for j
        # This bisection will take O(logn) for 1 j and so overall O(nlogn)
        # rightmost interval f_i <= s_j
         i=bisect.bisect_right(finish,start[j])-1
         p.append(i)
    return p

def schedule_weighted_interval(I):
    ''' Sort I on their Finish Time O(nlogn)'''

    I.sort(lambda x,y: x.finish-y.finish)
    p=compute_previous_intervals(I)

    ## Maximum sum of weights is OPT(j) for j interval {1,2...j}
    ## Now we have to guess whether j interval belongs to potimal solution or not

    OPT=collections.defaultdict(int)
    OPT[0]=0
    for j in range(1,len(I)):
        OPT[j]=max(I[j].weight+OPT[p[j]],OPT[j-1])

    O = []
    def compute_solution(j):
        if j >= 0:  # will halt on OPT[-1]
            if I[j].weight + OPT[p[j]] > OPT[j - 1]:
                O.append(I[j])
                compute_solution(p[j])
            else:
                compute_solution(j - 1)
    compute_solution(len(I) - 1)

    return O
I=[]
I.append(Interval("Summer School" , "14 Jan, 13", "24 Feb, 13"))
I.append(Interval("Semester 1" , "1 Mar, 13", "4 Jun, 13"))
I.append(Interval("Semester 2" , "18 Aug, 13", "24 Nov, 13"))
I.append(Interval("Trimester 1" , "22 Mar, 13", "16 May, 13"))
I.append(Interval("Trimester 2" , "22 May, 13", "24 Jul, 13"))
I.append(Interval("Trimester 3" , "28 Aug, 13", "16 Nov, 13"))
O = schedule_weighted_interval(I)
for i in O:
    print i
