#print current trips
def f_printList(list=3*[3*["-"]]):
    #x koordinaadid
    mainList = ['1','2','3']
    mainList = [mainList] + list
    yPos = 0
    for xList in mainList:
        if yPos == 1:
            print()
        print (str(yPos)+" |",end='')
        yPos += 1
        for x in xList:
            print((x + "|"), end='')
        print("")
f_printList()

#get input for player
def f_getPlayerInput(hint="Sisesta Number (1/2/3)",hintError="Vigane Number v6i number ei sobi, proovi uuesti",range=[1,2,3]):
    while True:
        print(hint)
        i = int(input())
        if (i in range):
            return i
        else:
            print(hintError)
def f_canUpdateList(list,xPos=1,yPos=1):
    xList = list[xPos-1]
    return (xList[yPos-1] == "-")
def f_updateList(list,offSet=-1,xPos=1,yPos=1,newVal='-')
    list[xPos+offSet][yPos+offSet] = newVal
    return list
def f_getPlayerPos(player="x"):
    while True:
        xPos = f_getPlayerInput(hint='X, vali positsioon x teljel')
        yPos = f_getPlayerInput(hint='X, vali positsioon y teljel')


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
        if player == 'x':

        
        
        

while True:
    if 'tripsList' not in locals() or tripsList == None:
        tripsList = 3*[3*["-"]]
        print("Trips traps trull:")
        f_printList(tripsList)
    else:

        tripsList = None
        
