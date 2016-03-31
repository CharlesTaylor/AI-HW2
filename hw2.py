
from random import shuffle

def PuzzleGenerator():
	lis = [0,1,2,3,4,5,6,7,8]
	shuffle(lis)
	print lis

	okashina = 0
	for i in range(len(lis)):
		if lis[i] is not 0:
			for j in range(i,len(lis)):
				if lis[j] is not 0:
					if(lis[j] < lis[i]):
						okashina = okashina + 1
	if( okashina % 2 is 1):#Not Solvable
		return PuzzleGenerator()
	else:#Solvable so return
		return lis


def BeamItUp(puzzle, w, ):
	pass






def main():
	PuzzleGenerator()




main()