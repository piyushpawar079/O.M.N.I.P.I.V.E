import pygame as p
import time

p.init()


class Square(p.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = ''
        self.number = number
        self.image = blank_image
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)

    def clicked(self, x_val, y_val):
        global turn, won

        if self.content == '':
            if self.rect.collidepoint(x_val, y_val):
                self.content = turn
                board[self.number] = turn

                if turn == 'x':
                    self.image = x_image
                    self.image = p.transform.scale(self.image, (self.width, self.height))
                    turn = 'o'
                    checkWinner('x')

                    if not won:
                        CompMove()

                else:
                    self.image = o_image
                    self.image = p.transform.scale(self.image, (self.width, self.height))
                    turn = 'x'
                    checkWinner('o')


def checkWinner(player):
    global background, won, startX, startY, endX, endY

    for i in range(8):
        if board[winners[i][0]] == player and board[winners[i][1]] == player and board[winners[i][2]] == player:
            won = True
            getPos(winners[i][0], winners[i][2])
            break

    if won:
        Update()
        drawLine(startX, startY, endX, endY)
        square_group.empty()
        w = "\\" + player.upper()
        m = r'C:\Users\bhush\PycharmProjects\PAVAN\OMNIPIVE\Games\TicTacToe'
        background = p.image.load( m + w + ' Wins.png')
        background = p.transform.scale(background, (WIDTH, HEIGHT))



def CompMove():
    global move, background
    move = True

    if move:
        Winner('o')

    if move:
        Winner('x')

    if move:
        checkDangerPos()

    if move:
        checkCentre()

    if move:
        checkCorner()

    if move:
        checkEdge()

    if not move:
        for square in squares:
            if square.number == compMove:
                square.clicked(square.x, square.y)

    else:
        Update()
        time.sleep(1)
        square_group.empty()
        background = p.image.load(r'/OMNIPIVE/Games/tic-tac-toe/Tie Game.png')
        background = p.transform.scale(background, (WIDTH, HEIGHT))


def Winner(player):
    global compMove, move

    for i in range(8):
        if board[winners[i][0]] == player and board[winners[i][1]] == player and board[winners[i][2]] == '':
            compMove = winners[i][2]
            move = False

        elif board[winners[i][0]] == player and board[winners[i][1]] == '' and board[winners[i][2]] == player:
            compMove = winners[i][1]
            move = False

        elif board[winners[i][0]] == '' and board[winners[i][1]] == player and board[winners[i][2]] == player:
            compMove = winners[i][0]
            move = False


def checkDangerPos():
    global move, compMove

    if board == dangerPos1:
        compMove = 2
        move = False

    elif board == dangerPos2:
        compMove = 4
        move = False

    elif board == dangerPos3:
        compMove = 1
        move = False

    elif board == dangerPos4:
        compMove = 4
        move = False

    elif board == dangerPos5:
        compMove = 7
        move = False

    elif board == dangerPos6:
        compMove = 9
        move = False

    elif board == dangerPos7:
        compMove = 9
        move = False

    elif board == dangerPos8:
        compMove = 7
        move = False

    elif board == dangerPos9:
        compMove = 9
        move = False


def checkCentre():
    global compMove, move

    if board[5] == '':
        compMove = 5
        move = False


def checkCorner():
    global compMove, move

    for i in range(1, 11, 2):
        if i != 5:
            if board[i] == '':
                compMove = i
                move = False
                break


def checkEdge():
    global compMove, move

    for i in range(2, 10, 2):
        if board[i] == '':
            compMove = i
            move = False
            break


green_color = (52, 168, 83)
light_green_color = (125, 213, 113)
red_color = (255, 69, 58)
light_red_color = (255, 138, 128)


def getPos(n1, n2):
    global startX, startY, endX, endY

    for sqs in squares:
        if sqs.number == n1:
            startX = sqs.x
            startY = sqs.y

        elif sqs.number == n2:
            endX = sqs.x
            endY = sqs.y


def drawLine(x1, y1, x2, y2):
    p.draw.line(win, (0, 0, 0), (x1, y1), (x2, y2), 15)
    p.display.update()
    time.sleep(2)


def Update():
    win.blit(background, (0, 0))
    square_group.draw(win)
    square_group.update()
    p.display.update()





