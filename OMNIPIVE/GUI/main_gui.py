import time
import pygame
import pyautogui as pyg

pygame.display.init()
screen_width = 800  # Set your desired screen width
screen_height = 600  # Set your desired screen height
screen = pygame.display.set_mode((screen_width, screen_height), flags=pygame.NOFRAME)


class imageHandler:

    run = True

    def __init__(self):
        self.pics = dict()

    def loadFromFile(self, filename, id=None):
        if id is None:
            id = filename
        self.pics[id] = pygame.image.load(filename).convert()

    def loadFromSurface(self, surface, id):
        self.pics[id] = surface.convert_alpha()

    def render(self, surface, id, position=None, clear=False, size=None):
        if clear:
            surface.fill((5, 2, 23))

        if position is None:
            picX = int(surface.get_width() / 2 - self.pics[id].get_width() / 2)
        else:
            picX = position[0]
            picY = position[1]

        if size is None:
            surface.blit(self.pics[id], (picX, picY))
        else:
            surface.blit(pygame.transform.smoothscale(self.pics[id], size), (picX, picY))

    def display(self):
        for i in range(1, 136):  # Use range(1, 11) to include 10
            self.loadFromFile(rf"C:\Users\bhush\PycharmProjects\PAVAN\OMNIPIVE\GUI\blue_gui\mp ({i}).jpg", str(i))

    def face(self):
        self.display()
        A = 0
        B = 0
        x = 800
        y = 600
        while True:
            if not self.run:
                while not self.run:
                    mp = 1
            for i in range(1, 136):  # Use range(1, 11) to include 10
                self.render(screen, str(i), (A, B), True, (x, y))
                pygame.display.update()
                time.sleep(0.02)
            if not pygame.display.get_active():
                pyg.hotkey('alt', 'tab')
                time.sleep(3)
            # else:
            #     pyg.hotkey('alt', 'tab')
            #     time.sleep(3)

    def minimize_gui(self):
        pygame.display.iconify()


if __name__ == '__main__':
    i = imageHandler()
    i.face()

