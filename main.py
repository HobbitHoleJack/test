import pygame
from time import sleep
import random
from sys import exit

pygame.init()

# creates window
running = True
screen = pygame.display.set_mode((330, 330))
pygame.display.set_caption("Tic Tac Toe")
screen.fill((255, 255, 255))
pygame.display.update()
icon = pygame.image.load('tictactoe.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 60)
redwin = font.render("Red Won", True, (0, 0, 0,))
bluewin = font.render('Blue Won', True, (0, 0, 0))
draw = font.render('Draw!', True, (0, 0, 0))
cpturn_done = True


def checkwin():
    win = 'null'

    if aa_s == 'X' and ab_s == 'X' and ac_s == 'X':
        win = 'red'

    if ba_s == 'X' and bb_s == 'X' and bc_s == 'X':
        win = 'red'

    if ca_s == 'X' and cb_s == 'X' and cc_s == 'X':
        win = 'red'

    if aa_s == 'X' and ba_s == 'X' and ca_s == 'X':
        win = 'red'

    if ab_s == 'X' and bb_s == 'X' and cb_s == 'X':
        win = 'red'

    if ac_s == 'X' and bc_s == 'X' and cc_s == 'X':
        win = 'red'

    if aa_s == 'X' and bb_s == 'X' and cc_s == 'X':
        win = 'red'

    if ac_s == 'X' and bb_s == 'X' and ca_s == 'X':
        win = 'red'

    if aa_s == 'O' and ab_s == 'O' and ac_s == 'O':
        win = 'blue'

    if ba_s == 'O' and bb_s == 'O' and bc_s == 'O':
        win = 'blue'

    if ca_s == 'O' and cb_s == 'O' and cc_s == 'O':
        win = 'blue'

    if aa_s == 'O' and ba_s == 'O' and ca_s == 'O':
        win = 'blue'

    if ab_s == 'O' and bb_s == 'O' and bc_s == 'O':
        win = 'blue'

    if ac_s == 'O' and bc_s == 'O' and cc_s == 'O':
        win = 'blue'

    if aa_s == 'O' and bb_s == 'O' and cc_s == 'O':
        win = 'blue'

    if ac_s == 'O' and bb_s == 'O' and ca_s == 'O':
        win = 'blue'

    if win == 'red':
        print('won Red')
        screen.blit(redwin, (80, 150))
        pygame.display.update()
        pygame.mixer.music.load("success-1-6297.mp3")
        pygame.mixer.music.play()
        sleep(3)
        exit()
    
    if win == 'blue':
        print('won Blue')
        screen.blit(bluewin, (80, 150))
        pygame.display.update()
        pygame.mixer.music.load("success-1-6297.mp3")
        pygame.mixer.music.play()
        sleep(3)
        exit()


# gametime baby lesgo


# notes:
# Red = X, Blue = o


class AA:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165), pygame.Rect(10, 10, 100, 100))


aa = AA()


class BA:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165), pygame.Rect(10, 115, 100, 100))


ba = BA()


class CA:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165), pygame.Rect(10, 220, 100, 100))


ca = CA()


class AB:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165), pygame.Rect(115, 10, 100, 100))


ab = AB()


class BB:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165), pygame.Rect(115, 115, 100, 100))


bb = BB()


class CB:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165), pygame.Rect(115, 220, 100, 100))


cb = CB()


class AC:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165), pygame.Rect(220, 10, 100, 100))


ac = AC()


class BC:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165), pygame.Rect(220, 115, 100, 100))


bc = BC()


class CC:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165), pygame.Rect(220, 220, 100, 100))


cc = CC()

# status of square
aa_s = ""
ab_s = ""
ac_s = ""
ba_s = ""
bb_s = ""
bc_s = ""
ca_s = ""
cb_s = ""
cc_s = ""

turn_done = False
available_squares = ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']

