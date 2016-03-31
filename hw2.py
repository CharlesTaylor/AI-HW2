
from random import shuffle

def Manhattan(puzzle):
	distance = 0
	for i in range(len(lis)):
		if(lis[i] is not -1):
			distance = distance + abs(puzzle[i] % 3 - i % 3) + abs(puzzle[i] / 3 - i /3)

	return distance

def PuzzleGenerator():
	lis = [-1,0,1,2,3,4,5,6,7]#Repsresents value+1
	shuffle(lis)
	#print lis

	okashina = 0
	for i in range(len(lis)):
		if lis[i] is not -1:
			for j in range(i,len(lis)):
				if lis[j] is not -1:
					if(lis[j] < lis[i]):
						okashina = okashina + 1
	if( okashina % 2 is 1):#Not Solvable
		return PuzzleGenerator()
	else:#Solvable so return
		return lis


def BeamItUp(puzzle, w):
	
	l = []
	ll = []
	ll.append(puzzle)
	empty = 0
	empty = puzzle.index(-1);
	row = puzzle[empty] /3
	col = puzzle[empty] %3
	
	print empty



def main():
	l = PuzzleGenerator()
	print l
	BeamItUp(l,3)



main()