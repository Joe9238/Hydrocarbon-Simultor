# Import pygame
from math import cos, sin, pi
import pygame

# Declare necessary global variables
global carbonNumber
global hydrogenNumber
global carbonNumberBranched
global branchList
global dataID
dataID = -1
carbonNumber = 1
hydrogenNumber = 4
carbonNumberBranched = 1
branchList = []

pygame.init()

# Screen dimensions
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Fonts used in text displays
pygame.display.set_caption('Show Text')
titleFont = pygame.font.SysFont('arial.ttf', 80)
menuFont = pygame.font.SysFont('arial.ttf', 75)
nextFont = pygame.font.SysFont('arial.ttf', 60)
surveyFont = pygame.font.SysFont('arial.ttf', 35)
informationFont = pygame.font.SysFont('arial.ttf', 27)
subscriptFont = pygame.font.SysFont('arial.ttf', 18)

# Colors used in displays
white = (255, 255, 255)
black = (0, 0, 0)
gray = (112, 129, 140)
lightGray = (141, 154, 163)
veryLightGray = (222, 214, 203)
red = (255, 0, 0)
lightRed = (242, 68, 68)
green = (0, 255, 0)
lightGreen = (113, 227, 113)
blue = (59, 175, 247)
yellow = (255, 255, 0)

# Game Framerate
clock = pygame.time.Clock()
FPS = 30

# Initial value for the chain number (used where there is more than one hydrocarbon possible)
global stereoisomerNumber
stereoisomerNumber = 1


# Main loop that determines what screen is displayed
def mainLoop():
    doLoop = True  # This will remain true up until pygame is quit
    readData()

    # Initial value for the screen number
    global screenID
    screenID = 1
    while doLoop:
        getCoordinates()  # Assists in creating boundaries for displays
        if screenID == 1:  # Default welcome page
            homeUI()
        elif screenID == 2:  # Survey page - entered through home page and leads to display page
            surveyUI()
        elif screenID == 3:  # Display page - entered through survey page and leads to home page or survey page
            displayUI()
        elif screenID == 4:
            savedUI()
        elif screenID == 5:
            branchedUI()

        pygame.display.update()  # Updates the on-screen display
        clock.tick(FPS)
        pygame.display.set_caption("Hydrocarbon Generator - Joe Maskell"
                                   )  # Sets the caption of the pygame window


# Display data for the home page
def homeUI():
    # Call other functions that need to be run on this page
    homeInteractions()
    global branchList
    branchList = []
    # Determine what the cursor is hovering over
    selected = ""
    if x >= 340 and y >= 300 and x <= 460 and y <= 350:
        selected = "start"
    elif x >= 325 and y >= 360 and x <= 475 and y <= 410:
        selected = "saved"
    elif x >= 345 and y >= 420 and x <= 455 and y <= 470:
        selected = "quit"

    # Set out colours/sections on screen
    screen.fill(gray)

    # Determine text appearance
    if selected == "start":
        startText = menuFont.render('Start', True, white, lightGray)
    else:
        startText = menuFont.render('Start', True, black)

    if selected == "quit":
        quitText = menuFont.render('Quit', True, white, lightGray)
    else:
        quitText = menuFont.render('Quit', True, black)

    if selected == "saved":
        savedText = menuFont.render('Saved', True, white, lightGray)
    else:
        savedText = menuFont.render('Saved', True, black)

    titleText = titleFont.render('Hydrocarbon Generator', True, blue)

    # Determine the length of each text block for positioning
    titleTextRect = titleText.get_rect()
    startTextRect = startText.get_rect()
    quitTextRect = quitText.get_rect()
    savedTextRect = savedText.get_rect()

    # Place the text on the screen
    screen.blit(titleText, (screenWidth / 2 - (titleTextRect[2] / 2), 80))
    screen.blit(startText, (screenWidth / 2 - (startTextRect[2] / 2), 300))
    screen.blit(quitText, (screenWidth / 2 - (quitTextRect[2] / 2), 420))
    screen.blit(savedText, (screenWidth / 2 - (savedTextRect[2] / 2), 360))


# Possible events for the main menu
def homeInteractions():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit pygame
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 345 and y >= 420 and x <= 455 and y <= 470:  # Selected quit button
            pygame.quit()  # Quit pygame
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 340 and y >= 300 and x <= 460 and y <= 350:  # Selected start button
            global screenID
            global cyclic
            global branched
            branched = False
            cyclic = False
            screenID = 2  # Move over to the survey page
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 325 and y >= 360 and x <= 475 and y <= 410:  # Selected saved button
            screenID = 4  # Move over to the saved page


# Display data for the saved page
def savedUI():
    # Call other functions that need to be run on this page
    savedInteractions()

    # Determine what the cursor is hovering over
    selected = ""
    if x >= 645 and y >= 30 and x <= 760 and y <= 70:
        selected = "home"

    # Set out colours/sections on screen
    screen.fill(gray)

    pygame.draw.line(screen, black, (0, 97), (screenWidth, 97))
    pygame.draw.line(screen, black, (675, 70), (675, 570))
    pygame.draw.line(screen, black, (250, 70), (250, 570))
    pygame.draw.line(screen, black, (410, 70), (410, 570))
    pygame.draw.line(screen, black, (535, 70), (535, 570))
    pygame.draw.line(screen, black, (130, 70), (130, 570))
    for i in range(8):
        pygame.draw.line(screen, black, (0, 150 + (i * 60)),
                         (screenWidth, 150 + (i * 60)))

    # Determine text appearance
    if selected == "home":
        homeText = nextFont.render('Home', True, white, lightGray)
    else:
        homeText = nextFont.render('Home', True, black)

    carbonsText = surveyFont.render('Carbons', True, black)
    viewText = surveyFont.render('View', True, black)
    removeText = surveyFont.render('Remove', True, black)
    cyclicValueText = surveyFont.render('Cyclic', True, black)
    branchedValueText = surveyFont.render('Branched', True, black)
    limitText = surveyFont.render('You can save a maximum of 8 hydrocarbons.',
                                  True, black)
    hydrogensText = surveyFont.render('Hydrogens', True, black)

    # Determine the length of each text block for positioning
    homeTextRect = homeText.get_rect()
    removeTextRect = removeText.get_rect()
    viewTextRect = viewText.get_rect()
    branchedValueTextRect = branchedValueText.get_rect()
    cyclicValueTextRect = cyclicValueText.get_rect()
    carbonsTextRect = carbonsText.get_rect()
    hydrogensTextRect = hydrogensText.get_rect()
    limitTextRect = limitText.get_rect()

    # Place the text on the screen
    screen.blit(homeText,
                (screenWidth - (screenWidth / 8) - (homeTextRect[2] / 2), 30))
    screen.blit(branchedValueText,
                ((screenWidth / 8) - (branchedValueTextRect[2] / 2) + 510, 70))
    screen.blit(viewText,
                ((screenWidth / 8) - (viewTextRect[2] / 2) + 635, 70))
    screen.blit(removeText,
                ((screenWidth / 8) - (removeTextRect[2] / 2) - 35, 70))
    screen.blit(cyclicValueText,
                ((screenWidth / 8) - (cyclicValueTextRect[2] / 2) + 370, 70))
    screen.blit(carbonsText,
                ((screenWidth / 8) - (carbonsTextRect[2] / 2) + 90, 70))
    screen.blit(hydrogensText,
                ((screenWidth / 8) - (hydrogensTextRect[2] / 2) + 230, 70))
    screen.blit(limitText, ((screenWidth / 2) - (limitTextRect[2] / 2), 573))

    # Create and place the text from the list onto the screen
    global savedList
    for a in range(len(savedList)):
        dataList = savedList[a].split()
        for i in range(4):
            data = dataList[i]
            if data == "True":
                data = "Yes"
            elif data == "False":
                data = "No"
            dataText = nextFont.render(data, True, black)
            dataTextRect = dataText.get_rect()
            screen.blit(dataText,
                        ((screenWidth / 8) - (dataTextRect[2] / 2) + (i * 140) + 90,
                         100 + (a * 60)))

    # Create and place the + and - buttons onto the screen
    for i in range(8):
        removeText = nextFont.render(" - ", True, red)
        addText = nextFont.render(" + ", True, green)
        if x >= 40 and y > 90 + (i * 60) and x <= 80 and y < 150 + (i * 60):
            removeText = nextFont.render(" - ", True, red, lightRed)
        elif x >= 720 and y > 90 + (
                i * 60) and x <= screenWidth - 35 and y < 150 + (i * 60):
            addText = nextFont.render(" + ", True, green, lightGreen)
        screen.blit(removeText, (40, 100 + (60 * i)))
        screen.blit(addText, (720, 100 + (60 * i)))


