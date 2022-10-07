class region:
    def _init_(self, rName, rColor):
        self.rName = rName  
        self.rColor = rColor  
        self.adjecentRegions = []  
    def setAdjacentR(self, adjecentRegions):
        self.adjecentRegions = adjecentRegions 
def printState():
    print("WA  color: ", WA.rColor)
    print("NT color: ", NT.rColor)
    print("SA color: ", SA.rColor)
    print("Q color: ", Q.rColor)
    print("NSW color: ", NSW.rColor)
    print("V color: ", V.rColor)
    print("T : ", T.rColor)
def validateInput(color):
    colors = ['Red', 'Green',  'Blue']
    if color in colors:
        return True
    else:
        print("Invalid color input")
        return False
def validateColor(region, color):
    colors_of_Adjacent_r = [region.rColor for region in region.adjecentRegions]
    if color in colors_of_Adjacent_r:
        print("one of the Adjacent region has same color!!")
        print("!!!!! GAME OVER !!!!!")
        return False
    else:
        return True
def clearMemory():
    WA.rColor = 'white'
    NT.rColor = 'white'
    SA.rColor = 'white'
    Q.rColor = 'white'
    NSW.rColor = 'white'
    V.rColor = 'white'
    T.rColor = 'white'
N = 7
WA = region('WA','White')
NT = region('NT','White')
SA = region('SA','White')
Q = region('Q','White')
NSW = region('NSW','White')
V = region('V','White')
T = region('T','White')
WA.setAdjacentR([NT,SA])
NT.setAdjacentR([WA,SA,Q])
SA.setAdjacentR([WA,NT,Q,NSW,V])
Q.setAdjacentR([NT,SA,NSW])
NSW.setAdjacentR([V,SA,Q])
V.setAdjacentR([SA, NSW])
T.setAdjacentR([])
while (True):
    print("===================NEW GAME==================")
    print("Red, Green, Blue")
    c1 = input("Enter color for Western Australia: ")
    if (validateInput(c1)):
        WA.rColor = c1
        printState()
    else:
        clearMemory()
        continue

    print("============================================")
    c2 = input("Enter color for Northern Territory:")
    if (validateInput(c2) and validateColor(NT, c2)):
        NT.rColor = c2
        printState()
    else:
        clearMemory()
        continue

    print("============================================")
    c3 = input("Enter color for South Australia: ")
    if (validateInput(c3) and validateColor(SA, c3)):
        SA.rColor = c3
        printState()
    else:
        clearMemory()
        continue

    print("============================================")
    c4 = input("Enter color for Queensland: ")
    if (validateInput(c4) and validateColor(Q, c4)):
        Q.rColor = c4
        printState()
    else:
        clearMemory()
        continue

    print("============================================")
    c5 = input("Enter color for New South Wales: ")
    if (validateInput(c5) and validateColor(NSW, c5)):
        NSW.rColor = c5
        printState()
    else:
        clearMemory()
        continue

    print("============================================")
