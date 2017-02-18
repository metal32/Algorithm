import sys
import math

paragraph="Tushar Roy likes to code"
words=paragraph.split()
n=len(words)
page_width=10 
justification_map={}
min_map={}
def total_length(str_arr):
    total=0
    for string in str_arr:
        total += len(string)

    total+=len(str_arr)-1 # to count the number of spaces
    return total

## making a function to calculate badness
# Badness is equal to infinity if total length is greater than the page width
# else for Latex it is (page_width-total length)**2

def badness(str_arr,page_width):
    line_len=total_length(str_arr)
    if line_len>page_width:
        return sys.maxint
    else:
        return math.pow(page_width-line_len,2)

def justify(i,n,words,page_width):
    if i==n:
        return 0
    ans=[]
    for j in range(i+1,n+1):
        ans.append(justification_map[j]+badness(words[i:j],page_width))
    min_map[i]=ans.index(min(ans))+1
    return min(ans)

for i in range(n,-1,-1):
    justification_map[i]=justify(i,n,words,page_width)

print "Minimum badness achieved {}".format(justification_map[0])
print justification_map

print min_map
key = 0
while(key <n):
    key = key + min_map[key]
    print key