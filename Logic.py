def main():
    global cnum
    global hnum
    global strcnum
    global strhnum
    global SUB
    global SUBimp
    global SUP
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    SUBimp = str.maketrans("(2n+2)-", "₍₂ₙ₊₂₎₋")
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    cnum = int(input("Enter the number of carbon atoms: "))
    hnum = int(input("Enter the number of hydrogen atoms: "))
    strcnum = str(cnum)
    strhnum = str(hnum)
    global array
    array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    global startposy
    global startposx
    rownum = 0
    for row in array:
        rowlen = len(row)
        rownum = rownum + 1

    startposy = rownum // 2
    startposx = (rowlen // 2) - cnum + 1

    straightchain()


def straightchain():
    if hnum == (cnum * 2) + 2:
        alkane()
    elif hnum == cnum * 2:
        alkene()
    elif hnum == cnum and cnum >= 6:
        cyclic()
    else:
        print("Error - Unknown Hydrocarbon")
        main()


def alkane():  # DOWN AND THEN ALONG - STARTS AT [0][0]
    array[startposy][startposx] = 1
    array[startposy + 1][startposx] = "|"
    array[startposy - 1][startposx] = "|"
    array[startposy][startposx + 1] = "-"
    array[startposy][startposx - 1] = "-"
    array[startposy][startposx - 2] = "H"
    array[startposy][(2 * cnum) + startposx] = "H"
    array[startposy + 2][startposx] = "H"
    array[startposy - 2][startposx] = "H"
    if cnum > 1:
        for x in range(cnum - 1):
            for row in array:
                for elem in row:
                    if elem == (x + 1):
                        colnum = row.index(x + 1)
            array[startposy][colnum + 2] = x + 2
            array[startposy + 1][colnum + 2] = "|"
            array[startposy - 1][colnum + 2] = "|"
            array[startposy - 2][colnum + 2] = "H"
            array[startposy + 2][colnum + 2] = "H"
            array[startposy][colnum + 3] = "-"
            array[startposy][colnum + 1] = "-"

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
    array[startposy][startposx] = 1
    array[startposy + 1][startposx] = "|"
    array[startposy - 1][startposx] = "|"
    array[startposy][startposx + 1] = "-"
    array[startposy][startposx - 1] = "-"
    array[startposy][startposx - 2] = "H"
    array[startposy][(2 * cnum) + 2] = "H"
    array[startposy + 2][startposx] = "H"
    array[startposy - 2][startposx] = "H"
    if cnum > 1:
        for x in range(cnum - 1):
            for row in array:
                for elem in row:
                    if elem == (x + 1):
                        colnum = row.index(x + 1)
            array[startposy][colnum + 2] = x + 2
            array[startposy + 1][colnum + 2] = "|"
            array[startposy - 1][colnum + 2] = "|"
            array[startposy - 2][colnum + 2] = "H"
            array[startposy + 2][colnum + 2] = "H"
            array[startposy][colnum + 3] = "-"
            array[startposy][colnum + 1] = "-"

    for row in array:
        for elem in row:
            print(elem, end=' ')
        print()

    print("""
  """)
    molformula = str("C" + strcnum + "H" + strhnum)
    print("The molecular formula of the hydrocarbon is " + molformula.translate(SUB))
    print("The hydrocarbon is an alkene")


def cyclic():
    pass


main()