# Import pygame
import pygame
from pygame.locals import *

# Declare neccessary global variables
global cnum  # number of carbon atoms
global hnum  # number of hydrogen atoms
global strcnum  # versions of hnum and cnum as string for typing
global strhnum
global selected
selected = ""
cnum = 1  # minimum values for hydrogen and carbon
hnum = 4
strcnum = str(cnum)  # creating the string versions of hnum and cnum
strhnum = str(hnum)

pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Fonts used in text displays
pygame.display.set_caption('Show Text')
titlefont = pygame.font.Font('freesansbold.ttf', 60)
menufont = pygame.font.Font('freesansbold.ttf', 50)
nextfont = pygame.font.Font('freesansbold.ttf', 40)
surveyfont = pygame.font.Font('freesansbold.ttf', 25)

# Colors used in displays
white = (255, 255, 255)
black = (0, 0, 0)
gray = (112, 129, 140)
lgray = (141, 154, 163)
pgray = (222, 214, 203)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (59, 175, 247)
yellow = (255, 255, 0)

# Game Framerate
clock = pygame.time.Clock()
FPS = 30

# Initial value for the screen number
global screenselect
screenselect = 1

# Initial value for the chain number (used where there is more than one hydrocarbon possible)
global chainnum
chainnum = 1


# Main loop that determines what screen is displayed
def main_loop():
    mainloop = True  # This will remain true up until pygame is quit
    while mainloop:
        getpos()  # Assists in creating boundaries for displays
        if screenselect == 1:  # Default welcome page
            homeui()
        elif screenselect == 2:  # Survey page - entered through home page and leads to display page
            surveyui()
        elif screenselect == 3:  # Display page - entered through survey page and leads to home page or survey page
            displayui()

        pygame.display.update()  # Updates the on-screen display
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection"
                                   )  # Sets the caption of the pygame window


# Display data for the home page
def homeui():
    homeinteractions()

    selected = ""  # Selected defines where the cursor is hovering over
    if x >= 340 and y >= 300 and x <= 460 and y <= 350:  # These are the start button parameters
        selected = "start"
    elif x >= 345 and y >= 360 and x <= 455 and y <= 410:  # These are the quit button parameters
        selected = "quit"
    screen.fill(gray)  # Create the basic background

    # This will determine the fonts and contents of each block of text
    # variable = font type(word to be printed, antialiasing, letter colour, highlighter colour)
    title = titlefont.render('Welcome', True, blue)
    if selected == "start":
        text_start = menufont.render('Start', True, white, lgray)
    else:
        text_start = menufont.render('Start', True, black)
    if selected == "quit":
        text_quit = menufont.render('Quit', True, white, lgray)
    else:
        text_quit = menufont.render('Quit', True, black)

    # Gets the length of each of the text blocks for positioning
    title_rect = title.get_rect()
    start_rect = text_start.get_rect()
    quit_rect = text_quit.get_rect()

    # Places the text centre to the screen at the given y position
    screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
    screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 300))
    screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 360))


# Possible events in the home screen
def homeinteractions():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit pygame
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 345 and y >= 360 and x <= 455 and y <= 410:  # Selected quit button on the home screen
            pygame.quit()  # Quit pygame
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 340 and y >= 300 and x <= 460 and y <= 350:  # Selected start button on the home screen
            global screenselect
            screenselect = 2  # Move over to the survey page


