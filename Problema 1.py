from math import sqrt

def crossProduct(p1,p2):
    return p1[0]*p2[1] - p1[1]*p2[0]

def direction(origin, point1, point2):  #usaremos el producto cruz
#si direction < 0, entonces el vetor esta a la izquierda. Si es >0, derecha. Colineales es nulo.
    v1 = (point1[0] - origin[0], point1[1] - origin[1])
    v2 = (point2[0] - origin[0], point2[1] - origin[1])
    return crossProduct(v1,v2)

def distance(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    return sqrt(x**2+y**2)

def convexhull(points):
    ordered = sorted(points)
    a = min(ordered)
    index = points.index(a)

#l sera el vertice actual, el que esta siendo analizado
    l = index
    hull = []
    hull.append(a)
    while True:
        q = (l+1) % len(points)
        for i in range(len(points)):
            if i == 1:
                continue
            d = direction(points[l],points[i],points[q])
            if d < 0 or (d==0 and distance(points[i],points[l]) > distance(points[q],points[l])):
                q = i
        l = q
        if l == index:
            break
        hull.append(points[q])
    return hull

#hay que hallar el radio de la envolvente convexa

def union(set1,set2):
    for i in set2:
        set1.append(i)
    return set1

def maxradii(set):
    values = []
    for i in range(len(set)):
        for j in range(i+1,len(set)):
            values.append(distance(set[i],set[j]))
    return max(values)

def hausdorffDistance(set1,set2):
    uni = union(set1,set2)
    set = convexhull(uni)
    return maxradii(set)

print(hausdorffDistance([(0,0),(1,1)],[(0,0),(1,-1)]))

#para explicacion en clase:
#https://algorithmtutor.com/Computational-Geometry/Convex-Hull-Algorithms-Jarvis-s-March/