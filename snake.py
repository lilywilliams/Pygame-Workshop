# ----- imports -----
import pygame
import random

# ----- global constants -----
BLOCK_SIZE = 20
X_SCREEN_DIM = 400
Y_SCREEN_DIM = 400
X_DIM = X_SCREEN_DIM / BLOCK_SIZE
Y_DIM = Y_SCREEN_DIM / BLOCK_SIZE

# ----- global pygame objects -----
screen = pygame.display.set_mode((X_SCREEN_DIM, Y_SCREEN_DIM))
clock = pygame.time.Clock()

# ----- global game objects -----
snake_segments = [(X_DIM / 2, Y_DIM / 2)] # list of segments in snake
x_direction = 0 # speed in the x direction
y_direction = -1 # speed in the y direction
length = 6 # how long the snake is
grow_length = 3 # how many segments the snake grows for each pellet
pellet = 0 # the pellet - when it's 0, a new pellet needs to be created
score = 0
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# ----- game loop -----
running = True

while running:
    # ----- Screen update -----
    caption = "Score: %d" %score
    pygame.display.set_caption(caption)

    screen.fill(black)

    for i in xrange(1, BLOCK_SIZE - 1):
        for j in xrange(1, BLOCK_SIZE - 1):
            # Blit snake segments to screen
            for x, y in snake_segments:
                screen.set_at((x*BLOCK_SIZE + i, y*BLOCK_SIZE + j), white)

            # Blit pellet to screen
            if pellet != 0:
                x = pellet[0]
                y = pellet[1]
                screen.set_at((x*BLOCK_SIZE + i, y*BLOCK_SIZE + j), red)


    # ----- Game logic -----
    # get coordinates for next snake segment
    x, y = snake_segments[-1]
    new_segment = (x + x_direction, y + y_direction)

    # check for collisions
    if (new_segment in snake_segments or
        new_segment[0] < 0 or new_segment[0] >= X_DIM or
        new_segment[1] < 0 or new_segment[1] >= Y_DIM):
        running = False

    # check for getting the pellet
    if new_segment == pellet:
        pellet = 0
        length += grow_length
        score += 100

    # add and potentially remove segments to snake
    snake_segments.append(new_segment)
    if len(snake_segments) > length:
        snake_segments.pop(0)

    # if there's not a pellet, create one
    if pellet == 0:
        x = random.randint(0, X_DIM - 1)
        y = random.randint(0, Y_DIM - 1)
        while (x, y) in snake_segments:
            x = random.randint(0, X_DIM - 1)
            y = random.randint(0, Y_DIM - 1)
        pellet = (x, y)


    # ----- User input -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y_direction == 0:
                x_direction = 0
                y_direction = -1
            elif event.key == pygame.K_DOWN and y_direction == 0:
                x_direction = 0
                y_direction = 1
            elif event.key == pygame.K_LEFT and x_direction == 0:
                x_direction = -1
                y_direction = 0
            elif event.key == pygame.K_RIGHT and x_direction == 0:
                x_direction = 1
                y_direction = 0

    pygame.display.flip()
    clock.tick(12)
