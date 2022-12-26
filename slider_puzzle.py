"""
Given an NxN board representation of a slider puzzle, and starting positon marked as 0, search for and return a series of moves Up,Down,Left,Right (U,D,L,R) that will solve the puzzle.
"""

import heapq


"""
example_board = [[6,4,5],
	 [3,2,7],
	 [8,1,0]]
"""

"""
example_board = [[6,14,11,12],
	 [4,13,7,1],
	 [15,3,9,8],
	 [10,2,5,0]]
"""

example_board = [[6,1,8,14,15],
		 [11,24,2,10,5],
		 [17,16,7,13,23],
		 [21,4,12,20,9],
		 [0,22,19,18,3]]

def idx(val,a_2d_list):
	for j in range(len(a_2d_list)):
		for i in range(len(a_2d_list)):
			if val == a_2d_list[j][i]:
				return (i,j)
	return None

def dist(p1,p2):
	return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def score(a,b):
	s = 0
	for val in range(len(a)*len(a)-1):
		s += dist(idx(val+1,a),idx(val+1,b))
	return s

def solve(board):
	print("Solving:",board)
	dim = len(board) # assume square board
	solved_board = [] # build a solved board to check against
	for i in range(dim):
		solved_board.append([ j+(dim*i)+1 for j in range(dim) ])
	solved_board[dim-1][dim-1] = 0
	seen = set()
	q = []
	heapq.heapify(q)
	heapq.heappush(q,(score(solved_board,board),board,''))
	seen.add(hash(tuple([ tuple(x[:]) for x in board ])))
	while len(q) > 0:
		junk,b,moves = heapq.heappop(q)
		if b == solved_board:
			return moves.strip(',')
		elif len(moves) < 351*2:
			x,y = None,None
			for j in range(dim):
				for i in range(dim):
					if b[j][i] == 0:
						x,y = i,j
			for dx,dy,char in ((0,-1,'U'),(0,1,'D'),(-1,0,'L'),(1,0,'R')):
				nx,ny = x+dx,y+dy
				if nx >= 0 and nx < dim and ny >= 0 and ny < dim: # not over the edge
					next_b = [ x[:] for x in b ]
					tmp = next_b[ny][nx]
					next_b[ny][nx] = b[y][x]
					next_b[y][x] = tmp
					state = hash(tuple([ tuple(x[:]) for x in next_b ]))
					if state not in seen:
						seen.add(state)
						heapq.heappush(q,(score(solved_board,next_b),[ x[:] for x in next_b ],moves+','+char))
		
print(solve(example_board))
