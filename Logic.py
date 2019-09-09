def main():
    global cnum
    global hnum
    global clist
    global hlist
    global cbondlist
    cnum = int(input("Enter the number of carbon atoms: "))
    hnum = int(input("Enter the number of hydrogen atoms: "))
    strcnum = str(cnum)
    strhnum = str(hnum)
    hlist = []
    clist = []
    cb

    global alkane
    global alkene
    global cyclic

    alkane = False
    alkene = False
    cyclic = False

    global a
    a = hnum // cnum

    straightchain()


def straightchain():  # create lists
    for i in range(cnum):
        if i == 0 or i == (cnum - 1):
            clist.append(1)
        else:
            clist.append(2)
    for i in range(hnum):
        hlist.append(1)
    straightchain2()


def straightchain2():
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
    for i in range(cnum):
        clist[i] == 2
    clist[0] == 3
    clist[-1] == 3

