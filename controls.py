import os

import pygame, sys

buttons = []


class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'
        # text
        self.text = text
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        buttons.append(self)

    def change_text(self, newtext):
        self.text_surf = gui_font.render(newtext, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

pygame.init()
screen = pygame.display.set_mode((800+200, 560+200))
pygame.display.set_caption('Controls')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 30)


display_surface = pygame.display.set_mode((800+200, 560+200))

image = pygame.image.load('cs.png')


def buttons_draw():
    for b in buttons:
        b.draw()


while True:
    for event in pygame.event.get():
        display_surface.blit(image, (0, 0))
        if event.type == pygame.QUIT:
            os.system("Breathshoot.exe")
            pygame.quit()
            sys.exit()

    # screen.fill('#DCDDD8')
    buttons_draw()

    pygame.display.update()
    clock.tick(60)
