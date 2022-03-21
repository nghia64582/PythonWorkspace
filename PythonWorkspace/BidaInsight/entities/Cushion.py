class Cushion:
	VERTICAL = 1
	HORIZONTAL = 2
	def __init__(self, x, y, direction):
		self.x = x
		self.y = y
		self.direction = direction

	def pointToEdge(self, point):
		if self.direction == Cushion.VERTICAL:
			return Point(self.x, point.y)
		if self.direction == Cushion.HORIZONTAL:
			return Point(point.x, self.y)
		