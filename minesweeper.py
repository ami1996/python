import random

game = [["" for x in range(8)] for x in range(8)]
lst = [-9,-8,-7,-1,1,7,8,9]
bom = random.sample(range(64),10)
print(bom)

for i in range(10):
	game[bom[i]//8][bom[i]%8] = '*'

for i in range(64):
	if(game[i//8][i%8] != '*'):
		game[i//8][i%8] = 0
		for j in range(8):
			if((i + lst[j]) >= 0 and (i + lst[j]) < 64):
				if(game[(i + lst[j])//8][(i + lst[j])%8] == '*'):
					if(abs((i + lst[j])%8 - i%8) <= 1):
						game[i//8][i%8] += 1

for i in range(8):
	print(game[i])

maze = [["_" for x in range(8)] for x in range(8)]

for i in range(8):
	print(maze[i])

pos = int(input())
while(game[pos//8][pos%8] != '*'):
	if(game[pos//8][pos%8] == 0):
		for j in range(8):
			if((pos + lst[j]) >= 0 and (pos + lst[j]) < 64):
				if(abs((pos + lst[j])%8 - pos%8) <= 1):
					maze[(pos + lst[j])//8][(pos + lst[j])%8] = str(game[(pos + lst[j])//8][(pos + lst[j])%8])
	maze[pos//8][pos%8] = str(game[pos//8][pos%8])
			
	for i in range(8):
		print(maze[i])
	pos = int(input())

for i in range(10):
	maze[bom[i]//8][bom[i]%8] = '*'

for i in range(8):
	print(maze[i])
