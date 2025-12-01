import pygame
import sys

pygame.init()

# --- FULLSCREEN ---
screen = pygame.display.set_mode((1200,800))
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Maze Generator")

# Zegar bierzemy, żeby kontrolować framerate, ale na razie nie używam
# clock = pygame.time.Clock()
print(WIDTH, HEIGHT)

# przykladowa
maze = {
    (0,0): [(1,0),(0,1)],
    (1,0): [(0,0),(1,1)],
    (0,1): [(0,0),(0,2)],
    (1,1): [(1,0),(2,1)],
    (2,1): [(1,1),(2,2)],
    (0,2): [(0,1),(1,2)],
    (1,2): [(0,2),(2,2)],
    (2,2): [(1,2),(2,1),(3,2)],
    (3,2): [(2,2),(4,2)],
    (4,2): [(3,2),(4,3)],
    (4,3): [(4,2),(4,4)],
    (4,4): [(4,3)],
}

CELL_SIZE = 60

maxX, maxY = 0, 0
for pos in maze:
    for cell in maze[pos]:
        maxX, maxY = max(cell[0], maxX), max(cell[1], maxY)

#rzeczy do kamery
last_mouse_pos = pygame.mouse.get_pos()
x, y = 0, 0
dragging = False
zoom = 1
# Main Game Loop
running = True
while running:

    for event in pygame.event.get():
        # wylaczanie escapem dla pelnego ekranu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # wylaczanie zwykle lel
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            last_mouse_pos = pygame.mouse.get_pos()
            dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                zoom *= 1.1
                zoom = min(4, zoom)
            else:
                zoom /= 1.1
                zoom = max(0.1, zoom)

    if dragging:
        mx, my = pygame.mouse.get_pos()
        dx = mx - last_mouse_pos[0]
        dy = my - last_mouse_pos[1]
        x += dx
        y += dy
        last_mouse_pos = (mx, my)

    screen.fill((255,255,255))

    #pygame.draw.circle(screen, (255, 255, 255), (100+x, 100+y), int(zoom*100), int(zoom*50))

    for pos in maze:
        px, py = pos #rysujemy linie z pos do cela
        cell_size_scaled = CELL_SIZE * zoom

        rect_x = px * cell_size_scaled + x - cell_size_scaled / 2
        rect_y = py * cell_size_scaled + y - cell_size_scaled / 2

        pygame.draw.rect(screen, (50, 50, 50),
                         (rect_x, rect_y, cell_size_scaled, cell_size_scaled), 2)
        for cell in maze[pos]:
            cx, cy = cell #cell x i cell y
            pygame.draw.line(screen, (255,0,0), (px*int(zoom*CELL_SIZE)+x, py*int(zoom*CELL_SIZE)+y),
                             (cx*int(zoom*CELL_SIZE)+x, cy*int(zoom*CELL_SIZE)+y), 4)

    pygame.display.flip()

pygame.quit()
sys.exit()
