# Seriously drunk university student standing in the middle of the field. Takes step in any direction, if he does the same thing for 500 sec 
# then how far will he be from his previous position.

## Assumption, the student can go in only four direction i.e. North, South, East, West
import math
import random

class Location(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self,xc,yc):
        return Location(self.x+xc,self.y+yc)
    def getLocation(self):
        return self.x, self.y
    def getDist(self,other):
        ox,oy=other.getLocation()
        return math.sqrt((ox-self.x)**2+(oy-self.y)**2)
class Direction(object):
    possible=('N','S','E','W')
    def __init__(self,point):
        if point in self.possible:
            self.point=point
        else:
            raise ValueError('point is not in the assumed direction')
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
            raise ValueError('You have mentioned wrong direction')
    def getDirection(self):
        return self.point
class Field(object):
    def __init__(self,drunk,loc):
        self.drunk=drunk
        self.loc=loc
    def move(self,cp,dist):
        oldLoc=self.loc
        xc,yc=cp.move(dist)
        self.loc=oldLoc.move(xc,yc)
    def getLoc(self):
        return self.loc
    def getDrunk(self):
        return self.drunk
class Drunk(object):
    def __init__(self,name):
        self.name=name
    def move(self,field,time=1):
        for i in range(time):
            pt=Direction(random.choice(Direction.possible))
            field.move(pt,1)

def PerformanceTrial(time,f):
    start=f.getLoc()
    distances=[]
    for i in range(time+1):
        f.getDrunk().move(f)
        end=f.getLoc()
        distance=end.getDist(start)
        distances.append(distance)
    return distances

drunk=Drunk('Ayush Mittal')
field=Field(drunk,Location(0.0,0.0))
Distances=PerformanceTrial(500,field)
print Distances
