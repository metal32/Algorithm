# First in First out
# enqueue cost O(n) while pop cost O(1)
class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return "Item is {}".format(self.items[-1])

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

"""
q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
print q.size()
print q.dequeue()
print q.isEmpty()

"""