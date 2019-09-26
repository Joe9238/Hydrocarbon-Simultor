# Import pygame
import pygame
from pygame.locals import *

# Declare neccessary global variables
global carbonNumber  # number of carbon atoms
global hydrogenNumber  # number of hydrogen atoms
global carbonNumberStr  # versions of hydrogenNumber and carbonNumber as string for typing
global hydrogenNumberStr
carbonNumber = 1  # minimum values for hydrogen and carbon
hydrogenNumber = 4
carbonNumberStr = str(carbonNumber)  # creating the string versions of hydrogenNumber and carbonNumber
hydrogenNumberStr = str(hydrogenNumber)

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

# Initial value for the screen number
global screenID
screenID = 1

# Initial value for the chain number (used where there is more than one hydrocarbon possible)
global stereoisomerNumber
stereoisomerNumber = 1


# Main loop that determines what screen is displayed
def mainLoop():
    doLoop = True  # This will remain true up until pygame is quit
    readData()
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

        pygame.display.update()  # Updates the on-screen display
        clock.tick(FPS)
        pygame.display.set_caption("Hydrocarbon Generator - Joe Maskell")  # Sets the caption of the pygame window


# Display data for the home page
def homeUI():
    homeinteractions()

    selected = ""  # Selected defines where the cursor is hovering over
    if x >= 340 and y >= 300 and x <= 460 and y <= 350:  # These are the start button parameters
        selected = "start"
    elif x >= 325 and y >= 360 and x <= 475 and y <= 410:  # These are the saved button parameters
        selected = "saved"
    elif x >= 345 and y >= 395 and x <= 455 and y <= 470:  # These are the quit button parameters
        selected = "quit"
    screen.fill(gray)  # Create the basic background

    # This will determine the fonts and contents of each block of text
    # variable = font type(word to be printed, antialiasing, letter colour, highlighter colour)
    titleText = titleFont.render('Welcome', True, blue)
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

    # Gets the length of each of the text blocks for positioning
    titleTextRect = titleText.get_rect()
    startTextRect = startText.get_rect()
    quitTextRect = quitText.get_rect()
    savedTextRect = savedText.get_rect()

    # Places the text centre to the screen at the given y position
    screen.blit(titleText, (screenWidth / 2 - (titleTextRect[2] / 2), 80))
    screen.blit(startText, (screenWidth / 2 - (startTextRect[2] / 2), 300))
    screen.blit(quitText, (screenWidth / 2 - (quitTextRect[2] / 2), 420))
    screen.blit(savedText, (screenWidth / 2 - (savedTextRect[2] / 2), 360))


# Possible events in the home screen
def homeinteractions():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit pygame
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 345 and y >= 395 and x <= 455 and y <= 470:  # Selected quit button on the home screen
            pygame.quit()  # Quit pygame
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 340 and y >= 300 and x <= 460 and y <= 350:  # Selected start button on the home screen
            global screenID
            screenID = 2  # Move over to the survey page
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 345 and y >= 360 and x <= 455 and y <= 410:
            screenID = 4


