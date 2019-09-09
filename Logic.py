def main():
    global cnum
    global hnum
    global list1
    global list2
    global list3
    global list4
    global list5
    cnum = int(input("Enter the number of carbon atoms: "))
    hnum = int(input("Enter the number of hydrogen atoms: "))
    strcnum = str(cnum)
    strhnum = str(hnum)
    global array
    array = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " "]]

    straightchain()


def straightchain():
    fillarray()
    for row in array:
        for elem in row:
            print(elem, end=' ')
        print()

        if hnum == (cnum * 2) + 2:
            alkane()
        elif hnum == cnum * 2:
            alkene()
        elif hnum == cnum and cnum >= 6:
            cyclic()
        else:
            print("Error - Unknown Hydrocarbon")
            main()


def fillarray():  # DOWN AND THEN ALONG - STARTS AT [0][0]
    n = 1
    i = 2 * n
    array[i][i] = "C"
    array[i + 1][i] = "|"
    array[i - 1][i] = "|"
    array[i][i + 1] = "-"
    array[i][i - 1] = "-"
    if cnum > 1:
        for x in range(cnum - 1):
            array[i][(x + 2) * i] = "C"
            array[i + 1][i * (x + 2)] = "|"
            array[i - 1][i * (x + 2)] = "|"
            array[i][(i * (x + 2)) + 1] = "-"
            array[i][(i * (x + 2)) - 1] = "-"


def alkane():
    pass


def alkene():
    pass


def cyclic():
    pass


main()