def main():
  global cnum
  global hnum
  global clist
  global hlist
  cnum = int(input("Enter the number of carbon atoms: "))
  hnum = int(input("Enter the number of hydrogen atoms: "))
  strcnum = str(cnum)
  strhnum = str(hnum)
  hlist = []
  clist = []
  #Make settings false
  schain = False

  print("Straight chain?")
  while True:
    a = str(input("Y or N: "))
    if a == "Y":
      schain = True
      break
    elif a == "N":
      schain = False
      break

  if schain == True:
    straightchain()
  else:
    print("False")

def straightchain():
  for i in range(cnum):
    if i == 0 or i == (cnum-1):
      clist.append(1)
    else:
      clist.append(2)
  for i in range(hnum):
    hlist.append(1)
  straightchain2()

def straightchain2():
    for i in range(hnum):
      if hlist[i] == 1:
        hlist[i] = 0
        for i in range(cnum):
          if clist[i] < 4:
            clist[i] = clist[i] + 1
            break
    for i in range(cnum):
      if clist[i] < 4:
        pass
      else:
        print(clist)
        print(hlist)
        break