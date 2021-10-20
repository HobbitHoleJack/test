import pygame
from time import sleep
import random

pygame.init()

# creates window
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

win = 'null'
turn_done = False
available_squares = ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']

running = True
while running:

    for event in pygame.event.get():

        # Makes the X button close the window
        if event.type == pygame.QUIT:
            running = False

        #click events
        if event.type == pygame.MOUSEBUTTONUP:
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
      move = random.choice(available_squares)
      if move == aa:
        AA.self = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(10, 10, 100, 100))
        aa_s = 'O'
        available_squares.remove('aa')

      if move == ab:
        AB.self = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(115, 10, 100, 100))
        ab_s = 'O'
        available_squares.remove('ab')
      if move == ac:
      if move == ba:
      if move == bb:
      if move == bc:
      if move == ca:
      if move == cb:
      if move == cc:
    # Updates
    pygame.display.update()
    if aa_s and ab_s and ac_s == 'X':
        win = True

    if ba_s and bb_s and bc_s == 'X':
        win = True

    if ca_s and cb_s and cc_s == 'X':
        win = True

    if aa_s and ba_s and ca_s == 'X':
        win = True

    if ab_s and bb_s and bc_s == 'X':
        win = True

    if ac_s and bc_s and cc_s == 'X':
        win = True

    if aa_s and bb_s and cc_s == 'X':
        win = True

    if ac_s and bb_s and ca_s == 'X':
        win = True

    if aa_s and ab_s and ac_s == 'O':
        win = False

    if ba_s and bb_s and bc_s == 'O':
        win = False

    if ca_s and cb_s and cc_s == 'O':
        win = False

    if aa_s and ba_s and ca_s == 'O':
        win = False

    if ab_s and bb_s and bc_s == 'O':
        win = False

    if ac_s and bc_s and cc_s == 'O':
        win = False

    if aa_s and bb_s and cc_s == 'O':
        win = False

    if ac_s and bb_s and ca_s == 'O':
        win = False



    if win == True:
        print('won Red')
        screen.blit(redwin, (80, 150))
        pygame.display.update()
        pygame.mixer.music.load("success-1-6297.mp3")
        pygame.mixer.music.play()
        sleep(3)
        break

    if win == False:
        print('won Blue')
        screen.blit(bluewin, (80, 150))
        pygame.display.update()
        pygame.mixer.music.load("success-1-6297.mp3")
        pygame.mixer.music.play()
        sleep(3)
        break
    clock.tick(60)
