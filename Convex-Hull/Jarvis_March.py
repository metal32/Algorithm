"""              Convex hull(2D) - Smallest convex polygon containing all points in O(n*h) also know as gift-wrapping algo                  """

# JARVIS MARCH
# We have to select a leftmost extreme point p and then select q such that pqr makes a counter-clockwise turn, i.e. left turn
# So below function will return positive value for left turn, negative value for right turn and zero if all of them are collinear.

def turn(p,q,r):
    return cmp((q[0]-p[0])*(r[1]-p[1])-(r[0]-p[0])*(q[1]-p[1]),0)

# return 1 for left turn, -1 for right turn and 0 for collinear

def _dist(p,q):
    dx,dy=p[0]-q[0],p[1]-q[1]
    return dx*dx+dy*dy

# Now if three points are collinear we need to select the point which is farthest from p so calculate the distance

def _nextHull(points,p):
    q=p
    for r in points:
        t=turn(p,q,r)
        if t==-1 or t==0 and _dist(p,r)>_dist(p,q):
            q=r
    return q

def convexHull(points):
    hull=[min(points)]
    for p in hull:
        q=_nextHull(points,p)
        if q!=hull[0]:
            hull.append(q)
    return hull

import numpy as np
import matplotlib.pyplot as plt
points = [(np.random.randint(0,200),np.random.randint(0,200)) for i in range(25)]

#points=[(0, 3), (1, 1), (2, 2), (4, 4),(0, 0), (1, 2), (3, 1), (3, 3)]

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
