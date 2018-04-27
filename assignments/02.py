#print current trips
def f_printList(list=3*[3*["-"]]):
    #x koordinaadid
    mainList = ['1','2','3']
    mainList = [mainList] + list
    yPos = 0
    for xList in mainList:
        if yPos == 1:
            print("--+-+-+")
        print (str(yPos)+" |",end='')
        yPos += 1
        for x in xList:
            print((x + "|"), end='')
        print("")
f_printList()

# return player input for single number
def f_getPlayerInput(hint="Sisesta Number (1/2/3)",hintError="Vigane Number v6i number ei sobi, proovi uuesti",range=[1,2,3]):
    while True:
        print(hint)
        i = int(input())
        if (i in range):
            return i
        else:
            print(hintError)

# returns true if position is empty
def f_canUpdateList(list,xPos=1,yPos=1):
    xList = list[xPos-1]
    return (xList[yPos-1] == "-")

# returns new list with updated value for certain square
def f_updateList(list,posList=[1,1],newVal='-'):
    xPos = posList[0]
    yPos = posList[1]
    list[xPos-1][yPos-1] = newVal
    return list

# loop until player has selected a empty position
def f_getPlayerPos(list,player="x"):
    while True:
        xPos = f_getPlayerInput(hint=player+', vali positsioon x teljel')
        yPos = f_getPlayerInput(hint=player+', vali positsioon y teljel')
        if f_canUpdateList(list):
            return [xPos,yPos]
        else:
            print("Positsioon :"+ str(xPos)+", "+ str(yPos)+" ei sobi")

def f_checkWin(list):
    winner = None
    for player in ["x","y"]:
        score = 0
        d1Score = 0
        d2score = 0
        y1Score = 0
        y2Score = 0
        y3Score = 0
        for y in range(0,2):
            xList = list[y]
            xScore = 0
            for x in range(0,2):
                xVal = xList[x]
                if xVal == player:
                    xScore += 1
                    if x == 0:
                        y1Score += 1
                        if y == 0:
                            d1Score += 1
                        if y == 2:
                            d2score += 1
                    if x == 1:
                        y2Score += 1
                        if y == 1:
                            d1Score += 1
                            d2Score += 1
                    if x == 2:
                        y3Score += 1
                        if y == 2:
                            d1Score += 1
                        if y == 0:
                            d2Score += 1
            if xScore == 3:
                return player

                

def f_play():
    tripsList = 3*[3*["-"]]
    end = None
    print("Trips Traps Trull")
    print("Saa 3 x v6i 3 o j2rjestikku et v6ita")
    print("Kui k6ik ruudud on t2is, siis on viik")
    f_printList(tripsList)
    player = 'x'
    while True:
        if end != None:
            print(end)
            break
        tripsList = f_updateList(tripsList,f_getPlayerPos(tripsList,player))
        f_printList(tripsList)
        if player == 'x':
            player = 'y'
        else:
            player = 'x'

        
        
        

while True:
    if 'tripsList' not in locals() or tripsList == None:
        tripsList = 3*[3*["-"]]
        print("Trips traps trull:")
        f_printList(tripsList)
    else:

        tripsList = None
        
