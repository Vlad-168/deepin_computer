import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv

class comand:
	def __init__(self):
		self.name = ''
		self.points = 0
		self.wins = 0
		self.loses = 0
		self.qwerty = 0

f=open("text.txt")
data = f.readlines() # read ALL the lines!
length = len(data)
mas=['']*length
results = []
peer = []
for i in range(0,length):
	peer.append(comand())
	mas[i] = data[i][:-1]
	s=mas[i]
	indexs = s.find(" ")
	peer[i].name = s[:indexs]
	mas[i] = s[indexs:]
	results.append(list(map(int,mas[i].split())))

results[length-1].append(0)

for i in range(0,length):
	for j in range(0,length):
		if results[i][j]>results[j][i]:
			peer[i].wins+=1
		elif results[i][j] < results[j][i]:
			peer[i].loses+=1
		elif results[i][j] == results[j][i]:
			peer[i].qwerty+=1
print("----------Score-------------")
for i in range(length):
	res= 3*peer[i].wins+2*peer[i].qwerty+peer[i].loses
	peer[i].points = res
	print(peer[i].name, peer[i].points)
	i_name = peer[i].name
	i_score = peer[i].points 
print("____________Finish____________")
#__________START_SORT_________________
n=1
while n<length:
	for i in range(length-n):
		if peer[i].points<peer[i+1].points:
			#tmp = mas[i]
			#mas[i] = mas[i+1]
			#mas[i+1] = tmp
			peer[i].wins, peer[i+1].wins = peer[i+1].wins, peer[i].wins
			peer[i].qwerty, peer[i+1].qwerty = peer[i+1].qwerty, peer[i].qwerty
			peer[i].loses, peer[i+1].loses = peer[i+1].loses, peer[i].loses
			peer[i].name, peer[i+1].name = peer[i+1].name, peer[i].name
			peer[i].points, peer[i+1].points = peer[i+1].points, peer[i].points

	n+=1
#___________END_SORT______________
col_labels = ['Wins','Lose', 'Draw', 'Score']
row_labels = ['']*length
for i in range(length):
	row_labels[i] = peer[i].name
table_vals = []
for i in range(length):
	table_vals.append([])
	for j in range(4):
		if j == 0:
			table_vals[i].append(peer[i].wins)
		elif j == 1:
			table_vals[i].append(peer[i].loses)
		elif j == 2:
			table_vals[i].append(peer[i].qwerty)
		elif j == 3:
			table_vals[i].append(peer[i].points)
#Построение диаграммы
data_names = ['']*length
data_values = [0]*length
for i in range(length):
	data_names[i] = peer[i].name
	data_values[i] = peer[i].points
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (500 / dpi, 200 / dpi) )
mpl.rcParams.update({'font.size': 9})

plt.title('Процентное соотношение очков ')

xs = range(len(data_names))
the_table = plt.table(cellText = table_vals,
					colWidths = [0.2]*length,
					rowLabels = row_labels,
					colLabels = col_labels,
					loc='left')
plt.pie( 
    data_values, autopct='%0.1f', radius = 1.,
    explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
plt.legend(
    bbox_to_anchor = (1., 0.10, 0.70, 0.25),
    loc = 'lower right', labels = data_names )
fig.savefig('pie.png')
plt.show()

f.close()