# Possible events for the saved page
def savedInteractions():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit pygame
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 645 and y >= 30 and x <= 760 and y <= 70:  # Selected home button
            global screenID
            screenID = 1  # Move over to the main menu
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 40 and y >= 90 and x <= 80 and y <= 630:  # Selected - button
            removeData()  # remove data
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 720 and y >= 90 and x <= screenWidth - 35 and y <= 630:
            goToSave()  # Go to the display page with saved settings


def branchedUI():
    # Call other functions that need to be run on this page
    branchedInteractions()
    hydrocarbonCheck()

    # Determine what the cursor is hovering over
    selected = ""
    if x >= 60 and y >= 30 and x <= 135 and y <= 70:
        selected = "last"
    elif x >= 655 and y >= 30 and x <= 740 and y <= 70:
        selected = "next"
    elif x >= 420 and y >= 125 and x <= 435 and y <= 150:
        selected = "upcnum"
    elif x >= 420 and y >= 155 and x <= 435 and y <= 180:
        selected = "downcnum"
    elif x >= 40 and y >= 300 and x <= 125 and y <= 325:
        selected = "submit"
    elif x >= 235 and y >= 220 and x <= 315 and y <= 245:
        selected = "branch"

    # Set out colours/sections on screen
    screen.fill(veryLightGray)

    # Get needed variables for hydrocarbon-variable-related texts
    global carbonNumberBranched
    carbonNumberBranchedStr = str(carbonNumberBranched)

    # Determine text appearance
    if selected == "next":
        nextText = nextFont.render('Next', True, white, lightGray)
    else:
        nextText = nextFont.render('Next', True, black, gray)

    if selected == "last":
        lastText = nextFont.render('Last', True, white, lightGray)
    else:
        lastText = nextFont.render('Last', True, black, gray)

    if selected == "upcnum":
        increaseCarbonsText = surveyFont.render('^', True, white, lightGray)
    else:
        increaseCarbonsText = surveyFont.render('^', True, black, gray)

    if selected == "downcnum":
        decreaseCarbonsText = surveyFont.render('v', True, white, lightGray)
    else:
        decreaseCarbonsText = surveyFont.render('v', True, black, gray)

    if selected == "submit":
        submitText = surveyFont.render('Submit', True, white, lightGray)
    else:
        submitText = surveyFont.render('Submit', True, black, gray)

    carbonNumberText = surveyFont.render(
        'Number of carbon atoms: ' + carbonNumberBranchedStr, True, black)

    # Determine the length of each text block for positioning
    nextTextRect = nextText.get_rect()
    lastTextRect = lastText.get_rect()

    # Place the text on the screen
    screen.blit(nextText,
                (screenWidth - (screenWidth / 8) - (nextTextRect[2] / 2), 30))
    screen.blit(lastText, (screenWidth / 8 - (lastTextRect[2] / 2), 30))
    screen.blit(carbonNumberText, (40, 140))
    screen.blit(submitText, (40, 300))
    screen.blit(increaseCarbonsText, (420, 125))
    screen.blit(decreaseCarbonsText, (420, 155))

    global branchList
    for i in range(len(branchList)):
        data = str(branchList[i])
        dataText = nextFont.render(data, True, black)
        dataTextRect = dataText.get_rect()
        screen.blit(
            dataText,
            ((screenWidth - (screenWidth / 3) - (dataTextRect[2] / 2) + 140),
             140 + (60 * i)))

    # Create and place the - buttons onto the screen
    for i in range(len(branchList)):
        removeText = nextFont.render(" - ", True, red)
        if x >= 755 and y > 130 + (i * 60) and x <= screenWidth and y < 190 + (
                i * 60):
            removeText = nextFont.render(" - ", True, red, lightRed)
        screen.blit(removeText, (758, 140 + (60 * i)))


def branchedInteractions():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit pygame
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 655 and y >= 30 and x <= 740 and y <= 70:  # Selected next button
            global screenID
            while len(branchList) != carbonNumber:
                branchList.append(0)
            screenID = 3  # Move over to the display page
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 60 and y >= 30 and x <= 135 and y <= 70:  # Selected last button
            screenID = 2  # Move over to the survey page
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 420 and y >= 125 and x <= 435 and y <= 150:  # Selected increase carbons button
            global carbonNumberBranched
            if carbonNumberBranched < 3:  # Increase carbons if the number of carbons is less than 3
                carbonNumberBranched = carbonNumberBranched + 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 420 and y >= 155 and x <= 435 and y <= 180:  # Selected decrease carbons button
            if carbonNumberBranched > 0:  # Decrease carbons if the number of carbons is more than 0
                carbonNumberBranched = carbonNumberBranched - 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 755 and y >= 130 and x <= screenWidth and y <= 670:  # Selected - button
            removeBranch()  # remove data
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 40 and y >= 300 and x <= 125 and y <= 325:
            submitBranch()


def checkMax():
    global cyclic
    global carbonNumber
    global overMaximum
    branchList.append(carbonNumberBranched)
    for i in range(len(branchList)):
        branchList[i] = int(branchList[i])
    overMaximum = False
    if cyclic == True:
        maxList = []
        for i in range(carbonNumber):
            maxList.append(3)
    elif carbonNumber == 3:
        maxList = [1]
    elif carbonNumber == 4:
        maxList = [1, 1]
    elif carbonNumber == 5:
        maxList = [1, 2, 1]
    elif carbonNumber == 6:
        maxList = [1, 2, 2, 1]
    if len(branchList) <= len(maxList):
        for i in range(len(branchList)):
            if branchList[i] > maxList[i]:
                overMaximum = True
    else:
        overMaximum = True
    branchList.pop()


def submitBranch():
    global carbonNumberBranched
    global savedList
    global cyclic
    global branched
    global dataID
    cyclicStr = str(cyclic)
    branchedStr = str(branched)
    checkMax()
    global overMaximum
    if overMaximum == False:
        try:
            dataID = dataID + 1
            dataID = dataID - 1
        except Exception:
            dataID = -1
        finally:
            branchList.append(carbonNumberBranched)
            branchListStr = ""
            for i in range(len(branchList)):
                branchListStr = branchListStr + str(branchList[i]) + " "
        savedList[
            dataID] = carbonNumberStr + " " + hydrogenNumberStr + " " + cyclicStr + " " + branchedStr + " " + branchListStr
        with open(
                "savedData.txt", mode="w", encoding="utf-8"
        ) as my_file:  # Saves new data to ensure its read correctly upon sudden exit
            for data in savedList:
                my_file.write(data + "\n")


