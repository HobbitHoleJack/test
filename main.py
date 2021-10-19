import pygame
from time import sleep
pygame.init()

#creates window
screen = pygame.display.set_mode((330, 330))
pygame.display.set_caption("Tic Tac Toe")
screen.fill((255, 255, 255))
pygame.display.update()
icon = pygame.image.load('tictactoe.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 60)
redwin = font.render("Red Won", True, (0, 128, 0))
bluewin = font.render('Blue Won', True, (0, 128, 0))
#gametime baby lesgo


#notes:
# Red = X, Blue = o


class AA:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165),
                                     pygame.Rect(10, 10, 100, 100))


aa = AA()


class BA:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165),
                                     pygame.Rect(10, 115, 100, 100))


ba = BA()


class CA:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165),
                                     pygame.Rect(10, 220, 100, 100))


ca = CA()


class AB:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165),
                                     pygame.Rect(115, 10, 100, 100))


ab = AB()


class BB:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165),
                                     pygame.Rect(115, 115, 100, 100))


bb = BB()


class CB:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165),
                                     pygame.Rect(115, 220, 100, 100))


cb = CB()


class AC:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165),
                                     pygame.Rect(220, 10, 100, 100))


ac = AC()


class BC:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165),
                                     pygame.Rect(220, 115, 100, 100))


bc = BC()


class CC:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (199, 195, 165),
                                     pygame.Rect(220, 220, 100, 100))


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


running = True
while running:

    for event in pygame.event.get():

        #Makes the X button close the window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if aa.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse clicked on aa")
                if aa_s == '':
                    AA.self = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 10, 100, 100))
                    aa_s = 'X'

            if ab.rect.collidepoint(pygame.mouse.get_pos()):
              print('Mouse Clicked on ab')
              if ab_s == '':
                AB.self = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(115, 10, 100, 100))
                ab_s = 'X'

            if ac.rect.collidepoint(pygame.mouse.get_pos()):
              print('Mouse Clicked on ac')
              if ac_s == '':
                AC.self = pygame.draw.rect(screen, (255, 0, 0),
                                     pygame.Rect(220, 10, 100, 100))
                ac_s = 'X'
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
      sleep(4)
      break
    if win == False:
      print('won Blue')
      screen.blit(bluewin, (80,150))
      pygame.display.update()
      sleep(4)
      break
    clock.tick(30)

