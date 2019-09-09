def main():
    survey()
    startpos()
    createchain()
    if straightchain == "Y":
        straightchain1()
    else:
        multichain()


def survey():
    global cnum
    global hnum
    global strcnum
    global strhnum
    global SUB
    global SUBimp
    global SUP
    global straightchain
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    SUBimp = str.maketrans("(2n+2)-", "₍₂ₙ₊₂₎₋")
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

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

    while True:
        straightchain = str(input("Is it a single chain hydrocarbon? Y or N: "))
        if straightchain == "Y" or straightchain == "N":
            break
        else:
            print("Invalid input")
            print(" ")

    strcnum = str(cnum)
    strhnum = str(hnum)


def startpos():
    global array
    array = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
    global startposy
    global startposx
    rownum = 0
    for row in array:
        rowlen = len(row)
        rownum = rownum + 1

    startposy = rownum // 2
    startposx = (rowlen // 2) - cnum + 1


def straightchain1():
    if hnum == (cnum * 2) + 2:
        alkane()
    elif hnum == cnum * 2:
        alkene()
    elif hnum == cnum and cnum >= 6:
        cyclic()
    else:
        print("Error - Unknown Hydrocarbon")
        main()


def createchain():
    for x in range(cnum):
        array[startposy][startposx + (2 * (x + 1)) - 2] = "H"
        array[startposy][startposx + (2 * (x + 1)) + 2] = "H"

    for x in range(cnum):
        array[startposy][startposx + (2 * (x + 1))] = "C"
        array[startposy + 1][startposx + (2 * (x + 1))] = "|"
        array[startposy - 1][startposx + (2 * (x + 1))] = "|"
        array[startposy - 2][startposx + (2 * (x + 1))] = "H"
        array[startposy + 2][startposx + (2 * (x + 1))] = "H"
        array[startposy][startposx + (2 * (x + 1)) - 1] = "-"
        array[startposy][startposx + (2 * (x + 1)) + 1] = "-"


def alkane():  # DOWN AND THEN ALONG - STARTS AT [0][0]
    for row in array:
        for elem in row:
            print(elem, end=' ')
        print()

    print("""
  """)
    molformula = str("C" + strcnum + "H" + strhnum)
    print("The molecular formula of the hydrocarbon is " + molformula.translate(SUB))
    print("The hydrocarbon is an alkane")


def alkene():
    for x in range(cnum // 2):
        array[startposy][startposx + (2 * (x + 1)) + 1] = "="
        array[startposy - 2][startposx + (2 * (x + 1))] = " "
        array[startposy - 2][startposx + (2 * (x + 2))] = " "
        array[startposy - 1][startposx + (2 * (x + 1))] = " "
        array[startposy - 1][startposx + (2 * (x + 2))] = " "
        for row in array:
            for elem in row:
                print(elem, end=' ')
            print()
        print(" ")
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


def cyclic():
    pass


def multichain():
    pass


main()