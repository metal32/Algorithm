""" SELECTION IN A SORTED LIST"""
#def search(s,e):
#    i=0
#    answer=None
#    count=0
#    while i<len(s) and answer==None:
#        count+=1
#        if e==s[i]:
#            answer=True
#        elif e<s[i]:
#            answer=False
#            print "The number is not present in the list"
#        i+=1
#    print answer, count

""" Binary search in a sorted list"""
#def biSearch(s,e,low,high):
#    if(high-low==1):
#        if s[high]==e or s[low]==e:
#            return True
#        else:
#            return False
#    else:
#        mid=(low+high)/2
#        if s[mid]==e:
#            return True
#        elif s[mid]>e:
#            return biSearch(s,e,low,mid-1)
#        elif s[mid]<e:
#            return biSearch(s,e,mid+1,high)
    

#s=range(1,10000,2)
#print biSearch(s,501,0,len(s)-1)
         

