import pygame
from pygame.locals import *

RED = (255, 0, 0)
LIGHT_RED = (255, 128, 128)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 128, 255)
GREEN = (82, 184, 82)
LIGHT_GREEN = (100, 255, 100)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)


class Button:
    def __init__(self, path1, x, y, path2=None):
        self.surface = pygame.image.load(path1)
        self.pressed_surf = pygame.image.load(path2 if path2 else path1)
        self.rect = self.surface.get_rect()
        self.rect.center = (x, y)
        self.pressed = False

    def get_surface(self):
        if not self.pressed:
            return self.surface
        return self.pressed_surf


class Snake:
    def __init__(self, x, y):
        self.surface = process_image(GREEN, GREEN, LIGHT_GREEN, pygame.image.load("assets/snake_cell.png"))

        self.size = 10
        self.length = 1

        self.pixels = [[x, y]]

        self.x = x
        self.y = y

        self.prev_pos = (x, y)

        self.xspeed = 10
        self.yspeed = 0

    def update(self):
        self.prev_pos = (self.x, self.y)

        self.x += self.xspeed
        self.y += self.yspeed

        self.pixels.append([self.x, self.y])

        if len(self.pixels) > self.length:
            del self.pixels[0]

    def render(self, screen: pygame.Surface):
        for pixel in self.pixels:
            screen.blit(self.surface, [pixel[0], pixel[1], self.size, self.size])

    def collides(self, rect: pygame.Rect):
        if [rect.x, rect.y] in self.pixels:
            return True
        return False

    def grow(self):
        self.length += 1

    def reset_stats(self):
        self.x = 0
        self.y = 20
        self.prev_pos = (self.x, self.y)
        self.xspeed = 10
        self.yspeed = 0
        self.length = 1
        self.pixels = [[self.x, self.y]]

    # TODO: COMPUTE CELLS positions
    def dir_right(self):
        if self.length > 1:
            if self.xspeed != -self.size and self.y != self.prev_pos[1]:
                self.xspeed = self.size
                self.yspeed = 0
        else:
            self.xspeed = self.size
            self.yspeed = 0

    def dir_left(self):
        if self.length > 1:
            if self.xspeed != self.size and self.y != self.prev_pos[1]:
                self.xspeed = -self.size
                self.yspeed = 0
        else:
            self.xspeed = -self.size
            self.yspeed = 0

    def dir_up(self):
        if self.length > 1:
            if self.yspeed != self.size and self.x != self.prev_pos[0]:
                self.xspeed = 0
                self.yspeed = -self.size
        else:
            self.xspeed = 0
            self.yspeed = -self.size

    def dir_down(self):
        if self.length > 1:
            if self.yspeed != -self.size and self.x != self.prev_pos[0]:
                self.xspeed = 0
                self.yspeed = self.size
        else:
            self.xspeed = 0
            self.yspeed = self.size


class Food:
    def __init__(self, x, y, path):
        self.x = x
        self.y = y

        self.surface = pygame.image.load(path)
        self.rect = self.surface.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
        return


class TextBoxInput:
    def __init__(self, x, y, width, height):
        self.content = ""
        self.color = (255, 255, 255)
        self.cursor_color = (0, 0, 0)
        self.input_rect = pygame.Rect(x, y, width, height)
        self.input_surface = draw_text(self.content, height, BLACK)
        self.x = self.input_rect.x
        self.y = self.input_rect.y

        # DO NOT MESS WITH THIS, THIS IS CURSOR
        self.internal = 0

    def render(self, screen: pygame.Surface, events):
        self.internal += 1
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    self.content = self.content[:-1]
                else:
                    if len(self.content) < 4:
                        self.content += event.unicode

        pygame.draw.rect(screen, self.color, self.input_rect)
        self.input_surface = draw_text(self.content, 50, BLACK)
        screen.blit(self.input_surface, [self.input_rect.x + 5, self.input_rect.y + 5])

        if self.internal > 15:
            pygame.draw.line(screen, BLACK,
                             (self.input_rect.x + 5 + self.input_surface.get_width(), self.input_rect.y + 5),
                             (self.input_rect.x + 5 + self.input_surface.get_width(),
                              self.input_rect.y + self.input_rect.height - 5), 3)
        if self.internal == 30:
            self.internal = 0

    def clear(self):
        self.content = ""
        
        
        
        
        
def process_image(col1, col2, col3, surface):
    img_str = pygame.image.tostring(surface, "RGB", False)
    converted = bytes()
    temp = []
    for index, val in enumerate(img_str, 1):
        temp.append(val)
        if index % 3 == 0:
            if temp == [0, 0, 0]:
                converted += bytes(col1)
            elif temp == [128, 128, 128]:
                converted += bytes(col2)
            if temp == [192, 192, 192]:
                converted += bytes(col3)
            temp.clear()
    surface = pygame.image.fromstring(converted, (10, 10), "RGB")
    del img_str
    return surface


def draw_text(string, size, col=None):
    txt = pygame.font.Font("assets/fonts/bit.ttf", size)
    return txt.render(string, True, (255, 255, 255) if not col else col)
