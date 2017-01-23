#In this the drunk guy has little biasedness of going more on the north side as compare to the south side or any ther side in general
# The code is very much similar to the random walk except the class Drunk

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
        return self.x, self.y
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
    def isChute(self):
        x,y=self.loc.getCoords()
        return abs(x)-abs(y)==0

class OddField(Field):
    def ischute(self):
        x,y=self.loc.getCoords()
        return abs(x)-abs(y)==0
    def move(self, cp, dist):
        Field.move(self,cp,dist)
        if self.ischute():
            self.loc=Location(0,0)

class Drunk(object):
    def __init__(self,name):
        self.name=name
    def move(self, field, pt, dist=1):
        if field.getDrunk() != self:
            raise ValueError("Drunk, move is called with drunk not in field")
        for i in range(dist):
            field.move(pt,1) 

class UsualDrunk(Drunk):
    def move(self, field, dist=1):
        pt=random.choice(Direction.possibles)
        Drunk.move(self,field,Direction(pt),dist)

class ColdDrunk(Drunk):
    def move(self, field, dist=1):
        pt=random.choice(Direction.possibles)
        if pt=='S':
            Drunk.move(self,field,Direction(pt),2*dist)
        else:
            Drunk.move(self,field,Direction(pt),dist)

class EWDrunk(Drunk):
    def move(self, field, dist=1):
        pt=random.choice(Direction.possibles)
        while pt!='E'and pt!='W':
            pt=random.choice(Direction.possibles)
        Drunk.move(self,field,Direction(pt),dist)



def PerformanceTrial(time, f):
    start=f.getLoc()
    distances=[0.0]
    locs=[]
    for t in range(1,time+1):
        f.getDrunk().move(f)
        newLoc=f.getLoc()
        distance=float(format(newLoc.getDist(start),'.2f'))
        distances.append(distance)
        locs.append(newLoc)
    return distances,locs
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
def PerformTrialTest(time,numTrials,drunkType):
    distLists=[]
    locLists=[]
    for trial in range(numTrials):
        d=drunkType('Drunk' + str(trial))
        f=OddField(d,Location(0,0))
        distances, Locs = PerformanceTrial(time,f)
        distLists.append(distances)
        locLists.append(Locs)
    return distLists, locLists
#distlists= PerformTrialTest(500,100)
def ansQuest(maxTime,numTrial,drunkType,title):
    means=[0.0]
    distLists, locLists=PerformTrialTest(maxTime,numTrial,drunkType)
    for t in range(1,maxTime+1):
        tot=0.0
        for list in distLists:
            tot=tot+list[t]
        means.append(tot/len(distLists))  
    pylab.figure()
    pylab.plot(means)
    pylab.xlabel('Steps')
    pylab.ylabel('Distance from origin')
    pylab.title(title)
    lastx=[]
    lasty=[]
    for locList in locLists:
        x,y=locList[-1].getCoords()
        lastx.append(x)
        lasty.append(y)
    pylab.figure()
    pylab.scatter(lastx,lasty)
    pylab.xlabel('EW Distance')
    pylab.ylabel('NS Distance')
    pylab.title(title+' Final Locations')
    pylab.figure()
    pylab.hist(lastx)
    pylab.xlabel('EW Value')
    pylab.ylabel('Number of trials')
    pylab.title(title+' Distribution of Final EW value')


#firstTest()
numTrials=300

ansQuest(500,numTrials,UsualDrunk,'Usual Drunk '+str(numTrials)+' Trials')

#ansQuest(500,numTrials,ColdDrunk,'Cold Drunk '+str(numTrials)+' Trials')

#ansQuest(500,numTrials,EWDrunk,'EW Drunk '+str(numTrials)+' Trials')
pylab.show()