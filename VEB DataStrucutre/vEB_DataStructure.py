'''
Created on 9-Mar-2017

@author: Ayush
@ Reference: CLRS and https://github.com/erikwaing/VEBTree/blob/master/VEB.py

'''

'''                                                           Van Embde Boas Trees Theory                                            '''
# VEB tree of any power 2 whether it is even or odd can be stored in this
# data-structure

import math


class VEB(object):

    def __init__(self, u):
        if u < 0:
            raise Exception(' u cannot be less than 0')
        self.u = 2
        while self.u < u:
            self.u = self.u * 2
        self.min = None
        self.max = None
        if u > 2:
            self.clusters = [
                None for _ in range(int(self.highroot(self.u)))]
            self.summary = None

    def lowroot(self, x):
        m = 1
        while 2**m < x:
            m += 1
        if m % 2 != 0:
            return math.sqrt(2**(m - 1))
        else:
            return math.sqrt(2**m)

    def highroot(self, x):
        m = 1
        while 2**m < x:
            m += 1
        if m % 2 != 0:
            return int(math.sqrt(2**(m + 1)))
        else:
            return int(math.sqrt(2**m))

    def __str__(self):
        return 'It\'s size is {} and max cluster is: {} and min cluster is: {}'.format(self.u, self.max, self.min)

    def high(self, x):
        return int(math.floor(x // self.lowroot(self.u)))

    def low(self, x):
        return int(x % self.lowroot(self.u))

    def index(self, x, y):
        return int(x * self.lowroot(self.u) + y)

    def emptyInsert(self, x):
        self.min = x
        self.max = x

    def insert(self, x):
        if self.min == None:
            self.emptyInsert(x)
        else:
            if x < self.min:
                self.min, x = x, self.min
            if self.u > 2:
                h = self.high(x)
                if self.clusters[h] == None:
                    self.clusters[h] = VEB(self.high(self.u))
                if self.summary == None:
                    self.summary = VEB(self.high(self.u))
                if self.clusters[h].min == None:
                    self.summary.insert(h)
                    self.clusters[h].emptyInsert(self.low(x))
                else:
                    self.clusters[h].insert(self.low(x))

            if x > self.max:
                self.max = x

    def member(self, x):
        if x == self.min or x == self.max:
            return True
        elif self.u <= 2:
            return False
        else:
            cluster = self.clusters[self.high(x)]
            if cluster != None:
                return cluster.member(self.low(x))
            else:
                return False

    def successor(self, x):
        if self.u <= 2:
            if x == 0 and self.max == 1:
                return 1
            else:
                return None
        elif self.min != None and x < self.min:
            return self.min
        else:
            h = self.high(x)
            l = self.low(x)
            maxlow = None
            cluster = self.clusters[h]
            if cluster != None:
                maxlow = cluster.max
            if maxlow != None and l < maxlow:
                offset = cluster.successor(l)
                return self.index(h, offset)
            else:
                succ_cluster = None
                if self.summary != None:
                    succ_cluster = self.summary.successor(h)
                if succ_cluster == None:
                    return None
                else:
                    cluster2 = self.clusters[succ_cluster]
                    offset = 0
                    if cluster2 != None:
                        offset = cluster2.min
                    return self.index(succ_cluster, offset)

    def predecessor(self, x):
        if self.u <= 2:
            if x == 1 and self.min == 0:
                return 1
            else:
                return None
        elif self.max != None and x > self.max:
            return self.max
        else:
            h = self.high(x)
            l = self.low(x)
            minLow = None
            cluster = self.clusters[h]
            if cluster != None:
                minLow = cluster.min
            if minLow != None and l > minLow:
                offset = cluster.predecessor(l)
                return self.index(h, offset)
            else:
                pre_cluster = None
                if self.summary != None:
                    pre_cluster = self.summary.predecessor(h)
                if pre_cluster == None:
                    if self.min != None and x > self.min:
                        return self.min
                    else:
                        return None
                else:
                    cluster2 = self.clusters[pre_cluster]
                    offset = 0
                    if cluster2 != None:
                        offset = cluster2.max
                    return self.index(pre_cluster, offset)

    def delete(self, x):
        if self.min == self.max:
            self.min = None
            self.max = None
        elif self.u <= 2:
            if x == 0:
                self.min = 1
            else:
                self.min = 0
            self.max = self.min
        else:
            if x == self.min:
                if self.summary != None:
                    first_cluster = self.summary.min
                    offset = self.clusters[first_cluster].min
                    x = self.index(first_cluster, offset)
                    self.min = x
                else:
                    raise Exception(' Value is not in the structure')
            h = self.high(x)
            l = self.low(x)
            self.clusters[h].delete(l)
            if self.clusters[h].min == None:
                self.summary.delete(h)
                if x == self.max:
                    summary_max = self.summary.max
                    if summary_max == None:
                        self.max = self.min
                    else:
                        off = self.clusters[summary_max].max
                        self.max = self.index(summary_max, off)
            elif x == self.max:
                off = self.clusters[self.high(x)].max
                self.max = self.index(self.high(x), off)


if __name__ == '__main__':
    my_veb = VEB(32)
    arr = [2, 3, 4, 5, 7, 14, 15, 27, 29]
    for item in arr:
        my_veb.insert(item)

    print my_veb.member(27)
    print my_veb.member(7)
    my_veb.delete(2)
    print my_veb.min
    print my_veb.member(2)
