from math import sqrt
'''La idea con este problema es aprovecharnos de lo que hicimos en el ejercicio 1.
Si L es la lista de puntos y p el punto a revisar, entonces podemos calcular la 
envolvente convexa de L union p y ver si coincide con L. Si lo hace, entonces el punto
es interior. De lo contrario, esta fuera pues se necesita modificar la envolvente para tener convexidad.'''

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

def testPointInPolygon(vertx, verty, point_x, point_y):
    points = [(point_x,point_y)]
    new_points = []
    for i in range(len(vertx)):
        points.append((vertx[i],verty[i]))
        new_points.append((vertx[i],verty[i]))
    return convexhull(points) == new_points
