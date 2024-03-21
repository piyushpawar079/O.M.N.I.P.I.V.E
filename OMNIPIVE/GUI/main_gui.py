import time
import pygame


class imageHandler:
    flag = False

    def __init__(self):
        self.pics1 = dict()
        self.pics2 = dict()

    def loadFromFile1(self, filename, id=None):
        if id is None:
            id = filename
        self.pics1[id] = pygame.image.load(filename).convert()

    def loadFromFile2(self, filename, id=None):
        if id is None:
            id = filename
        self.pics2[id] = pygame.image.load(filename).convert()

    def render1(self, surface, id, clear=False, size=None):
        if clear:
            surface.fill((5, 2, 23))

        if id in self.pics1:
            image = self.pics1[id]
            image_rect = image.get_rect()
            surface_rect = surface.get_rect()

            # Calculate the centered position
            center_x = surface_rect.centerx - image_rect.width // 2
            center_y = surface_rect.centery - image_rect.height // 2

            if size is None:
                surface.blit(image, (center_x, center_y))
            else:
                surface.blit(pygame.transform.smoothscale(image, size), (center_x, center_y))
        else:
            print(f"Image with ID '{id}' not found in self.pics dictionary.")

    def render2(self, surface, id, clear=False, size=None):
        if clear:
            surface.fill((5, 2, 23))

        if id in self.pics2:
            image = self.pics2[id]
            image_rect = image.get_rect()
            surface_rect = surface.get_rect()

            # Calculate the centered position
            center_x = surface_rect.centerx - image_rect.width // 2
            center_y = surface_rect.centery - image_rect.height // 2

            if size is None:
                surface.blit(image, (center_x, center_y))
            else:
                surface.blit(pygame.transform.smoothscale(image, size), (center_x, center_y))
        else:
            print(f"Image with ID '{id}' not found in self.pics dictionary.")

    def display(self):
        for i in range(1, 277):  # Use range(1, 11) to include 10
            self.loadFromFile1(rf"C:\Users\bhush\PycharmProjects\PAVAN\OMNIPIVE\GUI\mp_gui\mp_gui\mp ({i}).jpg", str(i))
        for i in range(1, 90):
            self.loadFromFile2(rf"C:\Users\bhush\PycharmProjects\PAVAN\OMNIPIVE\GUI\glowing_gui\gp ({i}).jpg", str(i))

    def face(self):
        self.display()
        x = screen_width
        y = screen_height

        while True:
            if self.flag:
                for i in range(1, 277):  # Use range(1, 11) to include 10
                    self.render1(screen, str(i), True, (x, y))
                    pygame.display.update()
                    time.sleep(0.01)
                    if not self.flag:
                        break
            else:
                for i in range(1, 89):  # Use range(1, 11) to include 10
                    self.render2(screen, str(i), True, (x, y))
                    pygame.display.update()
                    time.sleep(0.1)
                    if self.flag:
                        break

    def Exit(self):
        pygame.quit()


pygame.init()
screen_width = 800  # Set your desired screen width
screen_height = 600  # Set your desired screen height
screen = pygame.display.set_mode((screen_width, screen_height))

