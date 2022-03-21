import pygame
from time import *
from math import *

class Point:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

def init():
	global NUM_BALLS, BALL_RADIUS, ZOOM, states
	pygame.font.init()
	lines = open("TurnRecord2.txt", "r").read().split("\n")[1:]
	NUM_BALLS = 16
	BALL_RADIUS = 3
	ZOOM = 3
	states = []
	for i in range(len(lines) // NUM_BALLS):
		state = []
		for j in range(NUM_BALLS):
			idx = i * NUM_BALLS + j
			state.append([float(ele) for ele in lines[idx].split()])
		states.append(state)

def f(x, y):
	return [x * ZOOM + 500, 200 - y * ZOOM]
	
def drawText(x, y, st):
	myfont = pygame.font.SysFont('Arial', 10)
	textsurface = myfont.render(st, False, (0, 255, 255))
	screen.blit(textsurface,(x, y))

def fAngle(x, y):
	if x == 0:
		return pi / 2 if y > 0 else 3 * pi / 2
	return atan(y / x) * (1 if x > 0 else -1) * 180 / pi

def drawBall(preState, state):
	screen.fill((0, 0, 0))
	for i in range(len(state)):
		ball = state[i]
		preBall = preState[i]
		color = (255, 255, 255) if i == 0 else (255, 0, 0)
		x, y = f(ball[0], ball[1])
		pygame.draw.circle(screen, color, (x, y), BALL_RADIUS * ZOOM)
		dx, dy = [ball[0] - preBall[0], ball[1] - preBall[1]]
		speed = round((dx * dx + dy * dy) ** 0.5, 2)
		angle = round(fAngle(dx, dy), 3)
		drawText(x, y, str(angle))
	pygame.display.flip()	

def main():
	global screen
	pygame.init()
	screen = pygame.display.set_mode((1500, 600))
	done = False
	x, y = 0, 0
	idx = 0
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == ord('q'):
					done = True
		idx += 1
		if idx < len(states):
			drawBall(states[idx - 1], states[idx])
		sleep(0.05)

def test():
	minX = 10000
	minY = 10000
	maxX = -10000
	maxY = -10000
	i = 0
	for state in states:
		for ball in state:
			i += 1
			minX = min(minX, ball[0])
			maxX = max(maxX, ball[0])
			minY = min(minY, ball[1])
			maxY = max(maxY, ball[1])
	print(i, minX, minY, maxX, maxY)

# init()
# main()
# test()
start = time()
file = open("BidaAngle.txt", "r")
print(time() - start)