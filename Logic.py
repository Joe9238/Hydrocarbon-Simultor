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

  SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
  SUBimp = str.maketrans("(2n+2)-", "₍₂ₙ₊₂₎₋")
  SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
  
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
    elif hnum == cnum * 2 and cnum > 1:
      break
    else:
      print("Error - Invalid hydrocarbon entered.")
      print(" ")

  strcnum = str(cnum)
  strhnum = str(hnum)

        
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
  array[startposy][rowlen-1] = "H"
  array[startposy][startposx+cnum] = "-"
  
  for x in range(cnum):
    array[startposy][(2*x)+2] = "C"
    array[startposy+1][(2*x)+2] = "|"
    array[startposy-1][(2*x)+2] = "|"
    array[startposy-2][(2*x)+2] = "H"
    array[startposy+2][(2*x)+2] = "H"
    array[startposy][(2*x)+1] = "-"



def definechain():
  if hnum == (cnum * 2) + 2:
      createchain()
      alkane()
  elif hnum == cnum * 2:
      createchain()
      alkene()
      


def alkane(): 
  printchain()
  
  print("""
  """)
  molformula = str("C" + strcnum + "H" + strhnum)
  print("The molecular formula of the hydrocarbon is " + molformula.translate(SUB))
  print("The hydrocarbon is an alkane")

def alkene():
  global startposx
  if cnum == 2:
    startposx = startposx - 1
  for x in range(cnum // 2):
    array[startposy][startposx+(2*(x+1))-1] = "="
    array[startposy-2][startposx+(2*(x+1))-2] = " "
    array[startposy-2][startposx+(2*(x+2))-2] = " "
    array[startposy-1][startposx+(2*(x+1))-2] = " "
    array[startposy-1][startposx+(2*(x+2))-2] = " "
    
    printchain()

    array[startposy][startposx+(2*(x+1))-1] = "-"
    array[startposy-2][startposx+(2*(x+1))-2] = "H"
    array[startposy-2][startposx+(2*(x+2))-2] = "H"
    array[startposy-1][startposx+(2*(x+1))-2] = "|"
    array[startposy-1][startposx+(2*(x+2))-2] = "|"

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

main()
