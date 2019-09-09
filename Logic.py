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
    list1 = [0, 0, 0, 0, 0]
    list2 = [0, 0, 0, 0, 0]
    list3 = [0, 0, 0, 0, 0]
    list4 = [0, 0, 0, 0, 0]
    list5 = [0, 0, 0, 0, 0]

    global alkane
    global alkene
    global cyclic

    alkane = False
    alkene = False
    cyclic = False

    straightchain()


def straightchain():
    if hnum == (cnum * 2) + 2:
        alkane = True
        alkane()
    elif hnum == cnum * 2:
        alkene = True
        alkene()
    elif hnum == cnum and cnum >= 6:
        cyclic = True
        cyclic()
    else:
        print("Error - Unknown Hydrocarbon")
        main()


def alkane():
    pass


def alkene():
    pass


def cyclic():
    pass

