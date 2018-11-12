string = str(input())
ints = 0
inte = 0
i=0
resultstr =''
while(i<len(string)):
	chet = 0
	while(47<ord(string[i])<58):
		chet = (ord(string[i])-48)+ chet*10
		i+=1
	print(chet)
	if (string[i] == 'N'):
		ints+=chet
	elif (string[i] == 'S'):
		ints-=chet
	elif (string[i] == 'W'):
		inte+=chet
	elif (string[i] == 'E'):
		inte-=chet	
	i+=1
print(inte)
print(ints)
if (inte < 0):
	resultstr =str((-1)*inte)+'E'
elif(inte > 0):
	resultstr = str(inte)+'W'

if (ints < 0):
	resultstr = resultstr+str((-1)*ints)+'S'
elif(ints > 0):
	resultstr = resultstr+str(ints)+'N'
print(string)
print(resultstr)
