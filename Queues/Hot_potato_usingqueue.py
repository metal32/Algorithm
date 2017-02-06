from Queue import Queue
def hotPotato(namelist, num):
    sim = Queue()
    for name in namelist:
        sim.enqueue(name)
    while sim.size()>1:
        for i in range(num):
            sim.enqueue(sim.dequeue())
        sim.dequeue()

    return sim

namelist=['Rishabh','Ayush','Ashish','Chaman','Viraj','Kunal','Kansal']
num=4
print hotPotato(namelist,num)
