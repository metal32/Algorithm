# Last in First out
class Stack:
    def __init__(self):
        self.items=[]
        self.max=0

    def __str__(self):
        return self.items

    def push(self,key):
        self.items.append(key)
        if key>self.max:
            self.max=key

    def isEmpty(self):
        return self.items==[]

    def pop(self):
        top=self.items.pop()
        if top==self.max:
            if len(self.items)>0:
                self.max=max(self.items)
            else:
                self.max=0
        return top

    def peep(self):
        return self.items[len(self.items)-1]

    def getMax(self):
        return self.max

"""
s=Stack()
print s.isEmpty
print "\n"

s.push(4)
s.push("DOG")
print s.peep()
print "\n"

s.push('CAT')

print s.pop()
print "\n"

print s.peep()

"""