def savedUI():
    savedInteractions()

    selected = ""
    if x >= 655 and y >= 30 and x <= 740 and y <= 70:
        selected = "home"

    screen.fill(gray)  # Create the basic background
    if selected == "home":
        homeText = nextFont.render('Home', True, white, lightGray)
    else:
        homeText = nextFont.render('Home', True, black)

    carbonsText = surveyFont.render('Carbons', True, black)
    limitText = surveyFont.render('You can save a maximum of 8 hydrocarbons.', True, black)
    hydrogensText = surveyFont.render('Hydrogens', True, black)

    global savedList
    for a in range(len(savedList)):
        dataList = savedList[a].split()
        for i in range(2):
            dataText = nextFont.render(dataList[i], True, black)
            dataTextRect = dataText.get_rect()
            screen.blit(dataText, ((screenWidth / 8) - (dataTextRect[2] / 2) + (i * 140), 100 + (a * 60)))

    for i in range(8):
        removeText = nextFont.render(" - ", True, red)
        addText = nextFont.render(" + ", True, green)
        if x >= 0 and y > 90 + (i * 60) and x <= 40 and y < 150 + (i * 60):
            removeText = nextFont.render(" - ", True, red, lightRed)
        elif x >= 755 and y > 90 + (i * 60) and x <= screenWidth and y < 150 + (i * 60):
            addText = nextFont.render(" + ", True, green, lightGreen)
        screen.blit(
            removeText,
            (3, 100 + (60 * i)))
        screen.blit(
            addText,
            (758, 100 + (60 * i)))


    homeTextRect = homeText.get_rect()
    carbonsTextRect = carbonsText.get_rect()
    hydrogensTextRect = hydrogensText.get_rect()
    limitTextRect = limitText.get_rect()

    screen.blit(homeText, (screenWidth - (screenWidth / 8) - (homeTextRect[2] / 2), 30))
    screen.blit(carbonsText, ((screenWidth / 8) - (carbonsTextRect[2] / 2), 70))
    screen.blit(hydrogensText, ((screenWidth / 8) - (hydrogensTextRect[2] / 2) + 140, 70))
    screen.blit(limitText, ((screenWidth / 2) - (limitTextRect[2] / 2), 573))

    pygame.draw.line(screen, black, (0, 97), (screenWidth, 97))
    pygame.draw.line(screen, black, (755, 70), (755, 570))
    pygame.draw.line(screen, black, (165, 70), (165, 570))
    pygame.draw.line(screen, black, (310, 70), (310, 570))
    pygame.draw.line(screen, black, (43, 70), (43, 570))
    for i in range(8):
        pygame.draw.line(screen, black, (0, 150 + (i * 60)), (screenWidth, 150 + (i * 60)))


