from chessLib_moves import *
from chessLib_tree import *
from random import *
def tchessPlayer(board,player):
	firstmove = genboard()
    
	pos = GetPlayerPositions(board,player)
	print "pos" ,pos
	okmoves = []
	candidateMoves = []
	for i in pos:
		candidates = GetPieceLegalMoves(board,i)
		for k in candidates:
			move = [i,k]
			candidateMoves = candidateMoves +[move]
	
			for j in candidateMoves:
				if IsPositionUnderThreat(board,j[1],player)==False:
					move = [i,j[1]]
					okmoves = okmoves + [move]
	if board == firstmove:
                if player == 10:
			move = [11,19]
                        return [True,move,candidateMoves,None]

	length = len(okmoves)
	x = randint(0,length-1)
	move = okmoves[x]
	return [True, move, candidateMoves, None]
	
				
def chessPlayer(board,player):
	firstmove = genboard()
	if board == firstmove:
		if player == 10:
			return [True,[11,19],candidateMoves,None]
	else:
		stuff = createCandidateAndTree(board,player)
		
		candidateMoves = stuff[0]
		if candidateMoves == []:
			status = False
			return [status,[],[],None]
		status = True
		
		evalTree = stuff[1].GetLevelOrder()
		max1 = -1000
		min1 = 1000
		if bestmove!= False:
			move = stuff[2]
		else:

			max1 = -1000
			min1 = 1000
			if player == 10:
				for i in candidateMoves:
					if i[1]>max1:
						move = i[0]
						max1 = i[1]
			else:
				for i in candidateMoves:
					if i[1]<min1:
						move = i[0]
						min1 = i[1]
			

	return [status, move, candidateMoves, evalTree]

def createCandidateAndTree(board,player):
	if player == 10:
		opp = 20
	if player  == 20:
		opp = 10
	goodmoveslist = []
	evalu = tree([[0,0],0.0])
	candidateMoves = []
	
	pos = GetPlayerPositions(board,player)
	
	for i in pos:
		candidates = GetPieceLegalMoves(board,i)
		wbest = -100000.0
		bbest = 100000.0
		for j in candidates:
			move = [i,j]
			score = assignScore(board,player,i,j)
			temp = [move,score]
			candidateMoves = candidateMoves + [temp]
			if (player == 10 and score > 0) or (player == 20 and score < 0):
				tempnode = tree(temp)
				evalu.AddSuccessor(tempnode)
				tboard = testboard(board,i,j)
				oppos = GetPlayerPositions(tboard,opp)
				if oppos == []:
					bestmove = False
				for k in oppos:
			
					opcan = GetPieceLegalMoves(tboard,k)
					for l in opcan:
						if opcan == []:
							bestmove = False
						score2 = assignScore(tboard,player,k,l)
						temp2 = [[k,l],score2]
						overall = score + score2
						print overall
						if player == 10:
							if overall > wbest:
								bestmove = [i,j]
								wbest = overall
						if player == 20:
							if overall < bbest:
								bestmove = [i,j]
								bbest = overall
						temp2node = tree(temp2)
						print bestmove
						tempnode.AddSuccessor(temp2node)																															
	return [candidateMoves, evalu, bestmove]

def testboard(board,position,move):
	testboard = list(board)
	a = testboard[position]
	testboard[position] = 0
	if move in range(0,64):
		testboard[move] = a
	return testboard		 

def assignScore(board,player,position,move):
	threat = 0.0
	if IsPositionUnderThreat(board,move,player)== True:
		if player == 10:
			threat = -1.0
		if player == 20:
			threat = 1.0

	tboard = testboard(board,position,move)
	
	kingcheckscore = 0.0
	
	

	if isKingInCheck(tboard,10):
		kingcheckscore = -0.3
	if isKingInCheck(tboard,20):
		kingcheckscore = 0.3

	whitepoints = [[10,0.05],[11,0.20],[12,0.25],[13,0.5],[14,0.8]]
	blackpoints = [[20,-0.05],[21,-0.20],[22,-0.25],[23,-0.5],[24,-0.8]]
	goodpos = [27,28,35,36]
	okpos = [18,19,20,21,26,29,34,37]
	

	wp = 0.0
	bp = 0.0
	ws = 0.0
	bs = 0.0

	for i in tboard:
		if i!=0:
			for j in whitepoints:
				if i in j:
					ws = ws + j[1]
					break
			for j in blackpoints:
				if i in j:
					bs = bs + j[1]
					break
	
	for i in goodpos:
		if tboard[i]-10 >= 0 and tboard[i] - 10 <5:
			wp = wp + 0.1
		if tboard[i]-20 >-0 and tboard[i] - 20 <5:
			bp = bp - 0.1
	for i in okpos:
		if tboard[i]-10 >= 0 and tboard[i] - 10 <5:
			wp = wp + 0.1
		if tboard[i]-20 >-0 and tboard[i] - 20 <5:
			bp = bp - 0.1

	totalscore = threat + kingcheckscore + wp + bp + ws + bs
	return totalscore
