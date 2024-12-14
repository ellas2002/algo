import math

hull = set()

#finding the determinant
#general equation: ax*by + cx*ay + bx*cy - cx*by - bx*ay - ax*cy
def determinant(a, b, c):
    x, y = a
    x2, y2 = b
    x3, y3 = c
    return (x * y2) + (x3 * y) + (x2 * y3) - (x3 * y2) - (x2 * y) - (x * y3)


#wanted to create my own dot product instead of taking from numpy
def dot_product(a, b):
    dp = 0
    for i in range(len(a)):
        dp += a[i] * b[i]

    return dp


#calculates the vector
def vector_calculation(v1, v2):
    return (v1[0] - v2[0]), (v1[1] - v2[1])


#returns the length of the vector
def magnitude(v1):
    return math.sqrt(v1[0] ** 2 + v1[1] ** 2)


#calcualtes angle using cosine dot product formula
# v ⋅ w = ∥v∥ ∥w∥ cosθ
def angle(a, b, points):
    v1 = vector_calculation(a, b)
    v2 = vector_calculation(points, b)

    dp = dot_product(v1, v2)

    v1_m = magnitude(v1)
    v2_m = magnitude(v2)

    angles = math.acos(dp / v1_m * v2_m)
    return angles


#if the determinant of c is positive, then it is left of the line
def points_to_left(a, b, points):
    return [c for c in points if determinant(a, b, c) > 0]

#distance equation!!
def find_distance(a,b, c):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (c[2] - c[2]) ** 2)


def find_hull(points, p1, p2):
    #empty check
    if not points:
        return []

    # Find the farthest point from line p1 to p2
    farthest_point = max(points, key=lambda p: abs(determinant(p1, p2, p)))

    # Divide into subsets left of p1->farthest_point and farthest_point->p2
    subset1 = points_to_left(p1, farthest_point, points)
    subset2 = points_to_left(farthest_point, p2, points)

    return find_hull(subset1, p1, farthest_point) + [farthest_point] + find_hull(subset2, farthest_point, p2)


#Main QuickHull algorithm
def quickhull(points):

    if len(points) < 3:
        return points

    min_point = min(points, key=lambda p: p[0]) #find min points
    max_point = max(points, key=lambda p: p[0]) # max


    left_set = points_to_left(min_point, max_point, points) #left split
    right_set = points_to_left(max_point, min_point, points) # right split

    # Construct the hull
    upper_hull = find_hull(left_set, min_point, max_point)
    lower_hull = find_hull(right_set, max_point, min_point)

    return [min_point] + upper_hull + [max_point] + lower_hull

