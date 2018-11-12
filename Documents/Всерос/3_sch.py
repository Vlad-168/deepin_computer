import math
a = int(input())
cor = int(a**0.5)
mas = []
for i in range(1,cor):
	if a%i == 0:
		mas.append(a//i)
		mas.append(i)
mas.sort()
gr = a
num = 0	
while(gr>1):
	result = int(gr**0.5)**2
	if result == gr:
		break
	else:
		num+=1
		gr = int(a/mas[num])
print(gr)
