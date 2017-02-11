# Maximum subset pairwise not divisible by K problem in order of complexicity O(n)
import math
f=open('test7.txt','r')
n,k=map(int,f.readline().split())
line=[]
for q in f.readlines():
    line.append(map(int,q.split()))
arr=line[0]
subset=[]
# Counts the number of times elemet x got repeated in alist 
def count(alist,x):
    return len([i for i in alist if int(i)==x])

#Retrurns the indices where the element x is located in alist
def index(alist,x):
    return [i for i in range(len(alist)) if alist[i]==x]

# Make and array of modulus of k
r=[]
for i in range(n):
    r.append(arr[i]%k)

# Range of elements in r is (0,k-1) so max sum of two elements in r is 2(k-1).
# Now if sum of two numbers in array r will be equal to k then they can't be added in the subset.
# For making the sum equal to k, one number has to be smaller than k/2 and other larger than k/2. 
# So we will select only one out of them whichever having more number of occurences in r.
# So we are evaluating the k from 1 to ceil[k/2]-1 and using one of the either elements i.e either 1 or k-1, 2 or k-2..........

for j in range(1,int(math.ceil(k/2.0))):
    if count(r,j)>=count(r,k-j):
        indices=index(r,j)
        for m in indices:
            subset.append(arr[m])
    else:
        indices=index(r,k-j)
        for m in indices:
            subset.append(arr[m])
#We can only add one element having remainder 0
#add one (r,0) if there it exist such element in r
indices=index(r,0)
if len(indices)>0:
    subset.append(arr[indices[0]])

# Now when k is even we can't add all the elements having modulus k/2 since two elements having modulus k/2 will sum up to k
if k%2==0:
    indices=index(r,k/2)
    subset.append(arr[indices[0]])
print len(set(subset))


            
    
        
    



