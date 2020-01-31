import sys
import time
import pygame

data = []

class Cell:
    def __init__(self, x, y, v):
        self.row = x
        self.column = y
        self.value = v

    def can_go(self, target_x, target_y):
        if target_x in range(len(data)) and target_y in range(len(data[0])):
            if data[target_x][target_y].value == '.':
                return True
            elif data[target_x][target_y].value == '#':
                return False
            elif data[target_x][target_y].value < self.value + 2:
                return False
            return True
        else:
            return False

    def make_move(self):
        if self.can_go(self.row + 1, self.column):
            update_screen(data[self.row + 1][self.column])
            data[self.row + 1][self.column].value = self.value + 1
            data[self.row + 1][self.column].make_move()

        if self.can_go(self.row - 1, self.column):
            update_screen(data[self.row - 1][self.column])
            data[self.row - 1][self.column].value = self.value + 1
            data[self.row - 1][self.column].make_move()

        if self.can_go(self.row, self.column + 1):
            update_screen(data[self.row][self.column + 1])
            data[self.row][self.column + 1].value = self.value + 1
            data[self.row][self.column + 1].make_move()

        if self.can_go(self.row, self.column - 1):
            update_screen(data[self.row][self.column - 1])
            data[self.row][self.column - 1].value = self.value + 1
            data[self.row][self.column - 1].make_move()


def generate_table_as_list():
    output = []
    h = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            h.append(data[i][j].value)
        output.append(h)
        h = []
    return output


def update_screen(target):

    screen.fill(black)
    for r in range(len(data)):
        for c in range(len(data[0])):
            rectangle = pygame.Rect(r * 40, c * 40, 40, 40)
            if r == target.row and c == target.column:
                pygame.draw.rect(screen, yellow, rectangle)
            elif data[r][c].value == '#':
                pygame.draw.rect(screen, black, rectangle)
            elif data[r][c].value == '.':
                pygame.draw.rect(screen, white, rectangle)
            else:
                pygame.draw.rect(screen, green, rectangle)
    time.sleep(0.4)
    pygame.display.flip()



f = open("input.txt", "r")
content = f.read()

content = content.split()

pom = []
data = []

for i in range(len(content)):
    for j in range(len(content[i])):
        pom.append(content[i][j])
    data.append(pom)
    pom = []

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = Cell(i, j, data[i][j])

pygame.init()

w = len(data[0])*40
h = len(data)*40

size = width, height = h, w
speed = [2, 2]
black = 0, 0, 0
yellow = 255, 255, 0
red = 255, 0, 0
green = 0, 255, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

data[0][0].value = 1
data[0][0].make_move()

finished = generate_table_as_list()

output_file = open("output.txt", "w")
for i in range(len(data)):
    output_file.write(''.join([str(j.value) for j in data[i]]))
    output_file.write("\n")

time.sleep(5)

sys.exit()