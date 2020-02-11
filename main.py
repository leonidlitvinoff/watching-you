import pygame


pygame.init()
size = width, height = 200, 200
screen = pygame.display.set_mode(size)
running = True
counter = 1
font = pygame.font.Font(None, 100)
text = font.render(str(counter), 1, (255, 0, 0))
text_x = width // 2 - text.get_width() // 2
text_y = height // 2 - text.get_height() // 2
text_w = text.get_width()
text_h = text.get_height()
screen.blit(text, (text_x, text_y))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.ACTIVEEVENT and event.state == 6:
            counter += 1
            screen.fill((0, 0, 0))
            text = font.render(str(int(counter / 2 + 1)), 1, (255, 0, 0))
            screen.blit(text, (text_x, text_y))
    pygame.display.flip()