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


# dictionary
aInimesed = ['Mati', 23, 'Karl', 20, 'Triin', 19] #array
dInimesed = {'Mati': 23, 'Karl': 20, 'Triin': 19} #dictionary
# dInimesed.keys() # tagastab v6tmed
# dInimesed.values() # tagastab v22rtused

mati = aInimesed[1]
mati2 = dInimesed['Mati']

# tuple, teineteisega seotud asjad
dup = (2,3.5,'Mati') #kogumik mida ei saa muuta (funktsioonides)
dupMult = dup*4

# set, ainult unikaalsed v22rtused
hulk = set() #tyhi set
hulk = {'6unad','pirnid','kirsid'} #pole v6tmed, ainult v22rtused
a = set('abracadabra') #ainult unikaalsed t2hed
b = set('KabrDakgu')
c = a - b #hulkade vahe
d = a | b #asjad mis on kas yhes v6i teises
e = a & b #asjad mis on m6lemas
f = a ^ b #xor, asi mis yhes v6i teises, kuid mitte m6lemas

# if
if 2 < 5:
	print('abc')
else:
	print('def')

x = 2
if x > 0:
	print('positiivne')
elif x == 0:
	print('null')
else:
	print('negatiivne')


list = ['element 0','element 1','element 2']

for element in list:
	print(element)

for i in range(0,101,2):
	print(i)

x = 0
while x < 101:
	x = x + 1
	if (x % 2 != 0):
		continue
	print (x)
	if (x == 100):
		break
	else:
		pass


#mingi muu tsykkel
for n in range(0,101):
	if (n % 2 == 0 and n > 2) or n == 1:
		continue
	is_prime = True
	for i in range(3, n):
		if (n % i == 0):
			is_prime = False
			break
	if (is_prime):
		print(str(n)+' on algarv')

while True:
	sisend = input('Sisesta Number, l6petamiseks vajuta ENTER: ')
	if (len(sisend)== 0):
		break
	print('Trykitud: '+ sisend)



a,b = 0,1
while b <= 1000:
	print(b,end = ' ', flush=True)
	a,b = b,a+b

# tsykkel ja else
x = 0
list = [2,5,7,8,10]
for element in list:
	x += element
else: 
	print(x)

l = 0
while l < 5:
	l += 1
else:
	print(l)



#protseduur
def minu_funktsioon():
	print('see on protseduur')
minu_funktsioon()

#functisioon
def liida(a = 0,b = 0,c = 0,d = 0):
	return a+b+c+d

def isPrime(n):
	for i in range(3,n):
		if (n % i) == 0:
			return False
	else:
		return True

nr = 5

if (isPrime(nr)):
	print(f"{nr} on prime")
else:
	print(f"{nr} ei ole prime")

def listPrimes(max_num = 100):
	for n in range (2, max_num):
		if (isPrime(n)):
			print(n,end = ' ')
	print()


listPrimes()

#liida arre
def arrLiida(arr = [0]):
	sum = 0
	for i in arr:
		sum += i
	return sum
#keskmine arre
def arrKeskmine(arr = [0]):
	sum = arrLiida(arr)
	return (sum/(len(arr)))

arrKeskmine([1,2,3,4])


#keskmine tunnis
def keskmine(a,b,c=None,d=None):
	sum = a+b
	argumente = 2

	if (c is not None):
		argumente += 1
		sum += c
	if (d is not None):
		argumente += 1
		sum += d
	return sum/argumente


#t2rn muudab parameetrit listiks
#t2rn muudab ka listi parameetriteks
def liitmine(*arr):
	sum = 0
	for i in arr:
		sum += i
	return sum

# try / except
def numcount(*numbrid):
	sum = numsum(*numbrid)
	count = numcount(*numbrid)
	result = 0.0

	try:
		result = sum/(count*1.0)
	except ZeroDivisionError as err:
		print('numcount - nulliga jagamise viga',err)
		result = 0.0
	except:
		print ('mingi muu viga')
		raise               # kutsub vea uuesti v2lja
	else:                   # kui viga ei juhtu
		print("numcount - tulemus {result}")
	finally:                # igal juhul k2ivitab 
		print('tehtud')

# failide avamine
f = open('minufail.txt')

for rida in f:
	print(rida,end ="")
f.close()

with open('minufail.txt') as f:
	for rida in f:
		print(rida,end="")

# clear console
print("\n\n\n\n\n\n\n\n\n\n\n\n")
print('--- clear ---')


# import test
import mymodule
from mymodule import tere2

mymodule.tere()
tere2()

# kaustast import
import f.functions
f.functions.tere3()
#print(dir(f))


# scope
s_a = 2

def func():
	s_a = 11
	def func2():
		#nonlocal s_a
		s_a = 10
		print('func2:',s_a)
	
	func2()
	print("func:",s_a)

func()
print('V2limine: ',s_a)


# lambda
double = lambda x: x*2
print(double(5),type(double))	# double on funktsioon


# list comperhensions (apply {})
arvude_ruudud = [x**2 for x in range(10)]
print(arvude_ruudud)





# klasssid

class dog:
	def __init__(self, color = "white",colorTail = "grey"):
		self.color = color
		self.colorTail = colorTail
	
	def bark(self):
		print(f"Woof, said {self.color} doggie")
	
#dog.color = "orange"
pontu = dog()
pontu.bark()
sally = dog(color = "orange",colorTail = "white")
sally.bark()
dog.bark(sally)

sally.paws = 4
print(sally.paws)


# polymorfism

from abc import ABCMeta, abstractmethod
class kujund(metaclass = ABCMeta):
	@abstractmethod
	def tutvusta(self):
		pass
		print("Ma ei tea kes ma olen")

class ruut(kujund):
	def tutvusta(self):
		print("Ma olen ruut")

class ring(kujund):
	def tutvusta(self):
		print("Ma olen ring")

class kolmnurk(kujund):
	def tutvusta(self):
		print("Ma olen kolmnurk")

def tutvusta(*kujundid):
	for kujund in kujundid:
		kujund.tutvusta()

list = (kolmnurk(), ruut(), ring())

tutvusta(*list)