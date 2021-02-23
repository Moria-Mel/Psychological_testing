import pygame



pygame.init()
screen = pygame.display.set_mode((480, 420))
keys_list = ['Г', 'Ц', 'Л', 'А', 'С', 'П', 'Ш', 'Э', 'И', 'Н', 'К', 'О',
                 'Д', 'Т', 'В', 'Е', 'd', 'М', 'Ф']
x_line = 330
y_line = 60
place_dict = {keys_list[i]: y_line + 20 * i for i in range(len(keys_list))}
font = pygame.font.Font(None, 24)


class Line(pygame.sprite.Sprite):
    def __init__(self, name, value):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, value * 20))
        self.image.fill((100, 100, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = place_dict[name]
        self.rect.y = x_line - value * 20


class Text(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(name, True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = place_dict[name]
        self.rect.y = x_line + 15


class Different_text(pygame.sprite.Sprite):
    def __init__(self, text, place):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(text, True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = place[0], place[1]


def draw_red_line(start, leng):
    global screen
    pygame.draw.line(screen, (255, 0, 0), start, (start[0] + leng, start[1]), 3)


def graphic(ito_dict, V):
    pygame.display.set_caption("Результаты")
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    numb_font = pygame.font.Font(None, 12)
    running = True
    FPS = 60

    for i in keys_list:
        all_sprites.add(Line(i, ito_dict[i]))
        all_sprites.add(Text(i))
    all_sprites.add(Different_text(f'Склонность к алкоголизации = {V}', (20, 390)))
    while running:
        clock.tick(FPS)
        screen.fill((255, 255, 255))
        for i in range(16):
            pygame.draw.line(screen, (0, 0, 0), (y_line - 20, x_line - i * 20), (y_line + len(keys_list) * 20, x_line - i * 20), 1)
            screen.blit(numb_font.render(str(i), True, (0, 0, 0)), (y_line - 30, x_line - i * 20 - 3))
        all_sprites.draw(screen)
        draw_red_line((y_line - 10, x_line - 6 * 20), 20)
        draw_red_line((y_line + 10, x_line - 5 * 20), 40)
        draw_red_line((y_line + 50, x_line - 4 * 20), 20)
        draw_red_line((y_line + 70, x_line - 5 * 20), 140)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

