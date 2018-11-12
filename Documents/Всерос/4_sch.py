a=int(input())
string  = ''

if a == 3:
	string = "++-"
elif a%4!=0:
	string='IMPOSSIBLE'
else:
	a=a//2
	for i in range(a):
		if i%2==0:
			string = '-'+string+'-'
		else:
			string = '+'+string+'+'
print(string)