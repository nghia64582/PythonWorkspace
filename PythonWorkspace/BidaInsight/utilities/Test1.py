from matplotlib import markers
import matplotlib.pyplot as plt
from math import *
lines = [[float(i) for i in line[1 : -1].split(', ')[ : 2]] for line in open("BidaRecord1.txt", "r").read().split("\n")]
# lines.sort(key = lambda x : x[0])
x = [i[0] for i in lines]
y = [i[1] for i in lines]
n = len(lines)
# draw plot

cx = 255.7 / 2
cy = 127.7 / 2
figure, axes = plt.subplots()
axes.set_aspect(1)
draw_circle1 = plt.Circle((cx, cy), 7,fill=False)
axes.add_artist(draw_circle1)
draw_circle2 = plt.Circle((cx, -cy), 7,fill=False)
axes.add_artist(draw_circle2)
draw_circle3 = plt.Circle((-cx, cy), 7,fill=False)
axes.add_artist(draw_circle3)
draw_circle4 = plt.Circle((-cx, -cy), 7,fill=False)
axes.add_artist(draw_circle4)
draw_circle5 = plt.Circle((0, -cy), 7,fill=False)
axes.add_artist(draw_circle5)
draw_circle6 = plt.Circle((0, cy), 7,fill=False)
axes.add_artist(draw_circle6)

plt.plot(-127.7, 63.8, "bo")
plt.plot(-127.7, -63.8, "bo")
plt.plot(127.7, 63.8, "bo")
plt.plot(127.7, -63.8, "bo")
plt.plot(x, y, "bo", markersize=1)
for i in range(n):
    if i % 5 == 0:
        plt.annotate(str(i), [x[i], y[i]])
plt.show()
