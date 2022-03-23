lines = open("../res/BidaAngle.txt", "r").read().split("\n")
n = len(lines)
inAngle = [float(i.split(':')[0]) for i in lines]
outAngle = [float(i.split(':')[1]) for i in lines]
ratio = [outAngle[i] / inAngle[i] for i in range(n)]
import matplotlib.pyplot as plt
plt.plot(inAngle, ratio)
plt.show()