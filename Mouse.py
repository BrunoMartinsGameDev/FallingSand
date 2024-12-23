class Mouse:
    def __init__(self,pygame):
        self.x = 0
        self.y = 0
        self.pygame = pygame
        self.leftButtomPressed = False
        self.rightButtomPressed = False
        self.middleButtomPressed = False
        self.leftButtomClicked = False
    def update(self):
        self.__updatePosition()
        self.__updateMousePressed()
        for event in self.pygame.event.get():
            if event.type == self.pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.leftButtomClicked = True
    def late_update(self):
        self.leftButtomClicked = False
    def __updatePosition(self):
        mouse_pos = self.pygame.mouse.get_pos()
        self.x = mouse_pos[0]
        self.y = mouse_pos[1]
    def __updateMousePressed(self):
        self.leftButtomPressed = self.pygame.mouse.get_pressed()[0]
        self.rightButtomPressed = self.pygame.mouse.get_pressed()[2]
        self.middleButtomPressed = self.pygame.mouse.get_pressed()[1]
    