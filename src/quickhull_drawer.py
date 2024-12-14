from quickhull import quickhull
import random
import matplotlib.pyplot as plt


points = [(random.randint(0, 99), random.randint(0, 99)) for _ in range(50)]
x = [x for x, _ in points]
y = [y for _, y in points]
hull = quickhull(points)

plt.scatter(x, y)
for a, b in zip(hull, hull[1:] + hull[0:1]):
    plt.plot([a[0], b[0]], [a[1], b[1]], c='k')
plt.show(block=True)
exit()