while running:

    for event in pygame.event.get():

        # Makes the X button close the window
        if event.type == pygame.QUIT:
            running = False

        #click events
        if event.type == pygame.MOUSEBUTTONUP:
          if cpturn_done:
            if aa.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse clicked on aa")
                if aa_s == '':
                    AA.self = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 10, 100, 100))
                    aa_s = 'X'
                    turn_done = True
                    available_squares.remove('aa')

            if ab.rect.collidepoint(pygame.mouse.get_pos()):
                print('Mouse Clicked on ab')
                if ab_s == '':
                    AB.self = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(115, 10, 100, 100))
                    ab_s = 'X'
                    turn_done = True
                    available_squares.remove('ab')

            if ac.rect.collidepoint(pygame.mouse.get_pos()):
                print('Mouse Clicked on ac')
                if ac_s == '':
                    AC.self = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(220, 10, 100, 100))
                    ac_s = 'X'
                    turn_done = True
                    available_squares.remove('ac')
            
            if ba.rect.collidepoint(pygame.mouse.get_pos()):
                print('Mouse Clicked on ba')
                if ba_s == '':
                    BA.self = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 115, 100, 100))
                    ba_s = 'X'
                    turn_done = True
                    available_squares.remove('ba')
            
            if bb.rect.collidepoint(pygame.mouse.get_pos()):
                print('Mouse Clicked on bb')
                if bb_s == '':
                  BB.self = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(115, 115, 100, 100))
                  bb_s = 'X'
                  turn_done = True
                  available_squares.remove('bb')

            if bc.rect.collidepoint(pygame.mouse.get_pos()):
                print('Mouse Clicked on bc')
                if bc_s == '':
                  BC.self = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(220, 115, 100, 100))
                  bc_s = 'X'
                  turn_done = True
                  available_squares.remove('bc')
            
            if ca.rect.collidepoint(pygame.mouse.get_pos()):
                print('Mouse Clicked on ca')
                if ca_s == '':
                  CA.self = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 220, 100, 100))
                  ca_s = 'X'
                  turn_done = True
                  available_squares.remove('ca')

            if cb.rect.collidepoint(pygame.mouse.get_pos()):
                print('Mouse Clicked on cb')
                if cb_s == '':
                  CB.self = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(115, 220, 100, 100))
                  cb_s = 'X'
                  turn_done = True
                  available_squares.remove('cb')

            if cc.rect.collidepoint(pygame.mouse.get_pos()):
                print('Mouse Clicked on cc')
                if cc_s == '':
                  CC.self = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(220, 220, 100, 100))
                  cc_s = 'X'
                  turn_done = True
                  available_squares.remove('cc')


    if turn_done:
      #computer time!!!!!!!!!!!
      checkwin()
      if available_squares:

        move = random.choice(available_squares)
        if move == 'aa':
          AA.self = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(10, 10, 100, 100))
          aa_s = 'O'
          available_squares.remove('aa')
          turn_done = False
          pygame.display.update()

        if move == 'ab':
          AB.self = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(115, 10, 100, 100))
          ab_s = 'O'
          available_squares.remove('ab')
          turn_done = False
          pygame.display.update()

        if move == 'ac':
          AC.self = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(220, 10, 100, 100))
          ac_s = 'O'   
          available_squares.remove('ac')
          turn_done = False
          pygame.display.update()

        if move == 'ba':
          BA.self = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(10, 115, 100, 100))
          ba_s = 'O'
          available_squares.remove('ba')
          turn_done = False
          pygame.display.update()
        if move == 'bb':
          BB.self = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(115, 115, 100, 100))
          bb_s = 'O'
          available_squares.remove('bb')
          turn_done = False
          pygame.display.update()
        if move == 'bc':
          BC.self = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(220, 115, 100, 100))
          bc_s = 'O'
          available_squares.remove('bc')
          turn_done = False
          pygame.display.update()
        if move == 'ca':
          CA.self = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(10, 220, 100, 100))
          ca_s = 'O'
          available_squares.remove('ca')
          turn_done = False
          pygame.display.update()
        if move == 'cb':
          CB.self = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(115, 220, 100, 100))
          cb_s = 'O'
          available_squares.remove('cb')
          turn_done = False
          pygame.display.update()
        if move == 'cc':
          CC.self = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(220, 220, 100, 100))
          cc_s = 'O'
          available_squares.remove('cc')
          turn_done = False
          cpturn_done = True
          pygame.display.update()
      else:
        screen.blit(draw, (110, 150))
        pygame.display.update()
        pygame.mixer.music.load("success-1-6297.mp3")
        pygame.mixer.music.play()
        sleep(3)
        exit()
    # Updates
    checkwin()
    pygame.display.update()
    clock.tick(60)