def surveyui():
    surveyinteractions()

    global flag
    flag = False  # flag is checked before moving onto the next page and to highlight incorrect inputs
    if hnum == (cnum * 2) + 2:
        flag = False
    elif hnum == cnum * 2:
        flag = False
    elif hnum == cnum and cnum >= 6:
        flag = False
    else:
        flag = True  # If the hydrocarbon is invalid, flag is set to true

    selected = ""  # Selected defines where the cursor is hovering over
    if x >= 500 and y >= 125 and x <= 515 and y <= 150:
        selected = "upcnum"
    elif x >= 500 and y >= 155 and x <= 515 and y <= 180:
        selected = "downcnum"
    elif x >= 500 and y >= 205 and x <= 515 and y <= 230:
        selected = "uphnum"
    elif x >= 500 and y >= 235 and x <= 515 and y <= 260:
        selected = "downhnum"
    elif x >= 60 and y >= 30 and x <= 135 and y <= 70:
        selected = "last"
    elif x >= 655 and y >= 30 and x <= 740 and y <= 70:
        selected = "next"
    # This will determine the fonts and contents of each block of text
    # variable = font type(word to be printed, antialiasing, letter colour, highlighter colour)
    if selected == "upcnum":
        text_upcnum = surveyfont.render('^', True, white, lgray)
    else:
        text_upcnum = surveyfont.render('^', True, black, gray)

    if selected == "downcnum":
        text_downcnum = surveyfont.render('v', True, white, lgray)
    else:
        text_downcnum = surveyfont.render('v', True, black, gray)

    if selected == "uphnum":
        text_uphnum = surveyfont.render('^', True, white, lgray)
    else:
        text_uphnum = surveyfont.render('^', True, black, gray)

    if selected == "downhnum":
        text_downhnum = surveyfont.render('v', True, white, lgray)
    else:
        text_downhnum = surveyfont.render('v', True, black, gray)

    screen.fill(pgray)  # Create the basic background

    title = titlefont.render('Survey Page', True, black)
    if selected == "next" and flag is False:
        nextpage = nextfont.render('Next', True, white, lgray)
    else:
        nextpage = nextfont.render('Next', True, black, gray)
    if selected == "last":
        previouspage = nextfont.render('Last', True, white, lgray)
    else:
        previouspage = nextfont.render('Last', True, black, gray)

    title_rect = title.get_rect()
    nextpage_rect = nextpage.get_rect()
    previouspage_rect = previouspage.get_rect()

    screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 30))
    screen.blit(
        nextpage,
        (screen_width - (screen_width / 8) - (nextpage_rect[2] / 2), 30))
    screen.blit(previouspage,
                (screen_width / 8 - (previouspage_rect[2] / 2), 30))

    global strcnum
    global strhnum
    strcnum = str(cnum)
    strhnum = str(hnum)

    text_cnum = surveyfont.render('Number of carbon atoms: ' + strcnum, True,
                                  black)

    if flag is False:
        text_hnum = surveyfont.render('Number of hydrogen atoms: ' + strhnum,
                                      True, black)
    else:
        text_hnum = surveyfont.render('Number of hydrogen atoms: ' + strhnum,
                                      True, black, red)

    # Main Menu Text
    screen.blit(text_cnum, (40, 140))
    screen.blit(text_hnum, (40, 220))
    screen.blit(text_upcnum, (500, 125))
    screen.blit(text_downcnum, (500, 155))
    screen.blit(text_uphnum, (500, 205))
    screen.blit(text_downhnum, (500, 235))


def surveyinteractions():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 500 and y >= 125 and x <= 515 and y <= 150:
            global cnum  #
            if cnum < 6:
                cnum = cnum + 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 500 and y >= 155 and x <= 515 and y <= 180:
            if cnum > 1:
                cnum = cnum - 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 500 and y >= 205 and x <= 515 and y <= 230:
            global hnum
            if hnum < (cnum * 2) + 2:
                hnum = hnum + 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 500 and y >= 235 and x <= 515 and y <= 260:
            if hnum > 4:
                hnum = hnum - 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 655 and y >= 30 and x <= 740 and y <= 70:
            if flag is False:
                global screenselect
                screenselect = 3
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 60 and y >= 30 and x <= 135 and y <= 70:
            screenselect = 1


def displayui():
    displayinteractions()
    selected = ""
    if x >= 60 and y >= 30 and x <= 135 and y <= 70:
        selected = "last"
    elif x >= 655 and y >= 30 and x <= 740 and y <= 70:
        selected = "home"
    elif x >= 280 and y >= 500 and x <= 295 and y <= 525:
        selected = "nextchain"
    elif x >= 160 and y >= 500 and x <= 175 and y <= 525:
        selected = "lastchain"

    screen.fill(pgray)
    pygame.draw.rect(screen, white,
                     ((screen_width / 3.5 - 450 / 2), 100, 450, 400))
    main()
    title = titlefont.render('Display Page', True, black)
    if selected == "home":
        homepage = nextfont.render('Home', True, white, lgray)
    else:
        homepage = nextfont.render('Home', True, black, gray)
    if selected == "last":
        previouspage = nextfont.render('Last', True, white, lgray)
    else:
        previouspage = nextfont.render('Last', True, black, gray)

    if hnum == cnum * 2:
        if selected == "nextchain":
            nextchain = surveyfont.render('>', True, white, lgray)
        else:
            nextchain = surveyfont.render('>', True, black, gray)
        if selected == "lastchain":
            lastchain = surveyfont.render('<', True, white, lgray)
        else:
            lastchain = surveyfont.render('<', True, black, gray)

        nextchain_rect = nextchain.get_rect()
        lastchain_rect = lastchain.get_rect()
        screen.blit(nextchain,
                    (screen_width / 3.5 - (nextchain_rect[2] / 2 - 60), 500))
        screen.blit(lastchain,
                    (screen_width / 3.5 - (lastchain_rect[2] / 2 + 60), 500))
        chainmax = cnum // 2
        chainmaxstr = str(chainmax)
        chainnumstr = str(chainnum)
        chaincount = surveyfont.render(chainnumstr + " / " + chainmaxstr, True,
                                       black)

        chaincount_rect = chaincount.get_rect()
        screen.blit(chaincount,
                    (screen_width / 3.5 - (chaincount_rect[2] / 2), 500))

    title_rect = title.get_rect()
    homepage_rect = homepage.get_rect()
    previouspage_rect = previouspage.get_rect()

    screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 30))
    screen.blit(
        homepage,
        (screen_width - (screen_width / 8) - (homepage_rect[2] / 2), 30))
    screen.blit(previouspage,
                (screen_width / 8 - (previouspage_rect[2] / 2), 30))