def main_menu():
    running = True
    while running:
        win.fill((49, 112, 143))  # Set a beautiful background color

        # Define color combinations for buttons
        light_blue = (102, 204, 255)
        dark_blue = (0, 51, 102)
        light_purple = (153, 102, 204)

        # One Player Button
        one_player_button = p.Rect(150, 200, 200, 50)
        p.draw.rect(win, light_blue, one_player_button)
        draw_text("One Player", font, (255, 255, 255), win, 190, 215)

        # Two Players Button
        two_players_button = p.Rect(150, 280, 200, 50)
        p.draw.rect(win, light_purple, two_players_button)
        draw_text("Two Players", font, (255, 255, 255), win, 180, 295)

        # Exit Button
        exit_button = p.Rect(150, 360, 200, 50)
        p.draw.rect(win, dark_blue, exit_button)
        draw_text("Exit", font, (255, 255, 255), win, 220, 375)

        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
                p.quit()
                quit()
            elif event.type == p.MOUSEBUTTONDOWN:
                mouse_pos = p.mouse.get_pos()

                if one_player_button.collidepoint(mouse_pos):
                    start_one_player_game()
                elif two_players_button.collidepoint(mouse_pos):
                    start_two_players_game()
                elif exit_button.collidepoint(mouse_pos):
                    running = False
                    p.quit()
                    quit()
                    # Check if mouse click is on a button

        p.display.update()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


WIDTH, HEIGHT = 1100, 700

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Tic Tac Toe')
clock = p.time.Clock()

blank_image = p.image.load(r'/OMNIPIVE/Games/tic-tac-toe/Blank.png')
x_image = p.image.load(r'/OMNIPIVE/Games/tic-tac-toe/x.png')
o_image = p.image.load(r'/OMNIPIVE/Games/tic-tac-toe/o.png')
background = p.image.load(r'/OMNIPIVE/Games/tic-tac-toe/Background.png')

background = p.transform.scale(background, (WIDTH, HEIGHT))

won = False
move = True
compMove = 5

square_group = p.sprite.Group()
squares = []

winners = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
board = ['' for i in range(10)]

dangerPos1 = ['', 'x', '', '', '', 'o', '', '', '', 'x']
dangerPos2 = ['', '', '', 'x', '', 'o', '', 'x', '', '']
dangerPos3 = ['', '', '', 'x', 'x', 'o', '', '', '', '']
dangerPos4 = ['', 'x', '', '', '', 'o', 'x', '', '', '']
dangerPos5 = ['', '', '', '', 'x', 'o', '', '', '', 'x']
dangerPos6 = ['', '', '', '', '', 'o', 'x', 'x', '', '']
dangerPos7 = ['', '', '', '', '', 'o', 'x', '', 'x', '']
dangerPos8 = ['', 'x', '', '', '', 'o', '', '', 'x', '']
dangerPos9 = ['', '', '', 'x', '', 'o', '', '', 'x', '']

startX = 0
startY = 0
endX = 0
endY = 0

num = 0 + 1
for y in range(1, 4):
    for x in range(1, 4):
        sq = Square(x, y, num)
        square_group.add(sq)
        squares.append(sq)

        num += 1

turn = 'x'

font = p.font.Font(None, 36)


def return_to_menu():
    main_menu()


def start_one_player_game():
    global turn
    turn = 'x'  # Set the turn for one player game
    run = True
    reset_game()
    while run:
        clock.tick(60)
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            elif event.type == p.MOUSEBUTTONDOWN and turn == 'x':
                mx, my = p.mouse.get_pos()
                for s in squares:
                    s.clicked(mx, my)

        Update()
    reset_game()
    return_to_menu()


def start_two_players_game():
    global turn
    turn = 'x'  # Set the turn for two players game
    run = True
    reset_game()
    while run:
        clock.tick(60)
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            elif event.type == p.MOUSEBUTTONDOWN:
                mx, my = p.mouse.get_pos()
                for square in squares:
                    if square.rect.collidepoint(mx, my) and square.content == '':
                        square.content = turn
                        board[square.number] = turn

                        if turn == 'x':
                            square.image = x_image
                            square.image = p.transform.scale(square.image, (square.width, square.height))
                            turn = 'o'
                            checkWinner('x')
                        else:
                            square.image = o_image
                            square.image = p.transform.scale(square.image, (square.width, square.height))
                            turn = 'x'
                            checkWinner('o')

        if '' not in board[1:]:
            time.sleep(2)
            square_group.empty()
            background = p.image.load(r'/OMNIPIVE/Games/tic-tac-toe/Tie Game.png')
            background = p.transform.scale(background, (WIDTH, HEIGHT))
            Update()
            time.sleep(2)
            reset_game()
            return_to_menu()
            break
        Update()


def reset_game():
    global board, turn, won
    board = ['' for i in range(10)]
    turn = 'x'
    won = False
    for square in squares:
        square.content = ''
        square.image = blank_image
        square.image = p.transform.scale(square.image, (square.width, square.height))
    # num = 1
    # for y in range(1, 4):
    #     for x in range(1, 4):
    #         sq = Square(x, y, num)
    #         square_group.add(sq)
    #         squares.append(sq)
    #
    #         num += 1


if __name__ == '__main__':
    main_menu()

