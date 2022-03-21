import matplotlib.pyplot as plt
lines = open("BidaAngle.txt", "r").read().split("\n")
a = [line.split(":") for line in lines]
angle = [90 - float(a[i][0]) for i in range(len(lines))]
ratio = [float(a[i][3]) for i in range(len(lines))]
newAngle = [angle[i] * ratio[i] for i in range(len(lines))]
plt.plot(angle, ratio)
plt.xlabel("angle")
plt.ylabel("ratio")
plt.show()