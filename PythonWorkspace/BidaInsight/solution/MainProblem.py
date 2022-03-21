import math

def compare(x, y, op):
	return {
		"=": x == y,
		">": x > y,
		"<": x < y	
	}[op]

def solve(cueBall, target, cushion):
	# [x, y], [x, y], [[x, y], [x, y]]
	minXCushion = cueBall[0]
	maxXCushion = target[0]
	epsilon = 1e-12
	while minXCushion < maxXCushion - epsilon:
		curX = (minXCushion + maxXCushion) / 2
