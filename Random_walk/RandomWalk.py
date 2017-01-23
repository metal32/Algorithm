# Seriously drunk university student standing in the middle of the field. Takes step in any direction, if he does the same thing for 500 sec 
# then how far will he be from his previous position.

## Assumption, the student can go in only four direction i.e. North, South, East, West
import math
import random
import pylab
class Location(object):   ## caluculating new coordinates and calculate the distance in two dimensional coordinates
    def __init__(self,x,y):
        self.x=float(x)
        self.y=float(y)
    def move(self,xc,yc):
        return Location(self.x+float(xc),self.y+float(yc))
    def getCoords(self):
        return self.x,self.y
    def getDist(self,other):
        ox, oy= other.getCoords()
        xDist=self.x-ox
        yDist=self.y-oy
        return math.sqrt(xDist**2+yDist**2)
class Direction(object):   ## To know the direction in which the person will move
    possibles=('N','S','E','W')
    def __init__(self, point):
        if point in self.possibles:
            self.point=point
        else:
            raise ValueError(" in Direction.__init__")
    def move(self,dist):
        if self.point=='N':
            return (0,dist)
        elif self.point=='S':
            return (0,-dist)
        elif self.point=='E':
            return (dist,0)
        elif self.point=='W':
            return (-dist,0)
        else:
            raise ValueError(" in direction.move")
class Field(object):  ## Store the old and new coordinates
    def __init__(self,drunk,loc):
        self.drunk=drunk
        self.loc=loc
    def move(self, cp, dist):
        oldloc=self.loc
        xc, yc=cp.move(dist)
        self.loc=oldloc.move(xc,yc)
    def getLoc(self):
        return self.loc
    def getDrunk(self):
        return self.drunk
class Drunk(object):
    def __init__(self,name):
        self.name=name
    def move(self, field, time=1):
        if field.getDrunk() != self:
            raise ValueError("Drunk, move is called with drunk not in field")
        for i in range(time):
            pt= Direction(random.choice(Direction.possibles))
            field.move(pt,1) 
def PerformanceTrial(time, f):
    start=f.getLoc()
    distances=[0.0]
    for t in range(1,time+1):
        f.getDrunk().move(f)
        newLoc=f.getLoc()
        distance=float(format(newLoc.getDist(start),'.2f'))
        distances.append(distance)
    return distances
def firstTest():
    drunk=Drunk('Homer Simpson')
    for i in range(3):
        f=Field(drunk,Location(0,0))
        distances=PerformanceTrial(1,f)
        pylab.plot(distances)
    pylab.title('Homer\'s Random walk')
    pylab.xlabel('Time')
    pylab.ylabel('Distance from origin')

    pylab.show()
def PerformTrialTest(time,numTrials):
    distLists=[]
    for trial in range(numTrials):
        drunk=Drunk('Homer Simpson' + str(trial))
        f=Field(drunk,Location(0,0))
        distances=PerformanceTrial(time,f)
        distLists.append(distances)
    return distLists
#distlists= PerformTrialTest(500,100)
def ansQuest(maxTime,numTrial):
    means=[0.0]
    distLists=PerformTrialTest(maxTime,numTrial)
    for t in range(1,maxTime+1):
        tot=0.0
        for list in distLists:
            tot=tot+list[t]
        means.append(tot/len(distLists))  
    pylab.figure()
    pylab.plot(means)
    pylab.xlabel('Time')
    pylab.ylabel('Distance from origin')
    pylab.title('Avg distance vs time ('+str(len(distLists))+' trials)')
#firstTest()
ansQuest(1,5)
pylab.show()


