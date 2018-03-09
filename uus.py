from random import randint
ran2 = randint(1,10)
#^ suvaline number

#suvaline number
ran = 4
ranstr = str(ran)

#proove
p = 0

#loop kuni vastus k2es
print('Arva number:')
while True:
    s = input ()
    i = float(s)
    p += 1
    if i == ran:
        print('Korrektne tulemus: '+ranstr)
        print('Proove kokku: '+str(p)+'')
        break
    elif (i > ran):
        print ('VALE! Liiga suur! Proovi uuesti:')
    elif (i < ran):
        print ('VALE! Liiga v2ike! Proovi uuesti:')


