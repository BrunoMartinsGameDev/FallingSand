from Mouse import Mouse


class Screen:
    def __init__(self, width, height, pygame, title):
        self.width = width
        self.height = height
        self.pygame = pygame
        self.title = title
        self.screen = self.pygame.display.set_mode((self.width, self.height))
    
    def start(self):
        self.pygame.display.set_caption(self.title)
        self.mouse = Mouse(self.pygame)
    def update(self):
        self.mouse.update()
    def late_update(self):
        self.mouse.late_update()