def removeBranch():
    try:
        doNotSave = False
        branchList.pop(
            (y - 140) // 60
        )  # Identifies the list number based upon the coordinate of the button
    except:
        doNotSave = True
    finally:
        if doNotSave == False:
            global savedList
            global cyclic
            global branched
            global dataID
            cyclicStr = str(cyclic)
            branchedStr = str(branched)
            branchListStr = ""
            for i in range(len(branchList)):
                branchListStr = branchListStr + str(branchList[i]) + " "
            savedList[
                dataID] = carbonNumberStr + " " + hydrogenNumberStr + " " + cyclicStr + " " + branchedStr + " " + branchListStr

            with open(
                    "savedData.txt", mode="w", encoding="utf-8"
            ) as my_file:  # Saves new data to ensure its read correctly upon sudden exit
                for data in savedList:
                    my_file.write(data + "\n")


# Shows the display page with saved settings
def goToSave():
    # The try command will catch out invalid saves
    try:
        # Determine the position of the data
        global dataID
        dataID = ((y - 100) // 60)
        dataList = savedList[dataID].split()

        # Copy the saved data to the hydrocarbon variables
        global carbonNumber
        global hydrogenNumber
        global carbonNumberStr
        global hydrogenNumberStr
        global cyclic
        global branched
        global skeletal
        global saved
        global branchList
        saved = True
        skeletal = False
        carbonNumber = int(dataList[0])
        hydrogenNumber = int(dataList[1])
        cyclicStr = str(dataList[2])
        branchedStr = str(dataList[3])

        dataPoint = 4
        for i in range((len(dataList)) - 4):
            branchList.append(int(dataList[dataPoint]))
            dataPoint = dataPoint + 1

        if cyclicStr == "True":
            cyclic = True
        elif cyclicStr == "False":
            cyclic = False
        else:
            cyclic = False  # Just in case the value is incorrectly saved

        if branchedStr == "True":
            branched = True
        elif branchedStr == "False":
            branched = False
        else:
            branched = False  # Just in case the value is incorrectly saved

        carbonNumberStr = str(carbonNumber)
        hydrogenNumberStr = str(hydrogenNumber)

        # Go to display page
        global screenID
        screenID = 3
    except:
        pass


# Check if the hydrocarbon is valid
def hydrocarbonCheck():
    # If statements go through the list of inputs
    global cannotContinue
    global cyclic
    global branched
    global screenID
    global carbonNumberBranched
    cannotContinue = True

    if screenID == 2:
        if branched == True or cyclic == True:
            if carbonNumber > 2:
                if carbonNumber * 2 == hydrogenNumber:
                    cannotContinue = False
                elif (carbonNumber * 2) + 2 == hydrogenNumber:
                    cannotContinue = False
                elif carbonNumber == hydrogenNumber == 6 and cyclic == True:
                    cannotContinue = False
        else:
            if carbonNumber * 2 == hydrogenNumber:
                cannotContinue = False
            elif (carbonNumber * 2) + 2 == hydrogenNumber:
                cannotContinue = False


def surveyUI():
    # Call other functions that need to be run on this page
    surveyInteractions()
    hydrocarbonCheck()

    # Determine what the cursor is hovering over
    selected = ""
    if x >= 420 and y >= 125 and x <= 435 and y <= 150:
        selected = "upcnum"
    elif x >= 420 and y >= 155 and x <= 435 and y <= 180:
        selected = "downcnum"
    elif x >= 420 and y >= 205 and x <= 435 and y <= 230:
        selected = "uphnum"
    elif x >= 420 and y >= 235 and x <= 435 and y <= 260:
        selected = "downhnum"
    elif x >= 55 and y >= 30 and x <= 140 and y <= 70:
        selected = "last"
    elif x >= 655 and y >= 30 and x <= 745 and y <= 70:
        selected = "next"
    elif x >= 130 and y >= 280 and x <= 170 and y <= 305:
        selected = "cyclic"
    elif x >= 330 and y >= 280 and x <= 370 and y <= 305:
        selected = "branched"

    # Set out colours/sections on screen
    screen.fill(veryLightGray)

    # Get needed variables for hydrocarbon-variable-related texts
    global carbonNumberStr
    global hydrogenNumberStr
    carbonNumberStr = str(carbonNumber)
    hydrogenNumberStr = str(hydrogenNumber)

    # Determine text appearance
    global cyclic
    global branched
    if cyclic == True:
        if selected == "cyclic":
            cyclicChoiceText = surveyFont.render('Yes', True, white,
                                                 lightGreen)
        else:
            cyclicChoiceText = surveyFont.render('Yes', True, black, green)
    else:
        if selected == "cyclic":
            cyclicChoiceText = surveyFont.render('No', True, white, lightRed)
        else:
            cyclicChoiceText = surveyFont.render('No', True, black, red)

    if branched == True:
        if selected == "branched":
            branchedChoiceText = surveyFont.render('Yes', True, white,
                                                   lightGreen)
        else:
            branchedChoiceText = surveyFont.render('Yes', True, black, green)
    else:
        if selected == "branched":
            branchedChoiceText = surveyFont.render('No', True, white, lightRed)
        else:
            branchedChoiceText = surveyFont.render('No', True, black, red)

    if selected == "upcnum":
        increaseCarbonsText = surveyFont.render('^', True, white, lightGray)
    else:
        increaseCarbonsText = surveyFont.render('^', True, black, gray)

    if selected == "downcnum":
        decreaseCarbonsText = surveyFont.render('v', True, white, lightGray)
    else:
        decreaseCarbonsText = surveyFont.render('v', True, black, gray)

    if selected == "uphnum":
        increaseHydrogensText = surveyFont.render('^', True, white, lightGray)
    else:
        increaseHydrogensText = surveyFont.render('^', True, black, gray)

    if selected == "downhnum":
        decreaseHydrogensText = surveyFont.render('v', True, white, lightGray)
    else:
        decreaseHydrogensText = surveyFont.render('v', True, black, gray)

    if selected == "next" and cannotContinue is False:
        nextText = nextFont.render('Next', True, white, lightGray)
    else:
        nextText = nextFont.render('Next', True, black, gray)

    if selected == "last":
        lastText = nextFont.render('Last', True, white, lightGray)
    else:
        lastText = nextFont.render('Last', True, black, gray)

    carbonNumberText = surveyFont.render(
        'Number of carbon atoms: ' + carbonNumberStr, True, black)
    titleText = titleFont.render('Survey Page', True, black)
    hydrogenNumberText = surveyFont.render(
        'Number of hydrogen atoms: ' + hydrogenNumberStr, True, black)
    cyclicText = surveyFont.render("Cyclic:", True, black)
    branchedText = surveyFont.render("Branched:", True, black)

    # Determine the length of each text block for positioning
    titleTextRect = titleText.get_rect()
    nextTextRect = nextText.get_rect()
    lastTextRect = lastText.get_rect()

    # Place the text on the screen
    screen.blit(cyclicText, (40, 280))
    screen.blit(cyclicChoiceText, (130, 280))
    screen.blit(branchedText, (200, 280))
    screen.blit(branchedChoiceText, (330, 280))
    screen.blit(titleText, (screenWidth / 2 - (titleTextRect[2] / 2), 30))
    screen.blit(nextText,
                (screenWidth - (screenWidth / 8) - (nextTextRect[2] / 2), 30))
    screen.blit(lastText, (screenWidth / 8 - (lastTextRect[2] / 2), 30))
    screen.blit(carbonNumberText, (40, 140))
    screen.blit(hydrogenNumberText, (40, 220))
    screen.blit(increaseCarbonsText, (420, 125))
    screen.blit(decreaseCarbonsText, (420, 155))
    screen.blit(increaseHydrogensText, (420, 205))
    screen.blit(decreaseHydrogensText, (420, 235))


def surveyInteractions():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit pygame
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 420 and y >= 125 and x <= 435 and y <= 150:  # Selected increase carbons button
            global carbonNumber
            if carbonNumber < 6:  # Increase carbons if the number of carbons is less than 6
                carbonNumber = carbonNumber + 1
                global branchList
                branchList = []
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 420 and y >= 155 and x <= 435 and y <= 180:  # Selected decrease carbons button
            if carbonNumber > 1:  # Decrease carbons if the number of carbons is more than 1
                carbonNumber = carbonNumber - 1
                branchList = []
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 420 and y >= 205 and x <= 435 and y <= 230:  # Selected increase hydrogens button
            global hydrogenNumber
            if hydrogenNumber < 14:  # Increase hydrogens if the number of hydrogens is less than the maximum
                hydrogenNumber = hydrogenNumber + 1
                branchList = []
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 420 and y >= 235 and x <= 435 and y <= 260:  # Selected decrease hydrogens button
            if hydrogenNumber > 4:  # Decrease hydrogens if the number of hydrogens is more than 1
                hydrogenNumber = hydrogenNumber - 1
                branchList = []
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 655 and y >= 30 and x <= 745 and y <= 70:  # Selected next button
            if cannotContinue == False:  # If able to continue, reset saved variable and go to display page / branched page
                global screenID
                global saved
                global skeletal
                global branched
                saved = False
                skeletal = False
                if branched == True:
                    screenID = 5
                else:
                    screenID = 3
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 55 and y >= 30 and x <= 140 and y <= 70:  # Selected last button
            screenID = 1  # Move over to the main menu
            branchList = []
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 130 and y >= 280 and x <= 170 and y <= 305:  # Selected cyclic button
            global cyclic
            branchList = []
            if cyclic == False:
                cyclic = True
            else:
                cyclic = False
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 330 and y >= 280 and x <= 370 and y <= 305:  # Selected cyclic button
            if branched == False:
                branched = True
            else:
                branched = False


# Generate the name of the hydrocarbon for the title of the display page
def generateName():
    # suffix is based upon carbon : hydrogen ratio
    suffix = ""
    if hydrogenNumber == carbonNumber * 2 or hydrogenNumber == carbonNumber:
        suffix = "ene"
    elif hydrogenNumber == (carbonNumber * 2) + 2:
        suffix = "ane"

    # Prefix is based upon the number of carbons
    global cyclic
    prefix = ""
    if carbonNumber == 1:
        prefix = "meth"
    elif carbonNumber == 2:
        prefix = "eth"
    elif carbonNumber == 3:
        prefix = "prop"
    elif carbonNumber == 4:
        prefix = "but"
    elif carbonNumber == 5:
        prefix = "pent"
    elif carbonNumber == 6:
        prefix = "hex"

    if cyclic == True:
        if carbonNumber == 3:
            prefix = "cycloprop"
        elif carbonNumber == 4:
            prefix = "cyclobut"
        elif carbonNumber == 5:
            prefix = "cyclopent"
        elif carbonNumber == 6:
            if hydrogenNumber == 6:
                prefix = "benz"
            else:
                prefix = "cyclohex"

    if branched == True and cyclic == True:
        branchName = ""
        methCount = 0
        ethCount = 0
        propCount = 0
        shift = 0
        methList = []
        ethList = []
        propList = []
        methList2 = []
        ethList2 = []
        propList2 = []
        branchList2 = branchList[:]

        largestBranch = 0
        for i in range(len(branchList2)):
            if branchList2[i] > largestBranch:
                largestBranch = branchList2[i]

        while branchList2[0] < largestBranch:
            branchList2.insert(0, branchList2.pop())
            shift = shift + 1

        for i in range(len(branchList2)):
            if branchList2[i] == 3:
                propList.append(i + 1)
                propCount = propCount + 1
            if branchList2[i] == 2:
                ethList.append(i + 1)
                ethCount = ethCount + 1
            if branchList2[i] == 1:
                methList.append(i + 1)
                methCount = methCount + 1

        branchList2.insert(0, branchList2.pop())
        branchList2.reverse()
        for i in range(len(branchList2)):
            if branchList2[i] == 3:
                propList2.append(i + 1)
            if branchList2[i] == 2:
                ethList2.append(i + 1)
            if branchList2[i] == 1:
                methList2.append(i + 1)

        total = 0
        total2 = 0
        counterList = []
        counterList2 = []
        for i in range(len(methList)):
            counterList.append(methList[i])
            counterList2.append(methList2[i])

        for i in range(len(ethList)):
            counterList.append(ethList[i])
            counterList2.append(ethList2[i])

        for i in range(len(propList)):
            counterList.append(propList[i])
            counterList2.append(propList2[i])

        for i in range(len(counterList)):
            total = total + counterList[i]
            total2 = total2 + counterList2[i]

        previous = False
        if total <= total2:
            if len(methList) > 0:
                previous = True
                branchName = branchName + str(methList).replace(
                    '[', "").replace("]", "").replace(" ", "") + "-"
                if len(methList) == 1:
                    branchName = branchName + "methyl"
                elif len(methList) == 2:
                    branchName = branchName + "dimethyl"
                elif len(methList) == 3:
                    branchName = branchName + "tetramethyl"
                elif len(methList) == 4:
                    branchName = branchName + "pentamethyl"
                elif len(methList) == 5:
                    branchName = branchName + "hexamethyl"
                elif len(methList) == 6:
                    branchName = branchName + "heptamethyl"

            if len(ethList) > 0:
                if previous == True:
                    branchName = branchName + "-" + str(ethList).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                else:
                    branchName = branchName + str(ethList).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                previous = True
                if len(ethList) == 1:
                    branchName = branchName + "ethyl"
                elif len(ethList) == 2:
                    branchName = branchName + "diethyl"
                elif len(ethList) == 3:
                    branchName = branchName + "tetraethyl"
                elif len(ethList) == 4:
                    branchName = branchName + "pentaethyl"
                elif len(ethList) == 5:
                    branchName = branchName + "hexaethyl"
                elif len(ethList) == 6:
                    branchName = branchName + "heptaethyl"

            if len(propList) > 0:
                if previous == True:
                    branchName = branchName + "-" + str(propList).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                else:
                    branchName = branchName + str(propList).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                if len(propList) == 1:
                    branchName = branchName + "propyl"
                elif len(propList) == 2:
                    branchName = branchName + "dipropyl"
                elif len(propList) == 3:
                    branchName = branchName + "tetrapropyl"
                elif len(propList) == 4:
                    branchName = branchName + "pentapropyl"
                elif len(propList) == 5:
                    branchName = branchName + "hexapropyl"
                elif len(propList) == 6:
                    branchName = branchName + "heptapropyl"
        else:
            if len(methList2) > 0:
                previous = True
                branchName = branchName + str(methList2).replace(
                    '[', "").replace("]", "").replace(" ", "") + "-"
                if len(methList2) == 1:
                    branchName = branchName + "methyl"
                elif len(methList2) == 2:
                    branchName = branchName + "dimethyl"
                elif len(methList2) == 3:
                    branchName = branchName + "tetramethyl"
                elif len(methList2) == 4:
                    branchName = branchName + "pentamethyl"
                elif len(methList2) == 5:
                    branchName = branchName + "hexamethyl"
                elif len(methList2) == 6:
                    branchName = branchName + "heptamethyl"

            if len(ethList2) > 0:
                if previous == True:
                    branchName = branchName + "-" + str(ethList2).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                else:
                    branchName = branchName + str(ethList2).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                previous = True
                if len(ethList2) == 1:
                    branchName = branchName + "ethyl"
                elif len(ethList2) == 2:
                    branchName = branchName + "diethyl"
                elif len(ethList2) == 3:
                    branchName = branchName + "tetraethyl"
                elif len(ethList2) == 4:
                    branchName = branchName + "pentaethyl"
                elif len(ethList2) == 5:
                    branchName = branchName + "hexaethyl"
                elif len(ethList2) == 6:
                    branchName = branchName + "heptaethyl"

            if len(propList2) > 0:
                if previous == True:
                    branchName = branchName + "-" + str(propList2).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                else:
                    branchName = branchName + str(propList2).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                if len(propList2) == 1:
                    branchName = branchName + "propyl"
                elif len(propList2) == 2:
                    branchName = branchName + "dipropyl"
                elif len(propList2) == 3:
                    branchName = branchName + "tetrapropyl"
                elif len(propList2) == 4:
                    branchName = branchName + "pentapropyl"
                elif len(propList2) == 5:
                    branchName = branchName + "hexapropyl"
                elif len(propList2) == 6:
                    branchName = branchName + "heptapropyl"

    elif branched == True and cyclic == False:
        branchName = ""
        methCount = 0
        ethCount = 0
        propCount = 0
        methList = []
        ethList = []
        propList = []
        methList2 = []
        ethList2 = []
        propList2 = []
        for i in range(len(branchList)):
            if branchList[i] == 1:
                methList.append(i + 1)
                methList2.append(len(branchList) - i)
                methCount = methCount + 1
            elif branchList[i] == 2:
                ethList.append(i + 1)
                ethList2.append(len(branchList) - i)
                ethCount = ethCount + 1
            elif branchList[i] == 3:
                propList.append(i + 1)
                propList2.append(len(branchList) - i)
                propCount = propCount + 1

        total = 0
        total2 = 0
        counterList = []
        counterList2 = []
        for i in range(len(methList)):
            counterList.append(methList[i])
            counterList2.append(methList2[i])

        for i in range(len(ethList)):
            counterList.append(ethList[i])
            counterList2.append(ethList2[i])

        for i in range(len(propList)):
            counterList.append(propList[i])
            counterList2.append(propList2[i])

        for i in range(len(counterList)):
            total = total + counterList[i]
            total2 = total2 + counterList2[i]

        if stereoisomerNumber > len(counterList) / 2:
            methList.reverse()
            ethList.reverse()
            propList.reverse()
        else:
            methList2.reverse()
            ethList2.reverse()
            propList2.reverse()

        previous = False
        if total <= total2:
            if len(methList) > 0:
                previous = True
                branchName = branchName + str(methList).replace(
                    '[', "").replace("]", "").replace(" ", "") + "-"
                if len(methList) == 1:
                    branchName = branchName + "methyl"
                elif len(methList) == 2:
                    branchName = branchName + "dimethyl"
                elif len(methList) == 3:
                    branchName = branchName + "tetramethyl"
                elif len(methList) == 4:
                    branchName = branchName + "pentamethyl"
                elif len(methList) == 5:
                    branchName = branchName + "hexamethyl"
                elif len(methList) == 6:
                    branchName = branchName + "heptamethyl"

            if len(ethList) > 0:
                if previous == True:
                    branchName = branchName + "-" + str(ethList).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                else:
                    branchName = branchName + str(ethList).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                previous = True
                if len(ethList) == 1:
                    branchName = branchName + "ethyl"
                elif len(ethList) == 2:
                    branchName = branchName + "diethyl"
                elif len(ethList) == 3:
                    branchName = branchName + "tetraethyl"
                elif len(ethList) == 4:
                    branchName = branchName + "pentaethyl"
                elif len(ethList) == 5:
                    branchName = branchName + "hexaethyl"
                elif len(ethList) == 6:
                    branchName = branchName + "heptaethyl"

            if len(propList) > 0:
                if previous == True:
                    branchName = branchName + "-" + str(propList).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                else:
                    branchName = branchName + str(propList).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                if len(propList) == 1:
                    branchName = branchName + "propyl"
                elif len(propList) == 2:
                    branchName = branchName + "dipropyl"
                elif len(propList) == 3:
                    branchName = branchName + "tetrapropyl"
                elif len(propList) == 4:
                    branchName = branchName + "pentapropyl"
                elif len(propList) == 5:
                    branchName = branchName + "hexapropyl"
                elif len(propList) == 6:
                    branchName = branchName + "heptapropyl"
        else:
            if len(methList2) > 0:
                previous = True
                branchName = branchName + str(methList2).replace(
                    '[', "").replace("]", "").replace(" ", "") + "-"
                if len(methList2) == 1:
                    branchName = branchName + "methyl"
                elif len(methList2) == 2:
                    branchName = branchName + "dimethyl"
                elif len(methList2) == 3:
                    branchName = branchName + "tetramethyl"
                elif len(methList2) == 4:
                    branchName = branchName + "pentamethyl"
                elif len(methList2) == 5:
                    branchName = branchName + "hexamethyl"
                elif len(methList2) == 6:
                    branchName = branchName + "heptamethyl"

            if len(ethList2) > 0:
                if previous == True:
                    branchName = branchName + "-" + str(ethList2).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                else:
                    branchName = branchName + str(ethList2).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                previous = True
                if len(ethList2) == 1:
                    branchName = branchName + "ethyl"
                elif len(ethList2) == 2:
                    branchName = branchName + "diethyl"
                elif len(ethList2) == 3:
                    branchName = branchName + "tetraethyl"
                elif len(ethList2) == 4:
                    branchName = branchName + "pentaethyl"
                elif len(ethList2) == 5:
                    branchName = branchName + "hexaethyl"
                elif len(ethList2) == 6:
                    branchName = branchName + "heptaethyl"

            if len(propList2) > 0:
                if previous == True:
                    branchName = branchName + "-" + str(propList2).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                else:
                    branchName = branchName + str(propList2).replace(
                        '[', "").replace("]", "").replace(" ", "") + "-"
                if len(propList2) == 1:
                    branchName = branchName + "propyl"
                elif len(propList2) == 2:
                    branchName = branchName + "dipropyl"
                elif len(propList2) == 3:
                    branchName = branchName + "tetrapropyl"
                elif len(propList2) == 4:
                    branchName = branchName + "pentapropyl"
                elif len(propList2) == 5:
                    branchName = branchName + "hexapropyl"
                elif len(propList2) == 6:
                    branchName = branchName + "heptapropyl"
    else:
        branchName = ""

    hydrocarbonName = branchName + prefix + suffix

    # If the name is incomplete, do not print any name
    if suffix == "" or prefix == "":
        hydrocarbonName = "Could not generate name"

    # create and place the hydrocarbon name on screen
    variableFont = pygame.font.SysFont('arial.ttf', 80)
    nameText = variableFont.render(hydrocarbonName, True, black)
    nameTextRect = nameText.get_rect()
    loopNum = 0
    while nameTextRect[2] > 470:
        loopNum = loopNum + 1
        variableFont = pygame.font.SysFont('arial.ttf', (80 - loopNum))
        nameText = variableFont.render(hydrocarbonName, True, black)
        nameTextRect = nameText.get_rect()

    screen.blit(nameText, (screenWidth / 2 - (nameTextRect[2] / 2), 35))


def displayUI():
    # Call other functions that need to be run on this page
    displayInteractions()

    # Determine what the cursor is hovering over
    selected = ""
    if x >= 60 and y >= 30 and x <= 135 and y <= 70:
        selected = "last"
    elif x >= 655 and y >= 30 and x <= 740 and y <= 70:
        selected = "home"
    elif x >= 280 and y >= 500 and x <= 295 and y <= 525:
        selected = "nextStereoisomer"
    elif x >= 160 and y >= 500 and x <= 175 and y <= 525:
        selected = "lastStereoisomer"
    elif x >= 20 and y >= 530 and x <= 140 and y <= 555:
        selected = "skeletal"

    # Set out colours/sections on screen
    screen.fill(veryLightGray)
    pygame.draw.rect(screen, white,
                     ((screenWidth / 3.5 - 450 / 2), 100, 450, 400))

    # Determine if hydrocarbon has been saved already
    global saved
    global savedList
    global cyclic
    for i in range(len(savedList)):
        variables = savedList[i].split()
        carbonNumberSaved = int(variables[0])
        hydrogenNumberSaved = int(variables[1])
        cyclicSaved = bool(variables[2])
        if carbonNumber == carbonNumberSaved and hydrogenNumber == hydrogenNumberSaved and cyclic == cyclicSaved:
            saved = True

    # Determine text appearance
    if saved == True:
        saveText = surveyFont.render('Save', True, black, green)
    else:
        saveText = surveyFont.render('Save', True, black, lightGray)

    if hydrogenNumber == carbonNumber * 2:
        hydrocarbonTypeText = informationFont.render(
            "The hydrocarbon is an alkene", True, black)
    elif hydrogenNumber == (carbonNumber * 2) + 2:
        hydrocarbonTypeText = informationFont.render(
            "The hydrocarbon is an alkane", True, black)
    elif cyclic == True:
        hydrocarbonTypeText = informationFont.render(
            "The hydrocarbon is cyclic", True, black)

    if selected == "home":
        homeText = nextFont.render('Home', True, white, lightGray)
    else:
        homeText = nextFont.render('Home', True, black, gray)

    if selected == "last":
        lastText = nextFont.render('Last', True, white, lightGray)
    else:
        lastText = nextFont.render('Last', True, black, gray)

    molecularFormula = str(carbonNumberStr + "      " + hydrogenNumberStr)
    molucularFormulaText = informationFont.render(
        "Molecular formula: C" + "  " + "H", True, black)
    molecularFormulaSubscriptText = subscriptFont.render(
        molecularFormula, True, black)
    molecularMass = (carbonNumber * 12) + hydrogenNumber
    molecularMassStr = str(molecularMass)
    molecularMassText = informationFont.render("Mr: " + molecularMassStr, True,
                                               black)

    # Determine the length of each text block for positioning
    saveTextRect = saveText.get_rect()
    homeTextRect = homeText.get_rect()
    lastTextRect = lastText.get_rect()

    # Place the text on the screen
    screen.blit(saveText, (screenWidth / 10 - (saveTextRect[2] / 2), 500))
    screen.blit(homeText,
                (screenWidth - (screenWidth / 8) - (homeTextRect[2] / 2), 30))
    screen.blit(lastText, (screenWidth / 8 - (lastTextRect[2] / 2), 30))
    screen.blit(hydrocarbonTypeText, (screenWidth / 2 + 60, 120))
    screen.blit(molucularFormulaText, (screenWidth / 2 + 60, 150))
    screen.blit(molecularFormulaSubscriptText, (screenWidth / 2 + 245, 157))
    screen.blit(molecularMassText, (screenWidth / 2 + 60, 180))

    # Create and place the stereoisomer scrolling buttons on the screen if needed
    if hydrogenNumber == carbonNumber * 2 and carbonNumber > 3:
        if selected == "nextStereoisomer":
            nextStereoisomerText = surveyFont.render('>', True, white,
                                                     lightGray)
        else:
            nextStereoisomerText = surveyFont.render('>', True, black, gray)
        if selected == "lastStereoisomer":
            lastStereoisomerText = surveyFont.render('<', True, white,
                                                     lightGray)
        else:
            lastStereoisomerText = surveyFont.render('<', True, black, gray)

        nextStereoisomerTextRect = nextStereoisomerText.get_rect()
        lastStereoisomerTextRect = lastStereoisomerText.get_rect()
        screen.blit(
            nextStereoisomerText,
            (screenWidth / 3.5 - (nextStereoisomerTextRect[2] / 2 - 60), 500))
        screen.blit(
            lastStereoisomerText,
            (screenWidth / 3.5 - (lastStereoisomerTextRect[2] / 2 + 60), 500))

        if cyclic == True:
            chainNumberMax = carbonNumber
        elif cyclic == False and carbonNumber * 2 == hydrogenNumber:
            chainNumberMax = carbonNumber - 1
        else:
            chainNumberMax = carbonNumber // 2
        chainMaxStr = str(chainNumberMax)
        chainNumberStr = str(stereoisomerNumber)
        chainCount = surveyFont.render(chainNumberStr + " / " + chainMaxStr,
                                       True, black)

        chainCountTextRect = chainCount.get_rect()
        screen.blit(chainCount,
                    (screenWidth / 3.5 - (chainCountTextRect[2] / 2), 500))

    # Create and place the skeletal button on the screen if needed
    if cyclic == False:
        if skeletal == False:
            if selected == "skeletal":
                skeletalText = surveyFont.render('Skeletal', True, white,
                                                 lightGray)
            else:
                skeletalText = surveyFont.render('Skeletal', True, black, gray)
        else:
            if selected == "skeletal":
                skeletalText = surveyFont.render('Displayed', True, white,
                                                 lightGray)
            else:
                skeletalText = surveyFont.render('Displayed', True, black,
                                                 gray)
        skeletalTextRect = skeletalText.get_rect()
        screen.blit(skeletalText,
                    (screenWidth / 10 - (skeletalTextRect[2] / 2), 530))

    main()  # Function for drawing the hydrocarbon
    generateName()  # Function for printing the hydrocarbon name


def displayInteractions():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit pygame
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 655 and y >= 30 and x <= 740 and y <= 70:  # Selected home button
            global screenID
            screenID = 1  # Move over to the main menu
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 60 and y >= 30 and x <= 135 and y <= 70:  # Selected last button
            global branched
            if branched == True:
                screenID = 5  # Move over to the branched page
            else:
                screenID = 2  # Move over to the survey page
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 160 and y >= 500 and x <= 175 and y <= 525:  # Selected decrease stereoisomer number button
            global stereoisomerNumber
            if stereoisomerNumber > 1:  # Decrease stereoisomer number if the stereoisomer number is more than 1
                stereoisomerNumber = stereoisomerNumber - 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 280 and y >= 500 and x <= 295 and y <= 525:  # Selected increase stereoisomer number button
            global branchList
            if stereoisomerNumber < carbonNumber // 2:  # Increase stereoisomer number if the stereoisomer number is below maximum
                stereoisomerNumber = stereoisomerNumber + 1
            elif stereoisomerNumber < carbonNumber and cyclic == True:
                stereoisomerNumber = stereoisomerNumber + 1
            elif stereoisomerNumber < carbonNumber - 1 and carbonNumber * 2 == hydrogenNumber and cyclic == False:
                stereoisomerNumber = stereoisomerNumber + 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 20 and y >= 530 and x <= 140 and y <= 555:  # Selected skeletal button
            global skeletal
            if skeletal == False:
                skeletal = True
            else:
                skeletal = False
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 50 and y >= 500 and x <= 110 and y <= 525:  # Selected save button
            global saved
            if saved == False:  # If not already saved, save it
                saved = True
                saveData()
            else:
                saved = False  # If already saved, delete it
                removeData()


# Read the data from the saved text file
def readData():
    global savedList
    savedList = []
    try:
        with open("savedData.txt", mode="r", encoding="utf-8") as my_file:
            for line in my_file:
                if line != "":
                    savedList.append(line.rstrip("\n"))
    finally:
        for i in range(len(savedList)):
            if savedList[i] == "" or savedList[i] == " ":
                savedList.pop(i)


# Remove the data from the saved text file
def removeData():
    global savedList
    global screenID

    if screenID == 4:  # Process for removing if done from saved page
        try:
            savedList.pop(
                (y - 100) // 60
            )  # Identifies the list number based upon the coordinate of the button
        finally:
            with open(
                    "savedData.txt", mode="w", encoding="utf-8"
            ) as my_file:  # Saves new data to ensure its read correctly upon sudden exit
                for data in savedList:
                    my_file.write(data + "\n")
    else:  # Process for removing if done from display page
        try:
            for i in range(
                    len(savedList)
            ):  # Identifies the list number based upon the current variables
                variables = savedList[i].split()
                carbonNumberCompare = int(variables[0])
                hydrogenNumberCompare = int(variables[1])
                cyclicCompareStr = str(variables[2])
                branchedCompareStr = str(variables[3])

                if cyclicCompareStr == "False":
                    cyclicCompare = False
                else:
                    cyclicCompare = True
                if branchedCompareStr == "False":
                    branchedCompare = False
                else:
                    branchedCompare = True

                global carbonNumber
                global hydrogenNumber
                global branched
                if carbonNumber == carbonNumberCompare and hydrogenNumber == hydrogenNumberCompare and branchedCompare == branched and cyclicCompare == cyclic:
                    savedList.pop(i)
                    with open(
                            "savedData.txt", mode="w", encoding="utf-8"
                    ) as my_file:  # Saves new data to ensure its read correctly upon sudden exit
                        for data in savedList:
                            my_file.write(data + "\n")
                    break  # Ensures only one data entry is deleted
        except:
            pass


# Saves data to text file
def saveData():
    global savedList
    global cyclic
    global branched
    global branchList
    global dataID
    cyclicStr = str(cyclic)
    branchedStr = str(branched)
    dataToAdd = carbonNumberStr + " " + hydrogenNumberStr + " " + cyclicStr + " " + branchedStr
    branchListStr = ""

    for i in range(len(branchList)):
        branchListStr = branchListStr + str(branchList[i]) + " "
    dataToAdd = dataToAdd + branchListStr

    doNotAdd = False
    for i in range(len(savedList)):  # Checks if data already exists
        if len(savedList) == 8:  # Limit to saves is 8
            doNotAdd = True  # True if data already exists
            global saved
            saved = False

    if doNotAdd == False:
        savedList.append(dataToAdd)
        with open("savedData.txt", mode="w", encoding="utf-8") as my_file:
            for data in savedList:
                my_file.write(data + "\n")


# Gets coordinates for reference
def getCoordinates():
    global x
    global y
    x, y = pygame.mouse.get_pos()


# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================


# References functions that are used for all hydrocarbons
def main():
    startPosition()
    defineHydrocarbonType()


# Determine starting position of array
def startPosition():
    global hydrocarbonArray
    global rowLength
    hydrocarbonArray = []
    rowLength = (carbonNumber * 2) + 3
    for i in range(5):
        hydrocarbonArray.append([" "] * rowLength)
    global startPositionY
    global startPositionX
    startPositionY = (5 // 2)
    startPositionX = (rowLength // 2)


# Create basic hydrocarbon
def createHydrocarbon():
    # Add components that cannot be added in a loop
    hydrocarbonArray[startPositionY][0] = "H"
    hydrocarbonArray[startPositionY][rowLength - 1] = "H"
    hydrocarbonArray[startPositionY][startPositionX + carbonNumber] = "—"

    for x in range(carbonNumber):
        hydrocarbonArray[startPositionY][(2 * x) + 2] = "C"
        hydrocarbonArray[startPositionY + 1][(2 * x) + 2] = "|"
        hydrocarbonArray[startPositionY - 1][(2 * x) + 2] = "|"
        hydrocarbonArray[startPositionY - 2][(2 * x) + 2] = "H"
        hydrocarbonArray[startPositionY + 2][(2 * x) + 2] = "H"
        hydrocarbonArray[startPositionY][(2 * x) + 1] = "—"


# Defines type of hydrocarbon and calls relevant functions
def defineHydrocarbonType():
    global cyclic
    global branched
    if cyclic == True:
        printCyclic()
        if branched == True:
            addCyclicBranch()
    elif skeletal == True or branched == True:
        if hydrogenNumber == (carbonNumber * 2) + 2:
            printSkeletal()
            addBranch()
        elif hydrogenNumber == carbonNumber * 2:
            printSkeletal()
            alkeneSkeletal()
            addBranch()
    elif hydrogenNumber == (carbonNumber * 2) + 2:
        createHydrocarbon()
        printHydrocarbon()
    elif hydrogenNumber == carbonNumber * 2:
        createHydrocarbon()
        alkene()
        printHydrocarbon()


def addBranch():
    # Determine length of hydrocarbon
    offsetX = 0
    for i in range(carbonNumber - 1):
        offsetX = offsetX + 75

    # Base dimensions of bonds
    length = 75
    height = 75

    # Calculate the starting points
    startingPointX = (screenWidth // 3.5 - offsetX // 2) + length
    startingPointY = (screenHeight // 2) - (height // 2) + height

    # Print the hydrocarbon
    offsetX = 0
    for a in range(len(branchList)):
        if (a % 2) == 0: # Drawing above Vs drawing below
            if branchList[a] == 1: # If the branch is 1 carbon long
                pygame.draw.line(
                    screen, black, (startingPointX + offsetX, startingPointY),
                    (startingPointX + offsetX, startingPointY + height), 2)
            elif branchList[a] == 2: # If the branch is 1 carbon long
                pygame.draw.line(screen, black,
                                 (startingPointX + offsetX, startingPointY),
                                 (startingPointX + offsetX - length,
                                  startingPointY + height), 2)
                pygame.draw.line(
                    screen, black, (startingPointX + offsetX - length,
                                    startingPointY + height),
                    (startingPointX + offsetX, startingPointY + (2 * height)),
                    2)
        else:
            if branchList[a] == 1:# If the branch is 1 carbon long
                pygame.draw.line(
                    screen, black,
                    (startingPointX + offsetX, startingPointY - height),
                    (startingPointX + offsetX, startingPointY - (2 * height)),
                    2)
            elif branchList[a] == 2: # If the branch is 1 carbon long
                pygame.draw.line(
                    screen, black,
                    (startingPointX + offsetX, startingPointY - height),
                    (startingPointX + offsetX - length,
                     startingPointY - (2 * height)), 2)
                pygame.draw.line(
                    screen, black, (startingPointX + offsetX - length,
                                    startingPointY - (2 * height)),
                    (startingPointX + offsetX, startingPointY - (3 * height)),
                    2)
        # Move to next carbon
        offsetX = offsetX + 75


def addCyclicBranch():
    # Determine starting point
    startingPointX = screenWidth // 3.5
    startingPointY = screenHeight // 2
    # Determine angle increment
    angleIncrement = 2 * pi / carbonNumber
    angle = 0
    # Twist is the value that alters the branch angle
    twist = 70
    for i in range(len(branchList)):
        # Ensure the branch list contains integers, not strings
        branchList[i] = int(branchList[i])

    for a in range(len(branchList)):
        # Find the starting position on the hydrocarbon
        xPosition1 = (90 * cos(angle + angleIncrement)) + startingPointX
        yPosition1 = (90 * sin(angle + angleIncrement)) + startingPointY
        for i in range(branchList[a]):
            # Add the branch lines to the hydrocarbon
            xPosition2 = xPosition1 + (50 * cos(
                (angle + angleIncrement + twist)))
            yPosition2 = yPosition1 + (50 * sin(
                (angle + angleIncrement + twist)))
            pygame.draw.line(screen, black, (xPosition1, yPosition1),
                             (xPosition2, yPosition2), 2)
            # Alternate the direction of the branch chain
            if twist == 70:
                twist = -70
            else:
                twist = 70
            xPosition1 = xPosition2
            yPosition1 = yPosition2
        # Reset the twist value
        twist = 70
        # Increment the angle
        angle = angle + angleIncrement


# Alters array for alkenes
def alkene():
    hydrocarbonArray[startPositionY][(2 * stereoisomerNumber) + 1] = "="
    hydrocarbonArray[startPositionY - 2][(2 * stereoisomerNumber) + 2] = " "
    hydrocarbonArray[startPositionY - 2][2 * stereoisomerNumber] = " "
    hydrocarbonArray[startPositionY - 1][(2 * stereoisomerNumber) + 2] = " "
    hydrocarbonArray[startPositionY - 1][2 * stereoisomerNumber] = " "


# Prints the array onto screen
def printHydrocarbon():
    # Determine the length of the hydrocarbon
    offsetY = 0
    for row in hydrocarbonArray:
        offsetX = -2 * carbonNumber
        for element in row:
            if element == "|":
                offsetX = offsetX + 5
            if element == "—":
                offsetY = offsetY - 2
                offsetX = offsetX - 2
            offsetX = offsetX + 30
            if element == "|":
                offsetX = offsetX - 5
            if element == "—":
                offsetY = offsetY + 2
                offsetX = offsetX + 2
        offsetY = offsetY + 30

    # Calculate the starting points
    startingPointX = screenWidth // 3.5 - offsetX // 2
    startingPointY = screenHeight // 2 - offsetY // 2

    # Print the hydrocarbon
    offsetY = 0
    for row in hydrocarbonArray:
        offsetX = 0
        for element in row:
            if element == "|":
                offsetX = offsetX + 5
            if element == "—":
                offsetY = offsetY - 2
                offsetX = offsetX - 2
            elementText = surveyFont.render(element, True, black)
            screen.blit(elementText, ((startingPointX + offsetX),
                                      (startingPointY + offsetY)))
            offsetX = offsetX + 30
            if element == "|":
                offsetX = offsetX - 5
            if element == "—":
                offsetY = offsetY + 2
                offsetX = offsetX + 2
        offsetY = offsetY + 30


def printSkeletal():
    # Determine length of hydrocarbon
    offsetX = 0
    for i in range(carbonNumber - 1):
        offsetX = offsetX + 75

    # Base dimensions of bonds
    length = 75
    height = 75
    # For alternating line direction
    drawUp = True

    # Calculate the starting points
    startingPointX = screenWidth // 3.5 - offsetX // 2
    startingPointY = (screenHeight // 2) - (height // 2)

    # Print the hydrocarbon
    offsetX = 0
    for i in range(carbonNumber - 1):
        if drawUp == True:
            pygame.draw.line(
                screen, black, (startingPointX + offsetX, startingPointY),
                (startingPointX + length + offsetX, startingPointY + height),
                2)
            drawUp = False
        else:
            pygame.draw.line(
                screen, black,
                (startingPointX + offsetX, startingPointY + height),
                (startingPointX + length + offsetX, startingPointY), 2)
            drawUp = True
        offsetX = offsetX + 75


def printCyclic():
    startingPointX = screenWidth // 3.5
    startingPointY = screenHeight // 2
    angleIncrement = 2 * pi / carbonNumber
    angle = 0
    for point in range(carbonNumber):
        xPosition1 = (90 * cos(angle)) + startingPointX
        yPosition1 = (90 * sin(angle)) + startingPointY
        xPosition2 = (90 * cos(angle + angleIncrement)) + startingPointX
        yPosition2 = (90 * sin(angle + angleIncrement)) + startingPointY
        pygame.draw.line(screen, black, (xPosition1, yPosition1),
                         (xPosition2, yPosition2), 2)
        if hydrogenNumber == carbonNumber * 2:
            if stereoisomerNumber - 1 == point:
                xPosition1 = (80 * cos(angle)) + startingPointX
                yPosition1 = (80 * sin(angle)) + startingPointY
                xPosition2 = (
                                     80 * cos(angle + angleIncrement)) + startingPointX
                yPosition2 = (
                                     80 * sin(angle + angleIncrement)) + startingPointY
                pygame.draw.line(screen, black, (xPosition1, yPosition1),
                                 (xPosition2, yPosition2), 2)
        elif hydrogenNumber == carbonNumber:
            pygame.draw.circle(screen, black,
                               (int(startingPointX), int(startingPointY)), 70,
                               2)
        angle = angle + angleIncrement


def alkeneSkeletal():
    # Determine length of hydrocarbon
    offsetX = 0
    for i in range(carbonNumber - 1):
        offsetX = offsetX + 75

    # Base dimensions of bonds
    length = 75
    height = 75

    # Calculate the starting points
    startingPointX = screenWidth // 3.5 - offsetX // 2
    startingPointY = (screenHeight // 2) - (height // 2)

    # Print the hydrocarbon
    offsetX = 75 * (stereoisomerNumber - 1)
    for i in range(carbonNumber - 1):
        if stereoisomerNumber % 2 != 0:
            pygame.draw.line(
                screen, black,
                (startingPointX + offsetX + 5, startingPointY - 5),
                (startingPointX + length + offsetX + 5,
                 startingPointY + height - 5), 2)
        else:
            pygame.draw.line(
                screen, black,
                (startingPointX + offsetX - 5, startingPointY + height - 5),
                (startingPointX + length + offsetX - 5, startingPointY - 5), 2)


mainLoop()
pygame.quit()
quit()
