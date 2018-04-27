
#suvaline number
ran = 4
ranstr = str(ran)

#proove
p = 0

#loop kuni vastus k2es
print('Arva number:')
while True:
    p += 1
    s = input ()
    if (any((i.isdigit()== False) for i in s)):
        print('Sisendis pole number! Proovi uuesti:')
        continue
    i = float(s)
    if i == ran:
        print('Korrektne tulemus: '+ranstr)
        print('Proove kokku: '+str(p)+'')
        break
    elif (i > ran):
        print ('VALE! Liiga suur! Proovi uuesti:')
    elif (i < ran):
        print ('VALE! Liiga v2ike! Proovi uuesti:')