def savedInteractions():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 655 and y >= 30 and x <= 740 and y <= 70:
            global screenID
            screenID = 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 0 and y >= 90 and x <= 40 and y <= 630:
            removeData()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 755 and y >= 90 and x <= screenWidth and y <= 630:
            try:
                dataID = ((y - 100) // 60)
                dataList = savedList[dataID].split()
                global carbonNumber
                global hydrogenNumber
                carbonNumber = int(dataList[0])
                hydrogenNumber = int(dataList[1])

                global carbonNumberStr
                global hydrogenNumberStr
                carbonNumberStr = str(carbonNumber)
                hydrogenNumberStr = str(hydrogenNumber)
                screenID = 3
            except:
                print("No data found")


def surveyUI():
    surveyInteractions()

    global cannotContinue
    cannotContinue = False  # cannotContinue is checked before moving onto the next page and to highlight incorrect inputs
    if hydrogenNumber == (carbonNumber * 2) + 2:
        cannotContinue = False
    elif hydrogenNumber == carbonNumber * 2:
        cannotContinue = False
    elif hydrogenNumber == carbonNumber and carbonNumber >= 6:
        cannotContinue = False
    else:
        cannotContinue = True  # If the hydrocarbon is invalid, cannotContinue is set to true

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

    screen.fill(veryLightGray)  # Create the basic background

    titleText = titleFont.render('Survey Page', True, black)
    if selected == "next" and cannotContinue is False:
        nextText = nextFont.render('Next', True, white, lightGray)
    else:
        nextText = nextFont.render('Next', True, black, gray)
    if selected == "last":
        lastText = nextFont.render('Last', True, white, lightGray)
    else:
        lastText = nextFont.render('Last', True, black, gray)

    titleTextRect = titleText.get_rect()
    nextTextRect = nextText.get_rect()
    lastTextRect = lastText.get_rect()

    screen.blit(titleText, (screenWidth / 2 - (titleTextRect[2] / 2), 30))
    screen.blit(nextText, (screenWidth - (screenWidth / 8) - (nextTextRect[2] / 2), 30))
    screen.blit(lastText, (screenWidth / 8 - (lastTextRect[2] / 2), 30))

    global carbonNumberStr
    global hydrogenNumberStr
    carbonNumberStr = str(carbonNumber)
    hydrogenNumberStr = str(hydrogenNumber)

    carbonNumberText = surveyFont.render('Number of carbon atoms: ' + carbonNumberStr, True, black)

    if cannotContinue is False:
        hydrogenNumberText = surveyFont.render('Number of hydrogen atoms: ' + hydrogenNumberStr, True, black)
    else:
        hydrogenNumberText = surveyFont.render('Number of hydrogen atoms: ' + hydrogenNumberStr, True, black, red)

    # Main Menu Text
    screen.blit(carbonNumberText, (40, 140))
    screen.blit(hydrogenNumberText, (40, 220))
    screen.blit(increaseCarbonsText, (500, 125))
    screen.blit(decreaseCarbonsText, (500, 155))
    screen.blit(increaseHydrogensText, (500, 205))
    screen.blit(decreaseHydrogensText, (500, 235))


def surveyInteractions():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 500 and y >= 125 and x <= 515 and y <= 150:
            global carbonNumber  
            if carbonNumber < 6:
                carbonNumber = carbonNumber + 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 500 and y >= 155 and x <= 515 and y <= 180:
            if carbonNumber > 1:
                carbonNumber = carbonNumber - 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 500 and y >= 205 and x <= 515 and y <= 230:
            global hydrogenNumber
            if hydrogenNumber < (carbonNumber * 2) + 2:
                hydrogenNumber = hydrogenNumber + 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 500 and y >= 235 and x <= 515 and y <= 260:
            if hydrogenNumber > 4:
                hydrogenNumber = hydrogenNumber - 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 655 and y >= 30 and x <= 740 and y <= 70:
            if cannotContinue is False:
                global screenID
                global saved
                saved = False
                screenID = 3
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 60 and y >= 30 and x <= 135 and y <= 70:
            screenID = 1


def generateName():
    suffix = ""
    if hydrogenNumber == carbonNumber * 2:
        suffix = "ene"
    elif hydrogenNumber == (carbonNumber * 2) + 2:
        suffix = "ane"

    prefix = ""
    if carbonNumber == 1:
        prefix = "Meth"
    elif carbonNumber == 2:
        prefix = "Eth"
    elif carbonNumber == 3:
        prefix = "Prop"
    elif carbonNumber == 4:
        prefix = "But"
    elif carbonNumber == 5:
        prefix = "Pent"
    elif carbonNumber == 6:
        prefix = "Hex"

    if suffix == "" or prefix == "":
        suffix = ""
        prefix = ""
    hydrocarbonName = prefix + suffix

    nameText = titleFont.render(hydrocarbonName, True, black)

    nameTextRect = nameText.get_rect()

    screen.blit(nameText, (screenWidth / 2 - (nameTextRect[2] / 2), 30))


def displayUI():
    displayInteractions()
    selected = ""
    if x >= 60 and y >= 30 and x <= 135 and y <= 70:
        selected = "last"
    elif x >= 655 and y >= 30 and x <= 740 and y <= 70:
        selected = "home"
    elif x >= 280 and y >= 500 and x <= 295 and y <= 525:
        selected = "nextStereoisomer"
    elif x >= 160 and y >= 500 and x <= 175 and y <= 525:
        selected = "lastStereoisomer"
    elif x >= 50 and y >= 500 and x <= 110 and y <= 525:
        selected = "save"

    screen.fill(veryLightGray)
    pygame.draw.rect(screen, white, ((screenWidth / 3.5 - 450 / 2), 100, 450, 400))
    main()
    generateName()
    global saved

    global savedList
    for i in range(len(savedList)):
        variables = savedList[i].split()
        carbonNumberSaved = int(variables[0])
        hydrogenNumberSaved = int(variables[1])

        if carbonNumber == carbonNumberSaved and hydrogenNumber == hydrogenNumberSaved:
            saved = True

    if saved == True:
        saveText = surveyFont.render('Save', True, black, green)
    elif selected == "save":
        saveText = surveyFont.render('Save', True, black, lightGreen)
    else:
        saveText = surveyFont.render('Save', True, black, lightGray)
    if selected == "home":
        homeText = nextFont.render('Home', True, white, lightGray)
    else:
        homeText = nextFont.render('Home', True, black, gray)
    if selected == "last":
        lastText = nextFont.render('Last', True, white, lightGray)
    else:
        lastText = nextFont.render('Last', True, black, gray)

    if hydrogenNumber == carbonNumber * 2 and carbonNumber > 3:
        if selected == "nextStereoisomer":
            nextStereoisomerText = surveyFont.render('>', True, white, lightGray)
        else:
            nextStereoisomerText = surveyFont.render('>', True, black, gray)
        if selected == "lastStereoisomer":
            lastStereoisomerText = surveyFont.render('<', True, white, lightGray)
        else:
            lastStereoisomerText = surveyFont.render('<', True, black, gray)

        nextStereoisomerTextRect = nextStereoisomerText.get_rect()
        lastStereoisomerTextRect = lastStereoisomerText.get_rect()
        screen.blit(nextStereoisomerText, (screenWidth / 3.5 - (nextStereoisomerTextRect[2] / 2 - 60), 500))
        screen.blit(lastStereoisomerText, (screenWidth / 3.5 - (lastStereoisomerTextRect[2] / 2 + 60), 500))

        chainNumberMax = carbonNumber // 2
        chainMaxStr = str(chainNumberMax)
        chainNumberStr = str(stereoisomerNumber)
        chainCount = surveyFont.render(chainNumberStr + " / " + chainMaxStr, True,
                                       black)

        chainCountTextRect = chainCount.get_rect()
        screen.blit(chainCount, (screenWidth / 3.5 - (chainCountTextRect[2] / 2), 500))

    saveTextRect = saveText.get_rect()
    homeTextRect = homeText.get_rect()
    lastTextRect = lastText.get_rect()

    screen.blit(saveText, (screenWidth / 10 - (saveTextRect[2] / 2), 500))
    screen.blit(homeText, (screenWidth - (screenWidth / 8) - (homeTextRect[2] / 2), 30))
    screen.blit(lastText, (screenWidth / 8 - (lastTextRect[2] / 2), 30))

    # Printing of information about the hydrocarbon
    molecularFormula = str(carbonNumberStr + "      " + hydrogenNumberStr)
    molucularFormulaText = informationFont.render("Molecular formula: C" + "  " + "H", True,
                                           black)
    molecularFormulaSubscriptText = subscriptFont.render(molecularFormula, True, black)
    molecularMass = (carbonNumber * 12) + hydrogenNumber
    molecularMassStr = str(molecularMass)
    molecularMassText = informationFont.render("Mr: " + molecularMassStr, True, black)

    if hydrogenNumber == carbonNumber * 2:
        hydrocarbonTypeText = informationFont.render("The hydrocarbon is an alkene", True,
                                           black)
    elif hydrogenNumber == (carbonNumber * 2) + 2:
        hydrocarbonTypeText = informationFont.render("The hydrocarbon is an alkane", True,
                                           black)
    elif hydrogenNumber == carbonNumber:
        hydrocarbonTypeText = informationFont.render("The hydrocarbon is cyclic", True, black)

    screen.blit(hydrocarbonTypeText, (screenWidth / 2 + 60, 120))
    screen.blit(molucularFormulaText, (screenWidth / 2 + 60, 150))
    screen.blit(molecularFormulaSubscriptText, (screenWidth / 2 + 245, 157))
    screen.blit(molecularMassText, (screenWidth / 2 + 60, 180))


def displayInteractions():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 655 and y >= 30 and x <= 740 and y <= 70:
            global screenID
            screenID = 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 60 and y >= 30 and x <= 135 and y <= 70:
            screenID = 2
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 160 and y >= 500 and x <= 175 and y <= 525:
            global stereoisomerNumber
            if stereoisomerNumber > 1:
                stereoisomerNumber = stereoisomerNumber - 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 280 and y >= 500 and x <= 295 and y <= 525:
            if stereoisomerNumber < carbonNumber // 2:
                stereoisomerNumber = stereoisomerNumber + 1
        if event.type == pygame.MOUSEBUTTONDOWN and x >= 50 and y >= 500 and x <= 110 and y <= 525:
            global saved
            if saved == False:
                saved = True
                saveData()
            else:
                saved = False
                removeData()


def readData():
    global savedList
    savedList = []
    try:
        with open("savedData.txt", mode="r", encoding="utf-8") as my_file:
            for line in my_file:
                if line != "":
                    savedList.append(line.rstrip("\n"))
    except:
        print("No data found")
    finally:
        print("Data gathered successfully")
        print(savedList)


def removeData():
    global savedList
    global screenID

    if screenID == 4:
        try:
            savedList.pop((y - 100) // 60)
        except:
            print("Could not delete")
        finally:
            with open("savedData.txt", mode="w", encoding="utf-8") as my_file:
                for data in savedList:
                    my_file.write(data+"\n")
    else:
        try:
            for i in range(len(savedList)):
                variables = savedList[i].split()
                cnumcompare = int(variables[0])
                hnumcompare = int(variables[1])
                global carbonNumber
                global hydrogenNumber
                if carbonNumber == cnumcompare and hydrogenNumber == hnumcompare:
                    savedList.pop(i)
                    with open("savedData.txt", mode="w", encoding="utf-8") as my_file:
                        for data in savedList:
                            my_file.write(data + "\n")
                    break
        except:
            print("Could not delete")


def saveData():
    global savedList
    dataToAdd = carbonNumberStr + " " + hydrogenNumberStr
    doNotAdd = False
    for i in range(len(savedList)):
        if savedList[i] == dataToAdd or len(savedList) == 8:
            doNotAdd = True
            global saved
            saved = False

    if doNotAdd == False:
        savedList.append(dataToAdd)
        with open("savedData.txt", mode="w", encoding="utf-8") as my_file:
            for data in savedList:
                my_file.write(data+"\n")


def getCoordinates():
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
    startPosition()
    defineHydrocarbonType()


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


def createHydrocarbon():
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


def defineHydrocarbonType():
    if hydrogenNumber == (carbonNumber * 2) + 2:
        createHydrocarbon()
        printHydrocarbon()
    elif hydrogenNumber == carbonNumber * 2:
        createHydrocarbon()
        alkene()
        printHydrocarbon()
    elif hydrogenNumber == carbonNumber and carbonNumber >= 6:
        cyclic()


def alkene():
    hydrocarbonArray[startPositionY][(2 * stereoisomerNumber) + 1] = "="
    hydrocarbonArray[startPositionY - 2][(2 * stereoisomerNumber) + 2] = " "
    hydrocarbonArray[startPositionY - 2][2 * stereoisomerNumber] = " "
    hydrocarbonArray[startPositionY - 1][(2 * stereoisomerNumber) + 2] = " "
    hydrocarbonArray[startPositionY - 1][2 * stereoisomerNumber] = " "


def printHydrocarbon():
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

    startingPointX = screenWidth // 3.5 - offsetX // 2
    startingPointY = screenHeight // 2 - offsetY // 2

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
            if element == "=":
                elementText = surveyFont.render(element, True, black, blue)
            screen.blit(elementText, (startingPointX + offsetX, startingPointY + offsetY))
            offsetX = offsetX + 30
            if element == "|":
                offsetX = offsetX - 5
            if element == "—":
                offsetY = offsetY + 2
                offsetX = offsetX + 2
        offsetY = offsetY + 30


def cyclic():
    pass


mainLoop()
pygame.quit()
quit()
