# O(nlogn) due to sorting

def turn(p,q,r):
    return cmp((q[0]-p[0])*(r[1]-p[1])-(r[0]-p[0])*(q[1]-p[1]),0)

def _keepHull(hull,r):
    while len(hull)>1 and turn(hull[-2],hull[-1],r)!=1:
        hull.pop()
    if not hull or hull[-1]!=r:
        hull.append(r)
    return hull

def convexHull(points):
    # First wee sort the points in lexicographically order using x-coordinates and then y-coordinates
    # After that we create a lower hull and upper hull
    points=sorted(points)
    l=reduce(_keepHull,points,[])
    u=reduce(_keepHull,reversed(points),[])
    # First point of lower Hull is the last point in upper Hull and vice-versa
    l.extend(u[i] for i in range(1,len(u)-1))
    return l

import numpy as np
import matplotlib.pyplot as plt
points = [(np.random.randint(0,200),np.random.randint(0,200)) for i in range(25)]
point1=[x[0] for x in points]
point2=[x[1] for x in points]

final=convexHull(points)
final1=[x[0] for x in final]
final2=[x[1] for x in final]
final1.append(final[0][0])
final2.append(final[0][1])
plt.scatter(point1,point2,marker='v')
plt.plot(final1,final2,c='crimson')
plt.title(' Convax Hull ')
plt.show()

