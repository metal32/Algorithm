### DECISION TREE- DEPTH FIRST LEFT FIRST, Complexicity(2**n), without dynamic programming
### With dynamic programming the complexicity comes into the form of pseudopolynomial, i.e. O(n*S)
### You arre given weiht and value of 3 objects with a constraing of maximum weight you can carry, so you have to find the maximum vaue.
w=[1,5,3,4,5,6,2,3,4]
v=[15,10,9,23,10,4,7,19,10]
#Constrain is that maximum weight you can carry is 10 only.

## With memorization 
def fastmaxVal(w,v,i,aw,m):
    global numCalls
    numCalls+=1
    try: return m[(i,aw)]
    except KeyError:
        if i==0:
            if w[i]<=aw:
                m[(i, aw)] = v[i]
                return v[i]
            else: 
                m[(i, aw)] = 0
                return 0
        without_i=fastmaxVal(w,v,i-1,aw,m) 
        if w[i]>aw:
            m[(i,aw)] = without_i
            return without_i
        else:
            with_i=v[i]+fastmaxVal(w,v,i-1,aw-w[i],m)
            res=max(without_i,with_i)
            m[(i,aw)]=res
        return res
def maxVal(w,v,i,aw):
    m={}
    return fastmaxVal(w,v,i,aw,m)
numCalls=0
print maxVal(w,v,len(w)-1,10)


"""
def maxVal(w,v,i,aw):
    print "maxval called with i ",i," and ",aw
    global numCalls
    numCalls+=1
    if i==0:
        if w[i]<=aw:
            return v[i]
        else: return 0
    without_i=maxVal(w,v,i-1,aw)
    print i
    if w[i]>aw:
        return without_i
    else:
        with_i=v[i]+maxVal(w,v,i-1,aw-w[i])
    return max(without_i,with_i)
numCalls=0
r=maxVal(w,v,len(w)-1,8)
print "The maximum value earned ",r," in number of calls ",numCalls
"""