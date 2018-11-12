#доп. методы
def chet(x):
	return (x**3+4*x-3)

def proizvod1(x):
	return (3*x**2+4)
def proizvod2(x):
	return(6*x)
#методы
def first(a,b,ch):
	results=0
	chethik=0
	while (chethik!=ch):
		x = (a+b)/2
		results = chet(x)
		if results>0:
		 	b=x
		else:
		 	a=x
		chethik+=1
	print(x)
	print("Количество итераций первым способом:",chethik)
def second(a,b,ch):
	e=0.00000001
	qwer = 0
	while (qwer!=ch):
		if (chet(b)*proizvod2(b)>0):
			while (chet(b)/proizvod1(b)>e):
				b=b-(chet(b)/proizvod1(b))
				print("b:",b)	
		else:
			while (chet(a)/proizvod1(a)>e):
				a=a-(chet(a)/proizvod1(a))
				print("a",a)
		qwer=qwer+1


ch = int(input("e:"))#число знаков после запятой
a=int (input("a:")) 
b=int(input("b:"))
print("--------first-----------")
first(a,b,ch)
print("--------second-----------")
second(a,b,ch)