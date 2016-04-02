
from random import shuffle

def Manhattan(puzzle):
	distance = 0
	for i in range(len(puzzle)):
		if(puzzle[i] is not -1):
			#print puzzle[i] , "------"
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

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K
def CmpPuzzle(p1,p2):
	return Manhattan(p1) - Manhattan(p2)
def PossibleMoves(puzzle):
	al = []
	empty = puzzle.index(-1);
	row = empty /3
	col = empty %3
	#print (str(row)+	"-"+str(col))
	tmp = list(puzzle)
	if row  > 0:
		tmp[empty] = tmp[(row -1)*3+col]
		tmp[(row -1)*3+col] = -1
		al.append(list(tmp))
	tmp = list(puzzle)
	if row +1 < 3:
		tmp[empty] = tmp[(row +1)*3+col]
		tmp[(row +1)*3+col] = -1
		al.append(list(tmp))
	tmp = list(puzzle)
	if col > 0:
		tmp[empty] = tmp[row*3+col-1]
		tmp[row*3+col-1] = -1
		al.append(list(tmp))
	tmp = list(puzzle)
	if col + 1 < 3:
		tmp[empty] = tmp[row*3+col+1]
		tmp[row*3+col+1] = -1
		al.append(list(tmp))
	return al
def ToString(puzzle):
	return str(puzzle)
def BeamItUp(puzzle, w):
	
	l = []
	ll = []
	ll.append(puzzle)
	count = 0
	dic = {}
	dic[ToString(puzzle)] = 1
	while(Manhattan(ll[0]) is not 0 and count < 1000):
		l = []
		for i in range(w):
			if i >= len(ll):
				break
			moves = PossibleMoves(ll[i])
			dic[ToString(ll[i])] = 1
			for pz in moves:
				if ToString(pz) not in dic:
					l.append(pz)

			#l.extend()
		ll = []
		ll.extend(l)
			
		ll = sorted(ll, key= cmp_to_key(CmpPuzzle))
		print ll
		ll = ll[0:w]
		count = count + 1
	
	



def main():
	l = PuzzleGenerator()
	#print l
	#print PossibleMoves(l)
	BeamItUp(l,4)
	
	

main()