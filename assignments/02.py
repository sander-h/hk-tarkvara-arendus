
#print current trips
def f_printList(list=3*[3*["-"]],clear=False):
    if clear:    
        for i in range(0,30):
            print("")

    #x koordinaadid
    mainList = [['1','2','3','<-X TELG']]
    mainList = mainList + list
    yPos = 0
    for xList in mainList:
        print (str(yPos)+" |",end='')
        yPos += 1
        for x in xList:
            print((x + "|"), end='')
        print("")

# return player input for single number
def f_getPlayerInput(hint="Sisesta Number (1/2/3)",hintError="Vigane Number v6i number ei sobi, proovi uuesti",range=[1,2,3]):
    while True:
        print(hint)
        i = input()
        
        # player quit check
        if not bool(i) or i is "":
            return False

        # check if pos is in allowed range
        i = int(i)
        if (i in range):
            return i
        else:
            print(hintError)

# returns true if position is empty
def f_canUpdateList(list,xPos=1,yPos=1):
    yList = list[yPos-1]
    return (yList[xPos-1] == "-")

# returns new list with updated value for certain square
def f_updateList(list,posList=[1,1],newVal='-'):

    # player exit check
    if posList is False:
        return False

    xPos = posList[0]
    yPos = posList[1]
    list[yPos-1][xPos-1] = newVal
    return list

# loop until player has selected a empty position
def f_getPlayerPos(list,player="x"):
    while True:
        f_printList(list)
        xPos = f_getPlayerInput(hint=player+', vali positsioon x teljel')

        # player exit check
        if xPos is False:
            return False

        yPos = f_getPlayerInput(hint=player+', vali positsioon y teljel')

        # player exit check
        if yPos is False:
            return False

        if f_canUpdateList(list,xPos,yPos):
            return [xPos,yPos]
        else:
            print("Positsioon :"+ str(xPos)+", "+ str(yPos)+" ei sobi")

def f_checkWin(list):
    for player in ["x","y"]:
        d1Score = 0
        d2Score = 0
        y1Score = 0
        y2Score = 0
        y3Score = 0
        y = -1

        # rows (3x)
        for yList in list:
            y += 1
            x = -1
            xScore = 0

            # elements in rows (3x)
            for val in yList:
                x += 1
                if val == player:
                    xScore += 1
                    if x == 0:
                        y1Score += 1
                        if y == 0:
                            d1Score += 1
                        if y == 2:
                            d2Score += 1
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
        if d1Score == 3 or d2Score == 3 or y1Score == 3 or y2Score == 3 or y3Score == 3:
            return player
    return None
                

def f_play():
    global tripsList
    tripsList = [["-","-","-"],["-","-","-"],["-","-","-"]]
    end = None
    print("Trips Traps Trull")
    print("Saa 3 x v6i 3 o j2rjestikku et v6ita")
    print("Kui k6ik ruudud on t2is, siis on viik")
    print("2ra sisesta midagi ja vajuta enter et m2ngu l6petada")
    #f_printList(tripsList,False)
    player = 'x'
    plays = 0
    while True:
        plays += 1
        tripsList = f_updateList(tripsList,f_getPlayerPos(tripsList,player),player)

        # player exit check
        if tripsList is False:
            print(f'{player} l6petas m2ngu.')
            break

        #f_printList(tripsList)
        winner = f_checkWin(tripsList)
        if winner != None:
            f_printList(tripsList,True)
            end = f'{winner} on v6itja'
        elif plays == 9:
            f_printList(tripsList,True)
            end = 'viik'
        if player == 'x':
            player = 'o'
        else:
            player = 'x'
        if end != None:
            print(end)
            break

f_play()

