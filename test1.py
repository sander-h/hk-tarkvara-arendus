""" kommentarr

"""

x = 12
print(x)

print("tere")

a = b = c = 12.5
a,b,c,d = 3,5.7,'tere',True

#konstant
PI = 3.14
true = True
false = False
d = true

x=0.1+0.1+0.1-0.3 #vastus vigane

sX = "string \"abc\""
sY = "see on \\ jagamismark"

sZ = '-' * 20
sX[-5:] #viimased 5
sX[2:] #teisest l6ppu
sX[0:30:2] #yle teise
sX[30:0:-1] #loeb tagurpidi
sX[::-1] #k6ik tagurpidi

# teksti n2itamine
print(sX[::-1])
print('t2na on ',-9,'kraadi', sep='')
print('t2na on ' + str(-9) + ' kraadi')
sNew = "Tere, t2na on {t} kraadi {s}".format(t=-9,s='kylma')

# input
sisend = input("Sisesta number 0..50:")
print('Sa sisestasid: {}'.format(sisend))

# nimekirjad / arrays
list = [5,3,3,true] #loob array
listLen = len(list) #array pikkus
list.append(18) #paneb l6ppu uue elemendi
list.insert(2,'uus tekst') #lisab vahele, liigutab teisi
del list[2] #kusutab vahelt
del list[3]
list2 = [1,2,3,4,5,6]
list3 = list + list2
list2Min = min(list2) #miinimum v22rtus listis
list3Count3 = list3.count(3) #loeb 3med
list3Sorted = sorted(list3) #loob uue sorditud listi
list3.sort() #sordib vana listi