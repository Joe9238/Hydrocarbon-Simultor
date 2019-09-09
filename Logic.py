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
    array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

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
    n = 1
    i = 2 * n
    array[i][i] = n
    array[i + 1][i] = "|"
    array[i - 1][i] = "|"
    array[i][i + 1] = "-"
    array[i][i - 1] = "-"
    if cnum > 1:
        for x in range(cnum - 1):
            array[i][(x + 2) * i] = x + 2
            array[i + 1][i * (x + 2)] = "|"
            array[i - 1][i * (x + 2)] = "|"
            array[i][(i * (x + 2)) + 1] = "-"
            array[i][(i * (x + 2)) - 1] = "-"
    for x in range(cnum):
        array[i + 2][(2 * x) + 2] = "H"
        array[i - 2][(2 * x) + 2] = "H"
    array[i][i - 2] = "H"
    array[i][(i * cnum) + 2] = "H"

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
    n = 1
    i = 2 * n
    array[i][i] = n
    array[i + 1][i] = "|"
    array[i - 1][i] = "|"
    array[i][i + 1] = "-"
    array[i][i - 1] = "-"
    if cnum > 1:
        for x in range(cnum - 1):
            array[i][(x + 2) * i] = x + 2
            array[i + 1][i * (x + 2)] = "|"
            array[i - 1][i * (x + 2)] = "|"
            array[i][(i * (x + 2)) + 1] = "-"
            array[i][(i * (x + 2)) - 1] = "-"
    for x in range(cnum):
        array[i + 2][(2 * x) + 2] = "H"
        array[i - 2][(2 * x) + 2] = "H"
    array[i][i - 2] = "H"
    array[i][(i * cnum) + 2] = "H"

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