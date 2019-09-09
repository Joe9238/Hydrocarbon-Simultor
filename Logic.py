def main():
    survey()
    startpos()
    definechain()


def survey():
    global cnum
    global hnum
    global strcnum
    global strhnum
    global SUB
    global SUBimp
    global SUP
    global straightchain
    global cnumbranchlist
    global hnumbranchlist
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    SUBimp = str.maketrans("(2n+2)-", "₍₂ₙ₊₂₎₋")
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    cnumbranchlist = []
    hnumbranchlist = []

    while True:
        while True:
            try:
                cnum = int(input("Enter the number of carbon atoms: "))
                break
            except:
                print("Invalid input")
                print(" ")

        while True:
            try:
                hnum = int(input("Enter the number of hydrogen atoms: "))
                break
            except:
                print("Invalid input")
                print(" ")
        if hnum == (cnum * 2) + 2:
            break
        elif hnum == cnum * 2:
            break
        elif hnum == cnum and cnum >= 6:
            break
        else:
            print("Error - Invalid hydrocarbon entered.")
            print(" ")

    strcnum = str(cnum)
    strhnum = str(hnum)

    while True:
        straightchain = str(input("Would you like to view straight chain hydrocarbons only? Y or N: "))
        if straightchain == "Y" or straightchain == "N":
            break
        else:
            print("Invalid input")
            print(" ")

    if straightchain == "N":
        print(
            "Please enter the number of carbon and hydrogen atoms in each additional carbon branch. If you have entered all the branches you wish to use, just enter 0.")

        while True:
            try:
                print(" ")
                cnumbranch = int(input("Enter the number of carbon atoms in the branch: "))
                if cnumbranch == 0:
                    break
                hnumbranch = int(input("Enter the number of hydrogen atoms in the branch: "))
                if hnumbranch == 0:
                    break
                if cnumbranch < (cnum // 2):
                    if ((cnumbranch * 2) + 1) == hnumbranch:
                        cnumbranchlist.append(cnumbranch)
                        hnumbranchlist.append(hnumbranch)
                    elif (cnumbranch * 2) == hnumbranch:
                        cnumbranchlist.append(cnumbranch)
                        hnumbranchlist.append(hnumbranch)
                    elif cnumbranch >= 6 and cnumbranch == (hnumbranch - 1):
                        cnumbranchlist.append(cnumbranch)
                        hnumbranchlist.append(hnumbranch)
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")

                if len(cnumbranchlist) == hnum:
                    print("All branch spaces have been taken")
                    break
                if cnumbranch == "" or hnumbranch == "" and valid != False:
                    break
            except:
                print("Invalid input")


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
    array[startposy][startposx + cnum] = "-"

    for x in range(cnum):
        array[startposy][(2 * x) + 2] = "C"
        array[startposy + 1][(2 * x) + 2] = "|"
        array[startposy - 1][(2 * x) + 2] = "|"
        array[startposy - 2][(2 * x) + 2] = "H"
        array[startposy + 2][(2 * x) + 2] = "H"
        array[startposy][(2 * x) + 1] = "-"


def definechain():
    if hnum == (cnum * 2) + 2:
        createchain()
        alkane()
    elif hnum == cnum * 2:
        createchain()
        alkene()
    elif hnum == cnum and cnum >= 6:
        cyclic()


def alkane():  # DOWN AND THEN ALONG - STARTS AT [0][0]
    if straightchain == "N":
        multichain()
    else:
        printchain()

    print("""
  """)
    molformula = str("C" + strcnum + "H" + strhnum)
    print("The molecular formula of the hydrocarbon is " + molformula.translate(SUB))
    print("The hydrocarbon is an alkane")


def alkene():
    if straightchain == "N":
        multichain()
    else:
        for x in range(cnum // 2):
            array[startposy][startposx + (2 * (x + 1)) + 1] = "="
            array[startposy - 2][startposx + (2 * (x + 1))] = " "
            array[startposy - 2][startposx + (2 * (x + 2))] = " "
            array[startposy - 1][startposx + (2 * (x + 1))] = " "
            array[startposy - 1][startposx + (2 * (x + 2))] = " "

            printchain()

            array[startposy][startposx + (2 * (x + 1)) + 1] = "-"
            array[startposy - 2][startposx + (2 * (x + 1))] = "H"
            array[startposy - 2][startposx + (2 * (x + 2))] = "H"
            array[startposy - 1][startposx + (2 * (x + 1))] = "|"
            array[startposy - 1][startposx + (2 * (x + 2))] = "|"

    print("""
  """)
    molformula = str("C" + strcnum + "H" + strhnum)
    print("The molecular formula of the hydrocarbon is " + molformula.translate(SUB))
    print("The hydrocarbon is an alkene")


def printchain():
    for row in array:
        for elem in row:
            print(elem, end=' ')
        print()
    print(" ")


def cyclic():
    pass


def multichain():
    pass


main()