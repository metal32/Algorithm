import math
class VEB(object):
    def __init__(self,u):
        if u<0:
            raise Exception ('u cannot be less than 0')
        self.u=2
        while self.u<u:
            self.u*=self.u
        self.min=None
        self.max=None
        if u>2:
            self.clusters=[None for i in range(self.high(self.u))]
            self.summary=None

    def high(self,x):
        return int(math.floor(x/math.sqrt(self.u)))

    def low(self,x):
        return (x%math.ceil(math.sqrt(self.u)))

    def index(self,x,y):
        return int((x*math.floor(math.sqrt(self.u)))+y)

    def emptyInsert(self,x):
        self.min=x
        self.max=x

    def insert(self,x):
        if self.min==None:
            self.emptyInsert(x)
        else:
            if x<self.min:
                self.min,x=x,self.min
            if self.u>2:
                h=self.high(x)
                if self.clusters[h]==None:
                    self.clusters[h]=VEB(self.high(self.u))
                if self.summary == None:
                    self.summary=VEB(self.high(self.u))
                if self.clusters[h].min==None:
                    self.summary.insert(h)
                    self.clusters[h].emptyInsert(self.low(x))
                else:
                    self.clusters[h].insert(self.low(x))
            if x>self.max:
                self.max=x
                  
    def successor(self,x):
        if self.u<=2:
            if x==0 and self.max==1:
                return 1
            else:
                return None
        elif self.min!=None and x<self.min:
            return self.min
        else:
            h=self.high(x)
            l=self.low(x)
            maxLow=None
            clusters=self.clusters[h]
            if clusters!=None:
                maxLow=cluster.max
            if maxLow!=None and l<maxLow:
                offset=cluster.successor(l)
                return self.index(h,offset)
            else:
                succ_cluster=None
                if self.summary!=None:
                    succ_cluster=self.summmary.successor(h)
                if succ_cluster == None:
                    return None
                else:
                    cluster2=self.clusters[succ_cluster]
                    offset=0
                    if cluster2 != None:
                        offset=cluster2.min
                    return self.index(succ_cluster,offset)


    def predecessor(self,x):
        if self.u<=2:
            if x==0 and self.max==1:
                return 1
            else:
                return None
        elif self.max!=None and x>self.max:
            return self.max
        else:
            h=self.high(x)
            l=self.low(l)
            minLow=None
            cluster=self.clusters[h]
            if self.clusters != None:
                minLow=cluster.min
            if minLow!=None and minLow<l:
                offset=cluster.predecessor(l)
                if offset == None:
                    offset=0
                return self.index(h,offset)
            else:
                pred_cluster=None
                if self.summary!=None:
                    pred_cluster=self.summary.predecessor(h)
                if pred_cluster == None:
                    if self.min != None and x>self.min:
                        return self.min
                    else:
                        return None
                else:
                    cluster=self.clusters[pred_cluster]
                    offset=0
                    if cluster2!=None:
                        offset=cluster2.max
                    return self.index(pred_cluster,offset)

    def delete(self,x):
        if x==self.min:
            # Finding new min
            i=self.summary.min
            if i==None:
                self.min=None
                self.max=None
                return
            self.min=self.index(i,self.clusters[i].min)
        # if x is not equal to self.min then we have to call the clusters and delete l index
        h=self.high(x)
        l=self.low(x)
        self.clusters[h].delete(l)
        if self.clusters[h].min==None:
            # Second call to delete the info from summary
            self.summary.delete(h)
        # If x equals to self.max
        if x==self.max:
            # If we deleted last second item i.e. only self.min is remaining
            if self.summary.max==None:
                self.max=self.min
            else:
                i=self.summary.max
                self.max=self.index(i,self.clusters[i].max)

