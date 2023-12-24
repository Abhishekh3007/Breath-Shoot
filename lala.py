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

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
                self.change_text(f"{self.text}")
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:

                    if button10.pressed:
                        pygame.quit()
                        sys.exit()

                    if button1.pressed:
                        # print('click')
                        import bs

                    if button2.pressed:
                        Button("0", 200, 50, (580, 325), 0)
                        zero = 0
                        f = open("scores/g7.dat", 'w')
                        f.write(str(zero))
                        f.close()
                    # print('click')
                    # import FinalGame_7
                    self.pressed = False
                    self.change_text(self.text)
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'


pygame.init()
screen = pygame.display.set_mode((800, 560))
pygame.display.set_caption('Controls')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 30)

v = open("scores/g7.dat", 'r')
topScore = int(v.readline())
v.close()
a = topScore

x = open("scores/hg7.dat", 'r')
HScore = int(x.readline())
x.close()
high = HScore
button10 = Button('Quit', 200, 40, (580, 500), 5)
button1 = Button('Play Now', 200, 40, (580, 400), 5)
button2 = Button('Reset score', 200, 42, (580, 450), 5)
button7 = Button('Current Score', 200, 30, (580, 290), 0)
button8 = Button(a.__str__(), 200, 50, (580, 325), 0)
btn1 = Button('High-Score', 200, 30, (580, 180), 0)
btn2 = Button(high.__str__(), 200, 50, (580, 215), 0)
if a > high:
    zero = a
    f = open("scores/hg7.dat", 'w')
    f.write(str(zero))
    f.close()
    btn2 = Button(high.__str__(), 200, 50, (580, 215), 0)

display_surface = pygame.display.set_mode((800, 560))
# display_surface = pygame.display.set_mode((800, 560))
# button1 = Button('Play Now', 200, 40, (560, 480), 5)

# image = pygame.image.load(r'C:\Project BCA\All in one\gc1.jpg')
image = pygame.image.load('gbg.png')

def buttons_draw():
    for b in buttons:
        b.draw()


while True:
    for event in pygame.event.get():
        display_surface.blit(image, (0, 0))
        if event.type == pygame.QUIT:
            # os.system("GUI6.exe")
            pygame.quit()
            sys.exit()

    # screen.fill('#DCDDD8')
    buttons_draw()
    pygame.display.update()
    clock.tick(60)
