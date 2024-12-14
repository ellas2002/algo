import math
class Distance:

    def distance(point):
        d = math.sqrt(abs(point[0] - point[0]) + abs(point[1] - point[1]))
        return d

    def closer(points):
        if len(points) < 2:
            raise ValueError("nope")

        close_pair = None
        min_distance = float("inf")

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                d = distance(points[i], points[j])

                if d <  min_distance:
                    min_distance = d
                    close_pair = p1, p2

            return close_pair, min_distance



