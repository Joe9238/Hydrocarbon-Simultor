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

  SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉") # Format subscript
  
  while True: # Loop until a full valid input is made
    while True: # Loop until a valid carbon input is made
      try: # An error will occur if the input is not an integer
        cnum = int(input("Enter the number of carbon atoms: "))
        break # Break the loop due to valid input
      except:
          print("Invalid input") # Notify user of invalid input
          print(" ")

    while True: # Loop until a valid hydrogen input is made
      try: # An error will occur if the input is not an integer
        hnum = int(input("Enter the number of hydrogen atoms: "))
        break # Break the loop due to valid input
      except:
          print("Invalid input") # Notify user of invalid input
          print(" ")

    if hnum == (cnum * 2) + 2: # Valid entry for alkane
      break
    elif hnum == cnum * 2 and cnum > 1: # Valid entry for alkene
      break
    else:
      print("Error - Invalid hydrocarbon entered.") 
      print(" ") # Notify user of invalid input

  strcnum = str(cnum)
  strhnum = str(hnum)

        
def startpos():
  global array
  global rowlen
  array = []
  rowlen = (cnum * 2) + 3 # Row length is the length of the hydrocarbon
  for i in range(5): # 5 is always the height of the hydrocarbon
      array.append([" "] * rowlen) # Form an appropriately sized array
  global startposy
  global startposx
  startposy = (5 // 2) # the Y axis starting position is the middle row 
  startposx = (rowlen // 2) # the X axis starting position is the middle column 



def createchain():
  array[startposy][0] = "H" # Place the initial hydrogen
  array[startposy][rowlen-1] = "H" # Place the final hydrogen
  array[startposy][startposx+cnum] = "-" # Place the final carbon-hydrogen bond
  
  for x in range(cnum): # Fill in the repeated section of the hydrocarbon
    array[startposy][(2*x)+2] = "C"
    array[startposy+1][(2*x)+2] = "|"
    array[startposy-1][(2*x)+2] = "|"
    array[startposy-2][(2*x)+2] = "H"
    array[startposy+2][(2*x)+2] = "H"
    array[startposy][(2*x)+1] = "-"



def definechain():
  if hnum == (cnum * 2) + 2: # If alkane is entered
      createchain() 
      alkane() 
  elif hnum == cnum * 2: # If alkene is entered
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

  # If the carbon number is odd offset the starting position 
  if cnum % 2 == 1: 
    startposx = startposx + 1

  # add comments
  for x in range(cnum // 2):
    array[startposy][startposx+(2*x)] = "="
    array[startposy-2][startposx+(2*x)-1] = " "
    array[startposy-2][startposx+(2*(x+1))-1] = " "
    array[startposy-1][startposx+(2*x)-1] = " "
    array[startposy-1][startposx+(2*(x+1))-1] = " "
    
    printchain()

    array[startposy][startposx+(2*x)] = "-"
    array[startposy-2][startposx+(2*x)-1] = "H"
    array[startposy-2][startposx+(2*(x+1))-1] = "H"
    array[startposy-1][startposx+(2*x)-1] = "|"
    array[startposy-1][startposx+(2*(x+1))-1] = "|"

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
