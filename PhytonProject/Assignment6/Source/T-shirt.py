import numpy as np
import matplotlib.pyplot as plt

c1 = None
c2 = None
c3 = None


sizes = np.array([11, 12, 21, 22, 23, 25, 27, 28, 32, 34, 36, 42, 39, 46, 48, 54])

sizeWeight = np.array([35, 14, 24, 53, 64, 32, 22, 23, 43, 23, 54, 23, 54, 23, 55, 53])

plt.scatter(sizes, sizeWeight)
plt.show()


center1 = 20
center2 = 40
center3 = 60


C1 = center1
C2 = center2
C3 = center3

i = 0
while C1 != c1 or C2 != c2 or C3 != c3:
    i = i+1
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for x in sizes:
        distance1 = abs(C1 - x)
        distance2 = abs(C2 - x)
        distance3 = abs(C3 - x)
        if distance1 < distance2 and distance1<distance3:
                cluster1.append(x)
                Distance1 = "(%.1f)" % distance1
                Distance2 = "%.1f" % distance2
                Distance3 = "%.1f" % distance3
        elif distance2 < distance3 and distance2<distance1:
                cluster2.append(x)
                Distance1 = "(%.1f)" % distance1
                Distance2 = "%.1f" % distance2
                Distance3 = "%.1f" % distance3
        else:
                cluster3.append(x)
                Distance1 = "%.1f" % distance1
                Distance2 = "(%.1f)" % distance2
                Distance3 = "%.1f" % distance3

    c1 = C1
    c2 = C2
    c3 = C3
C1 = np.mean(cluster1)
C2 = np.mean(cluster2)
C3 = np.mean(cluster3)

plt.scatter(sizes, sizeWeight)
plt.plot(C1, 20, color='green', marker='x')
plt.plot(C2, 30, color='green', marker='x')
plt.plot(C3, 40, color='green', marker='x')
plt.show()



