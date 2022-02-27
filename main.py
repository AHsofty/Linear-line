import pygame
import LinearFunction

BLACK    = (0,   0,   0)
WHITE    = (255, 255, 255)

pygame.init()
pygame.font.init()

# THIS HERE IS THE ACTUAL FUNCTION
# THE FUNCTION: 
# Y = arg1x + arg2
# This is kinda hardcoded but you get the idea
f = LinearFunction.LinearFunction(-5, 2) 

# We define our window size
W = 500
H = 500

# This'll get us two points on the line
A = (f.xcor(-H), H) 
B = (f.xcor(H), -H) 

deltaX = B[0] - A[0]
deltaY = B[1] - A[1]

# We change the positions
# We do this to prevent the line from appearing outside of the screen
new_a = (W/2, H)
new_b = (new_a[0]+deltaX, new_a[0]+deltaY)

screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Line go brrrr")

# Now we draw the cool line
pygame.draw.line(screen, WHITE, new_a, new_b)

# We type some text
myfont = pygame.font.SysFont(pygame.font.get_default_font(), 25)
functionText = myfont.render(f"y = {f.a}x + {f.b}", False, WHITE)
aText = myfont.render(f"({A[0]}, {A[1]})", False, WHITE)
bText = myfont.render(f"({B[0]}, {B[1]})", False, WHITE)


running = True
while running:
	# OMIGOSH HARDCODING
	screen.blit(functionText,((W/2)-35, 10))
	screen.blit(aText, (new_a[0]+20, new_a[1]-20))
	screen.blit(bText, (new_b[0], new_b[1]))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False

	pygame.display.update()