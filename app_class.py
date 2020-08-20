import pygame,sys
from settings import *
from buttonClass import *
import numpy as np


class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = finishedBoard
        self.selected = None
        self.mousePos = None
        self.state = "playing"
        self.finished = False
        self.cellChanged = False
        self.incorrectCells = []
        self.playingButtons = []
        self.menuButtons = []
        self.endButtons = []
        self.lockedCells = []
        self.font = pygame.font.SysFont("arial", cellSize // 2)
        self.load()
        print (np.matrix(self.grid))

    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
        pygame.quit()
        sys.exit()
        ###playing state functions#####

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid()
                if selected:
                    self.selected = selected
                else:
                    print("not on board")
                    self.selected = None

            # User Input
            if event.type == pygame.KEYDOWN:
                if self.selected != None and self.selected != self.lockedCells:
                    if self.isInt(event.unicode):
                        self.grid[self.selected[1]][self.selected[0]] = int(event.unicode)
                        self.cellChanged = True

    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.playingButtons:
            button.update(self.mousePos)

        if self.cellChanged :
            self.incorrectCells = []
            if self.allCellsDone():
                self.checkAllCells()
                print (self.incorrectCells)


    def checkALlCells(self):
        pass


    def playing_draw(self):
        self.window.fill(WHITE)

        for button in self.playingButtons:
            button.draw(self.window)

        if self.selected:
            self.drawSelection(self.window, self.selected)

        self.shadeLockedCells(self.window, self.lockedCells)
        self.shadeIncorrectCells(self.window,self.incorrectCells)

        self.drawNumber(self.window)
        self.drawGrid(self.window)

        pygame.display.update()
        self.cellChanged = False


    # Helper Functions
    def shadeLockedCells(self, window, locked):
        for cell in locked:
            pygame.draw.rect(window, LOCKEDCELLCOLOR, (cell[0]*cellSize+gridPos[0], cell[1]*cellSize+gridPos[1], cellSize, cellSize))

    def shadeIncorrectCells(self, window, incorrect):
        for cell in incorrect:
            pygame.draw.rect(window, INCORRECTCELLCOLOR, (cell[0]*cellSize+gridPos[0], cell[1]*cellSize+gridPos[1], cellSize, cellSize))

    def drawNumber(self, window):
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != 0:
                    pos = [(xidx * cellSize) + gridPos[0], (yidx * cellSize) + gridPos[1]]
                    self.textToScreen(window, str(num), pos)

    def drawSelection(self, window, pos):
        pygame.draw.rect(window, LIGHTBLUE,
                         ((pos[0] * cellSize) + gridPos[0], (pos[1] * cellSize) + gridPos[1], cellSize, cellSize))

    def drawGrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH - 150, HEIGHT - 150), 2)
        for x in range(9):
            pygame.draw.line(window, BLACK, (gridPos[0] + (x * cellSize), gridPos[1]),
                             (gridPos[0] + (x * cellSize), gridPos[1] + 450), 2 if x % 3 == 0 else 1)
            pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + (x * cellSize)),
                             (gridPos[0] + 450, gridPos[1] + +(x * cellSize)), 2 if x % 3 == 0 else 1)

    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:
            return False
        if self.mousePos[0] > gridPos[0] + gridSize or self.mousePos[1] > gridPos[1] + gridSize:
            return False
        return ((self.mousePos[0] - gridPos[0]) // cellSize, (self.mousePos[1] - gridPos[1]) // cellSize)

    def loadButtons(self):
        self.playingButtons.append(Button(20, 40, 100, 40))

    def load(self):
        self.loadButtons()
        # self.lockedCells = []

        # Setting locked Cells
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != 0:
                    self.lockedCells.append([xidx, yidx])
        print(self.lockedCells)

    def textToScreen(self, window, text, pos):
        font = self.font.render(text, False, BLACK)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSize - fontWidth) // 2
        pos[1] += (cellSize - fontHeight) // 2
        window.blit(font, pos)

    def isInt(self, string):
        try:
            int(string)
            return True
        except:
            return False

# Board Checking functions
    def allCellsDone(self):
        for row in self.grid:
            for number in row:
                if number == 0:
                    return False
        return True

    def checkAllCells(self):
        self.checkRows()

    def checkRows(self):
        for yidx ,row in enumerate(self.grid):
            possibles = [1,2,3,4,5,6,7,8,9]
            for xidx in range(9):
                if self.grid[yidx][xidx] in possibles:
                    possibles.remove(self.grid[yidx][xidx])
                else:
                    if [xidx,yidx] not in self.lockedCells and [xidx,yidx] not in self.incorrectCells:
                        self.incorrectCells.append([xidx,yidx])

