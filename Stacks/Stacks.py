# Last in First out
class Stack:
    def __init__(self):
        self.items=[]

    def __str__(self):
        return self.items

    def push(self,key):
        self.items.append(key)

    def isEmpty(self):
        return self.items==[]

    def pop(self):
        return self.items.pop()

    def peep(self):
        return self.items[len(self.items)-1]

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