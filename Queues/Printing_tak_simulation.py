# Simulation of task being assigned to a printer and whether the printer is busy and what is the waiting time and so
# On any average day about 10 students are working in the lab at any given hour. 
# These students typically print up to twice during that time, and the length of these tasks ranges from 1 to 20 pages
# The printer in the lab is older, capable of processing 10 pages per minute of draft quality.
# The printer could be switched to give better quality, but then it would produce only five pages per minute.
# The slower printing speed could make students wait too long. What page rate should be used?

from Queue import Queue
import random
import pylab
class Printer:
    def __init__(self,ppm):
        self.pageRate=ppm
        self.currentTask=None
        self.timeRemaining=0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining-=1
            if self.timeRemaining<=0:
                self.currentTask=None

    def busy(self):
        if self.currentTask != None:
            return True
        else: 
            return False

    def startNext(self,newTask):
        self.currentTask=newTask
        self.timeRemaining=newTask.getPages()*60/self.pageRate

class Task:
    def __init__(self,time):
        self.timeStamp=time
        self.pages=random.randrange(1,21)

    def getStamp(self):
        return self.timeStamp

    def getPages(self):
        return self.pages

    def waitTime(self,currentTime):
        return currentTime-self.timeStamp

## Twenty tasks per hour means that on average there will be one task every 180 seconds, so if random num generated is 180 the a new task is created.
def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

def simulation(numSeconds,pagesPerMinute):
    labPrinter=Printer(pagesPerMinute)
    waitingTime=[]
    printQueue=Queue()

    for currentsecond in range(numSeconds):
        if newPrintTask():
            task=Task(currentsecond)
            printQueue.enqueue(task)

        if (not labPrinter.busy()) and (not printQueue.isEmpty()):
            nextTask=printQueue.dequeue()
            waitingTime.append(nextTask.waitTime(currentsecond))
            labPrinter.startNext(nextTask)

        labPrinter.tick()

    return sum(waitingTime)/len(waitingTime)
    #print("Average Wait %6.2f secs %3d tasks remaining."%(average,printQueue.size()))

def Trials(numTrial,ppm):
    averages=[]
    for i in range(numTrial):
        average=simulation(3600,ppm)
        averages.append(average)
        pylab.scatter(i,average)
    pylab.xlabel("num trials")
    pylab.ylabel("Waiting time")
    pylab.axhline(sum(averages)/numTrial)
    pylab.title ("Waiting time for {} trial for {} page per rate".format(numTrial,ppm))
    
    #return "Average Wait {} secs for {} pagerate.".format(average,ppm)
    
Trials(10,5)
pylab.figure()
Trials(10,10)
pylab.show()
