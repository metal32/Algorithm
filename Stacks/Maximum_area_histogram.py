# Maximu area in a histogram
class Stack:
    def __init__(self):
        self.items=[]
        self.size=0

    def __str__(self):
        return self.items

    def push(self,key):
        self.size+=1
        self.items.append(key)

    def isEmpty(self):
        return self.size==0

    def pop(self):
        self.size-=1
        top=self.items.pop()
        return top

    def peep(self):
        return self.items[len(self.items)-1]

heights=[2,2,4,1,4,5,2,1,1,3]

def tem_area(S,heights,i,top):
    if S.isEmpty():
        return heights[top]*i
    else:
        return heights[top]*(i-S.peep()-1)


def max_area(heights):
    n=len(heights)
    maxarea=-1
    area=0
    S=Stack()
    S.push(0)
    i=1
    while i<n:
        k=i
        while k>=0 and heights[k-1]>heights[i] and (not S.isEmpty()):
            top=S.pop()
            area=tem_area(S,heights,i,top)
            if maxarea<area:
                maxarea=area
            k-=1
        S.push(i)
        i+=1
    while not S.isEmpty():
        top=S.pop()
        area=tem_area(S,heights,i,top)
        if maxarea<area:
            maxarea=area
    return maxarea

print max_area(heights)

