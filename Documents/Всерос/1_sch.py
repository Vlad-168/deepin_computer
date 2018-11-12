A = int(input())
B = int(input())
if (A%2 ==1 and B%2==0):
	B-=1
elif (a%2==0 and B%2==1):
	A-=1
N = int((B-A)/2)
print(N)