def genboard():
	row0 = [13,11,12,15,14,12,11,13]
	row1 = [10 for i in range(0,7)
	rowmiddle = [0 for i in range(0,32)]
	row6 = [20 for i in range(0,7)]
	row7 = [23,21,22,25,24,22,21,23]
	newboard= row0+row1+rowmiddle+row6+row7
	return newboard

def printBoard(board):

	for i in range(63,6,-7):
		print board[i-7:i+1]
		return True

def GetPlayerPositions(board,player):
	if (player!=10 and player!=20):
		return False
	if (len(board) != 64):
		return False
	accum = []
	val = 0
	if player == 10:
		for i in range(0,64,1):
			val = board[i] - 10
			if (val <= 5 and val >= 0):
				accum = accum + [i]
	if player == 20:
		 for i in range(0,64,1):
                        val = board[i] - 20
                        if (val <= 5 and val >= 0):
                                accum = accum + [i]
	return accum

#def DiscoveredCheck(board,position): #check: if opp moves a piece that doesn't check, but another does


def MovePieceCausesCheck(board,position): #if player moves a piece that brings their king into check...USE FOR INVALID CASES in LEGAL MOVES FUNC
	if board[position] == 15 or board[position] == 25:
		print "Cannot test King for 'Move Piece Causes Check"
		return -1

	board[position] = 0
	# check b or w
	if board[position]-20 >=0 and board[position]-20 <=5:
		opponent = 10
		for i in board:	
			if i == 25:
			
				kingposition = i
			break
	if board[position]-10 >=0 and board[position]-10 <=5:
                opponent = 20
		for i in board:
                        i == 15:
			
                        	kingposition = i
                        break

	# check position of player's king
	# get playersposition of opp
	opponentloc = getPlayerPositions(board,opponent)
	
	# if legalmoves of any opp players == king pos
	for i in opponentloc:
		opplegal = GetPieceLegalMoves(board,i)
		for j in opplegal:
			if j == kingposition:
				return True
	# return TRUE (means you have no legal moves for player)  
	return False

def isKingInCheck(board,player): # for LEGAL MOVES: make sure if K in check, legal moves are ones that bring King OUT of check
	if player == 10:
		opponent = 20
		for i in board:
			if i == 15:
				kingposition = i
	if player == 20:
		opponent = 10
                for i in board:
                        if i == 25:
                                kingposition = i
	
	opponentloc = getPlayerPositions(board,opponent)

        # if legalmoves of any opp players == king pos
        for i in opponentloc:
                opplegal = GetPieceLegalMoves(board,i)
                for j in opplegal:
                        if j == kingposition:
                                return True
      
	return False
				
	
def GetPieceLegalMoves(board,position):
	moves = GetMoves(board,position)
	if board[position] - 20 >= 0 and board[position] - 20 <=5:
		player = 20
	if board[position] - 10 >= 0 and board[position] - 10 <=5:
		player = 10	
	accum = []
	if isKingInCheck(board,player):
		for i in moves:
			testboard = list(board)
			testboard[position] = 0
			testboard[i] = board[position]
			if isKingInCheck(testboard,player) == False:
				accum = accum + [i]
		return accum	
			
	else:
		return moves
		
def GetMoves(board,position):
	#if isKingInCheck:
		
	if len(board) != 64:
		return False
	if board[position] == 0:
		return False
	if board[position]!=15 and board[position]!=20:
		if MovePieceCausesCheck(board,position):
			return []

	wpos = GetPlayerPositions(board,10)
	bpos = GetPlayerPositions(board,20)
	accum = []
	if board[position] == 10: #white pawn

		if position+8 <=63:
			if board[position+8] == 0:
				accum = accum + [position+8]
		if position%8 == 0:  #checking if it is a left border case, so one diagonal is invalid
			if position+9 <=63:
				if (board[position+9]-20) <= 5 and (board[position+9]-20) >= 0:
					accum = accum + [position + 9]
		else if position%8 == 7:  #checking if it is a right border case, so one diagonal is invalid
                        if position+7 <=63:
                                if (board[position+7]-20) <= 5 and (board[position+7]-20) >= 0:
                                        accum = accum + [position + 7]
		else:
			if position+9 <=63:
                                if (board[position+9]-20) <= 5 and (board[position+9]-20) >= 0:
                                        accum = accum + [position + 9]
			if position+7 <=63:
                                if (board[position+7]-20) <= 5 and (board[position+7]-20) >= 0:
                                        accum = accum + [position + 7]
	if board[position] == 20: #black pawn

                if position-8 >=0:
                        if board[position-8] == 0:
                                accum = accum + [position-8]
                if position%8 == 0:  #checking if it is a left border case, so one diagonal is invalid
                        if position-7 >=0:
                                if (board[position-7]-10) <= 5 and (board[position-7]-10) >= 0:
                                        accum = accum + [position -7]
                else if position%8 == 7:  #checking if it is a right border case, so one diagonal is invalid
                        if position-9 >=0:
                                if (board[position-9]-10) <= 5 and (board[position-9]-10) >= 0:
                                        accum = accum + [position -9]
                else:
                        if position-7 >=0:
                                if (board[position-7]-10) <= 5 and (board[position-7]-10) >= 0:
                                        accum = accum + [position - 7]
                        if position-9 >=0:
                                if (board[position-9]-10) <= 5 and (board[position-9]-10) >= 0:
                                        accum = accum + [position - 9]
	if board[position] == 13: #white rook
		rowleft = position - position%8
		rowright = rowleft + 7
		colbot = position%8
		coltop = 56 + position%8
		
		#ONCE COMPUTED, BOUNDS ARE INCLUSIVE,THEREFORE VALID POSITIONS
		leftbound = rowleft
		rightbound = rowright
		topbound = coltop
		botbound = colbot

		for i in range (rowleft,position,1):
			if i in bpos:
				leftbound = i
			if i in wpos:
				leftbound = i+1
		for j in range (colbot,position,8):
			if j in bpos:
				botbound = j
			if j in wpos:
				botbound = j+8
		for k in range(rowright,position,-1):
			if k in bpos:
				rightbound = k
				break
			if k in wpos:
				rightbound = k-1
				break
		for l in range(coltop,position,-8):
			if l in bpos:
				topbound = l
				break
			if l in wpos:
				topbound = l-8
				break
		
		for a in range(leftbound,position,1):
			accum = accum + [a]
		for b in range(botbound,position,8):
			accum = accum +	[b]
		for c in range(rightbound,position,-1):
			accum = accum + [c]
		for d in range(topbound,position,-8):
			accum = accum + [d]

        if board[position] == 23: #black rook
                rowleft = position - position%8
                rowright = rowleft + 7
                colbot = position%8
                coltop = 56 + position%8

                #ONCE COMPUTED, BOUNDS ARE INCLUSIVE,THEREFORE VALID POSITIONS
                leftbound = rowleft
                rightbound = rowright
                topbound = coltop
                botbound = colbot

                for i in range (rowleft,position,1):
                        if i in wpos:
                                leftbound = i
                        if i in bpos:
                                leftbound = i+1
                for j in range (colbot,position,8):
                        if j in wpos:
                                botbound = j
                        if j in bpos:
                                botbound = j+8
                for k in range(rowright,position,-1):
                        if k in wpos:
                                rightbound = k
                                break
                        if k in bpos:
                                rightbound = k-1
                                break
                for l in range(coltop,position,-8):
                        if l in wpos:
                                topbound = l
                                break
                        if l in bpos:
                                topbound = l-8
                                break

                for a in range(leftbound,position,1):
                        accum = accum + [a]
                for b in range(botbound,position,8):
                        accum = accum + [b]
                for c in range(rightbound,position,-1):
                        accum = accum + [c]
                for d in range(topbound,position,-8):
                        accum = accum + [d]

		
	if board[position] == 12: #white bishop
		top = [i for i in range(56,64,1)]
		bottom  = [i for i in range(0,8,1)]
		left = [i for i in range(0,57,8)]
		right = [i for i in range(7,64,8)]
		topr = position
		topl = position
		botr = position
		botl = position

		# BOUNDS ARE INCLUSIVE
		# when accuming, ALWAYS GO FROM BOUND TO POSITION SO BOUND IS INCL BUT POSITION IS NOT - esp if they are =
		# if enemy present, valid, if own player present, one before, if reaches bound, break
		while True:
			if topr in top or topr in right:
				break
			topr = topr + 9
			
			if topr in wpos:
				topr = topr - 9
				break
			if topr in bpos:
				break
			
		while True:
                        if topl in top or topl in left:
                                break
                        topr = topr + 7

                        if topl in wpos:
                                topl = topl - 7
                                break
                        if topl in bpos:
                                break
		while True:
                        if botr in bottom or botr in right:
                                break
                        botr = botr - 7

                        if botr in wpos:
                                botr = botr + 7
                                break
                        if botr in bpos:
                                break
		while True:
                        if botl in bottom or botl in left:
                                break
                        topr = topr - 9

                        if botl in wpos:
                                botl = botl + 9
                                break
                        if botl in bpos:
                                break
		for i in range(botl,position,9):
			accum = accum + [i]
		for j in range(botr,position,7):
			accum = accum + [j]
		for k in range(topl,position,-7):
			accum = accum + [k]
		for l in range(topr,position,-9):
			accum = accum + [l]
	

	if board[position] == 22: #black bishop
		top = [i for i in range(56,64,1)]
		bottom  = [i for i in range(0,8,1)]
		left = [i for i in range(0,57,8)]
		right = [i for i in range(7,64,8)]
		topr = position
		topl = position
		botr = position
		botl = position

		# BOUNDS ARE INCLUSIVE
		# when accuming, ALWAYS GO FROM BOUND TO POSITION SO BOUND IS INCL BUT POSITION IS NOT - esp if they are =
		# if enemy present, valid, if own player present, one before, if reaches bound, break
		while True:
			if topr in top or topr in right:
				break
			topr = topr + 9
			
			if topr in wpos:			
				break
			if topr in bpos:
				topr = topr - 9
				break
			
		while True:
                        if topl in top or topl in left:
                                break
                        topr = topr + 7

                        if topl in wpos:                               
                                break
                        if topl in bpos:
				topl = topl - 7
                                break
		while True:
                        if botr in bottom or botr in right:
                                break
                        botr = botr - 7

                        if botr in wpos:
                                break
                        if botr in bpos:
				botr = botr + 7
                                break
		while True:
                        if botl in bottom or botl in left:
                                break
                        topr = topr - 9

                        if botl in wpos:
                                break
                        if botl in bpos:
				topr = topr + 9
                                break

		for i in range(botl,position,9):
			accum = accum + [i]
		for j in range(botr,position,7):
			accum = accum + [j]
		for k in range(topl,position,-7):
			accum = accum + [k]
		for l in range(topr,position,-9):
			accum = accum + [l]

	if board[position] == 14: #white queen		
		rowleft = position - position%8
		rowright = rowleft + 7
		colbot = position%8
		coltop = 56 + position%8
		
		#ONCE COMPUTED, BOUNDS ARE INCLUSIVE,THEREFORE VALID POSITIONS
		leftbound = rowleft
		rightbound = rowright
		topbound = coltop
		botbound = colbot

		for i in range (rowleft,position,1):
			if i in bpos:
				leftbound = i
			if i in wpos:
				leftbound = i+1
		for j in range (colbot,position,8):
			if j in bpos:
				botbound = j
			if j in wpos:
				botbound = j+8
		for k in range(rowright,position,-1):
			if k in bpos:
				rightbound = k
				break
			if k in wpos:
				rightbound = k-1
				break
		for l in range(coltop,position,-8):
			if l in bpos:
				topbound = l
				break
			if l in wpos:
				topbound = l-8
				break
		
		for a in range(leftbound,position,1):
			accum = accum + [a]
		for b in range(botbound,position,8):
			accum = accum +	[b]
		for c in range(rightbound,position,-1):
			accum = accum + [c]
		for d in range(topbound,position,-8):
			accum = accum + [d]

		#bishop moves
		top = [i for i in range(56,64,1)]
		bottom  = [i for i in range(0,8,1)]
		left = [i for i in range(0,57,8)]
		right = [i for i in range(7,64,8)]
		topr = position
		topl = position
		botr = position
		botl = position

		# BOUNDS ARE INCLUSIVE
		# when accuming, ALWAYS GO FROM BOUND TO POSITION SO BOUND IS INCL BUT POSITION IS NOT - esp if they are =
		# if enemy present, valid, if own player present, one before, if reaches bound, break
		while True:
			if topr in top or topr in right:
				break
			topr = topr + 9
			
			if topr in wpos:
				topr = topr - 9
				break
			if topr in bpos:
				break
			
		while True:
                        if topl in top or topl in left:
                                break
                        topr = topr + 7

                        if topl in wpos:
                                topl = topl - 7
                                break
                        if topl in bpos:
                                break
		while True:
                        if botr in bottom or botr in right:
                                break
                        botr = botr - 7

                        if botr in wpos:
                                botr = botr + 7
                                break
                        if botr in bpos:
                                break
		while True:
                        if botl in bottom or botl in left:
                                break
                        topr = topr - 9

                        if botl in wpos:
                                botl = botl + 9
                                break
                        if botl in bpos:
                                break
		for i in range(botl,position,9):
			accum = accum + [i]
		for j in range(botr,position,7):
			accum = accum + [j]
		for k in range(topl,position,-7):
			accum = accum + [k]
		for l in range(topr,position,-9):
			accum = accum + [l]

	if board[position] == 24: #black queen

                rowleft = position - position%8
                rowright = rowleft + 7
                colbot = position%8
                coltop = 56 + position%8

                #ONCE COMPUTED, BOUNDS ARE INCLUSIVE,THEREFORE VALID POSITIONS
                leftbound = rowleft
                rightbound = rowright
                topbound = coltop
                botbound = colbot

                for i in range (rowleft,position,1):
                        if i in wpos:
                                leftbound = i
                        if i in bpos:
                                leftbound = i+1
                for j in range (colbot,position,8):
                        if j in wpos:
                                botbound = j
                        if j in bpos:
                                botbound = j+8
                for k in range(rowright,position,-1):
                        if k in wpos:
                                rightbound = k
                                break
                        if k in bpos:
                                rightbound = k-1
                                break
                for l in range(coltop,position,-8):
                        if l in wpos:
                                topbound = l
                                break
                        if l in bpos:
                                topbound = l-8
                                break

                for a in range(leftbound,position,1):
                        accum = accum + [a]
                for b in range(botbound,position,8):
                        accum = accum + [b]
                for c in range(rightbound,position,-1):
                        accum = accum + [c]
                for d in range(topbound,position,-8):
                        accum = accum + [d]

		top = [i for i in range(56,64,1)]
		bottom  = [i for i in range(0,8,1)]
		left = [i for i in range(0,57,8)]
		right = [i for i in range(7,64,8)]
		topr = position
		topl = position
		botr = position
		botl = position

		# BOUNDS ARE INCLUSIVE
		# when accuming, ALWAYS GO FROM BOUND TO POSITION SO BOUND IS INCL BUT POSITION IS NOT - esp if they are =
		# if enemy present, valid, if own player present, one before, if reaches bound, break
		while True:
			if topr in top or topr in right:
				break
			topr = topr + 9
			
			if topr in wpos:			
				break
			if topr in bpos:
				topr = topr - 9
				break
			
		while True:
                        if topl in top or topl in left:
                                break
                        topr = topr + 7

                        if topl in wpos:                               
                                break
                        if topl in bpos:
				topl = topl - 7
                                break
		while True:
                        if botr in bottom or botr in right:
                                break
                        botr = botr - 7

                        if botr in wpos:
                                break
                        if botr in bpos:
				botr = botr + 7
                                break
		while True:
                        if botl in bottom or botl in left:
                                break
                        topr = topr - 9

                        if botl in wpos:
                                break
                        if botl in bpos:
				topr = topr + 9
                                break

		for i in range(botl,position,9):
			accum = accum + [i]
		for j in range(botr,position,7):
			accum = accum + [j]
		for k in range(topl,position,-7):
			accum = accum + [k]
		for l in range(topr,position,-9):
			accum = accum + [l]

	if board[position] == 11: # white knight
		boardnums = [a for a in range(0,64)]
		change = [6, 10, 15, 17, -6, -10, -15, -17]
		testpositions = map(lambda change:change+position,change)
		for i in testpositions:
			if i in boardnums:
				if i in bpos or board[i] == 0:
					accum = accum + [i]
	if board[position] == 21: # black knight
                boardnums = [a for a in range(0,64)]
                change = [6, 10, 15, 17, -6, -10, -15, -17]
                testpositions = map(lambda change:change+position,change)
                for i in testpositions:
                        if i in boardnums:
                                if i in wpos or board[i] == 0: # check if the spot is either empty or has opponent
                                        accum = accum + [i]
	if board[position] == 15: #white KING			
		boardnums = [a for a in range(0,64)]
		change = [-1,1,-8,8,-7,7,-9,9]
		testpositions = map(lambda change:change+position,change)
		for i in testpositions:
			testboard = list(board)
			if i in boardnums:
				testboard[position] = 0
				testboard[i] = 15
				if i in bpos or board[i] == 0:
					if isKingInCheck(testboard,10) == False:
						accum = accum + [i]
	if board[position] == 25: #Black KING
                boardnums = [a for a in range(0,64)]
                change = [-1,1,-8,8,-7,7,-9,9]
                testpositions = map(lambda change:change+position,change)
                for i in testpositions:
                        testboard = list(board)
                        if i in boardnums:
                                testboard[position] = 0
                                testboard[i] = 25
                                if i in bpos or board[i] == 0:
                                        if isKingInCheck(testboard,20) == False:
                                                accum = accum + [i]
	return accum

		
	
def IsPositionUnderThreat(board,position,player):

	if player == 10:
		opp = 20
	else if player == 20:
		opp = 10
	else:
		return -1
	opppieces = GetPlayerPositions(board,opp)
	for i in opppieces:
		moves = GetPieceLegalMoves(board,i)
		for j in moves:
			if j == position:
				return True

	return False 
			
