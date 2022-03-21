class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distance(self, point):
		return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

	def distance(point1, point2):
		return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

	def pointToEdge(self, cushion):
		if cushion.direction == Cushion.VERTICAL:
			return Point(cushion.x, self.y)
		if cushion.direction == Cushion.HORIZONTAL:
			return Point(self.x, cushion.y)

	def incomingAngle(point1, point2, cushion):
		# point2 lines on cushion
		if cushion.direction == Cushion.VERTICAL:
			return math.atan(math.abs(point1.y - point2.y) / math.abs(point1.x - point2.x))
		if cushion.direction == Cushion.HORIZONTAL:
			return Point(self.x, cushion.y)

	def outgoingAngle(point1, point2, cushion):
		# point1 lines on cushion
		pass

a = Point(1, 2)
print(isinstance(a, Point))