def displayinteractions():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 655 and y >= 30 and x <= 740 and y <= 70:
            global screenselect
            screenselect = 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 60 and y >= 30 and x <= 135 and y <= 70:
            screenselect = 2
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 160 and y >= 500 and x <= 175 and y <= 525:
            global chainnum
            if chainnum > 1:
                chainnum = chainnum - 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 280 and y >= 500 and x <= 295 and y <= 525:
            if chainnum < cnum // 2:
                chainnum = chainnum + 1


def getpos():
    global x
    global y
    x, y = pygame.mouse.get_pos()
    print(x, y)


# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================


def main():
    startpos()
    definechain()


def startpos():
    global array
    global rowlen
    array = []
    rowlen = (cnum * 2) + 3
    for i in range(5):
        array.append([" "] * rowlen)
    global startposy
    global startposx
    startposy = (5 // 2)
    startposx = (rowlen // 2)


def createchain():
    array[startposy][0] = "H"
    array[startposy][rowlen - 1] = "H"
    array[startposy][startposx + cnum] = "—"

    for x in range(cnum):
        array[startposy][(2 * x) + 2] = "C"
        array[startposy + 1][(2 * x) + 2] = "|"
        array[startposy - 1][(2 * x) + 2] = "|"
        array[startposy - 2][(2 * x) + 2] = "H"
        array[startposy + 2][(2 * x) + 2] = "H"
        array[startposy][(2 * x) + 1] = "—"


def definechain():
    if hnum == (cnum * 2) + 2:
        createchain()
        printchain()
    elif hnum == cnum * 2:
        createchain()
        alkene()
        printchain()
    elif hnum == cnum and cnum >= 6:
        cyclic()


def alkene():
    array[startposy][(2 * chainnum) + 1] = "="
    array[startposy - 2][(2 * chainnum) + 2] = " "
    array[startposy - 2][2 * chainnum] = " "
    array[startposy - 1][(2 * chainnum) + 2] = " "
    array[startposy - 1][2 * chainnum] = " "


def printchain():
    offsety = 0
    for row in array:
        offsetx = -2
        offsetx = offsetx * cnum
        for elem in row:
            if elem == "|":
                offsetx = offsetx + 5
            if elem == "—":
                offsety = offsety - 2
                offsetx = offsetx - 2
            offsetx = offsetx + 30
            if elem == "|":
                offsetx = offsetx - 5
            if elem == "—":
                offsety = offsety + 2
                offsetx = offsetx + 2
        offsety = offsety + 30

    spx = screen_width // 3.5 - offsetx // 2
    spy = screen_height // 2 - offsety // 2

    offsety = 0
    for row in array:
        offsetx = 0
        for elem in row:
            if elem == "|":
                offsetx = offsetx + 5
            if elem == "—":
                offsety = offsety - 2
                offsetx = offsetx - 2
            variablefontsize = 25
            character = surveyfont.render(elem, True, black)
            screen.blit(character, (spx + offsetx, spy + offsety))
            offsetx = offsetx + 30
            if elem == "|":
                offsetx = offsetx - 5
            if elem == "—":
                offsety = offsety + 2
                offsetx = offsetx + 2
        offsety = offsety + 30


def cyclic():
    pass


main_loop()
pygame.quit()
quit()
