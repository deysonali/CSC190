def genboard():
	row0 = [13,11,12,15,14,12,11,13]
	row1 = [10 for i in range(0,7)]
	rowmiddle = [0 for i in range(0,32)]
	row6 = [20 for i in range(0,7)]
	row7 = [23,21,22,25,24,22,21,23]
	newboard= row0+row1+rowmiddle+row6+row7
	return newboard

def GetPlayerPositions(board,player):
	if (player!=10 and player!=20):
		return False
	if (len(board)!= 64):
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

	# check b or w
	if board[position]-20 >=0 and board[position]-20 <=5:
		#print "hi"
		opponent = 10
		for i in range(0,64):	
			if board[i] == 25:
			
				kingposition = i
				
	if board[position]-10 >=0 and board[position]-10 <=5:
                #print "Hi"
		opponent = 20
		for i in range(0,64):
			#print i
                        if board[i] == 15:
				#rint "got here"
                        	kingposition = i
        	                
	
	opponentloc = GetPlayerPositions(board,opponent)
	
	# if legalmoves of any opp players == king pos
	for i in opponentloc:
		opplegal = GetMoves(board,i)
		for j in opplegal:
			if j == kingposition:
				return True
	# return TRUE (means you have no legal moves for player)  
	return False

def isKingInCheck(board,player): # for LEGAL MOVES: make sure if K in check, legal moves are ones that bring King OUT of check
	#print board
	flag = False
	if player == 10:
	#	print "Hello"
		opponent = 20
		for i in range(0,64):
			if board[i] == 15:
				kingposition = i
				flag = True
	if player == 20:
	#	print "20 Hi"
		opponent = 10
                for i in range(0,64):
                        if board[i] == 25:
                                kingposition = i
				flag = True	
	opponentloc = GetPlayerPositions(board,opponent)
	if flag == False:
		return False
        # if legalmoves of any opp players == king pos
        for i in opponentloc:
                opplegal = GetMoves(board,i)
                for j in opplegal:
			
                        if j == kingposition:
                                return True
				break
      
	return False
				

	
def GetPieceLegalMoves(board,position):
	moves = GetMoves(board,position)
	if board[position] - 20 >= 0 and board[position] - 20 <=5:
		player = 20
	if board[position] - 10 >= 0 and board[position] - 10 <=5:
		player = 10	
	accum = []
	if MovePieceCausesCheck(board,position)==True:
		return []
	else:

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
	

	wpos = GetPlayerPositions(board,10)
	bpos = GetPlayerPositions(board,20)
	accum = []
	if board[position] == 10: #white pawn

		if position+8 <=63:
			if board[position+8] == 0:
				accum = accum + [position+8]
		if position%8 == 7:  #checking if it is a left border case, so one diagonal is invalid
			if position+7 <=63:
				if (board[position+7]-20) <= 5 and (board[position+7]-20) >= 0:
					accum = accum + [position + 7]
		elif position%8 == 0:  #checking if it is a right border case, so one diagonal is invalid
                        if position+9 <=63:
                                if (board[position+9]-20) <= 5 and (board[position+9]-20) >= 0:
                                        accum = accum + [position + 9]
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
                if position%8 == 7:  #checking if it is a left border case, so one diagonal is invalid
                        if position-9 >=0:
                                if (board[position-9]-10) <= 5 and (board[position-9]-10) >= 0:
                                        accum = accum + [position -9]
                elif position%8 == 0:  #checking if it is a right border case, so one diagonal is invalid
                        if position-7 >=0:
                                if (board[position-7]-10) <= 5 and (board[position-7]-10) >= 0:
                                        accum = accum + [position -7]
                else:
                        if position-7 >=0:
                                if (board[position-7]-10) <= 5 and (board[position-7]-10) >= 0:
                                        accum = accum + [position - 7]
                        if position-9 >=0:
                                if (board[position-9]-10) <= 5 and (board[position-9]-10) >= 0:
                                        accum = accum + [position - 9]
	if board[position] == 13: #white rook
		rowright = position - position%8
		rowleft = rowright + 7
		colbot = position%8
		coltop = 56 + position%8
		
		#ONCE COMPUTED, BOUNDS ARE INCLUSIVE,THEREFORE VALID POSITIONS
		leftbound = rowleft
		rightbound = rowright
		topbound = coltop
		botbound = colbot

		for i in range (rowleft,position,-1):
			if i in bpos:
				leftbound = i
			if i in wpos:
				leftbound = i-1
		for j in range (colbot,position,8):
			if j in bpos:
				botbound = j
			if j in wpos:
				botbound = j+8
		for k in range(rowright,position,1):
			if k in bpos:
				rightbound = k
				
			if k in wpos:
				rightbound = k+1
				
		for l in range(coltop,position,-8):
			if l in bpos:
				topbound = l
				
			if l in wpos:
				topbound = l-8
				
		
		for a in range(rightbound,position,1):
			accum = accum + [a]
		for b in range(botbound,position,8):
			accum = accum +	[b]
		for c in range(leftbound,position,-1):
			accum = accum + [c]
		for d in range(topbound,position,-8):
			accum = accum + [d]

        if board[position] == 23: #black rook
                rowright = position - position%8
                rowleft = rowright + 7
                colbot = position%8
                coltop = 56 + position%8

                #ONCE COMPUTED, BOUNDS ARE INCLUSIVE,THEREFORE VALID POSITIONS
                leftbound = rowleft
                rightbound = rowright
                topbound = coltop
                botbound = colbot

                for i in range (rowleft,position,-1):
                        if i in wpos:
                                leftbound = i
                        if i in bpos:
                                leftbound = i-1
                for j in range (colbot,position,8):
                        if j in wpos:
                                botbound = j
                        if j in bpos:
                                botbound = j+8
                for k in range(rowright,position,1):
                        if k in wpos:
                                rightbound = k
                                
                        if k in bpos:
                                rightbound = k+1
                                
                for l in range(coltop,position,-8):
                        if l in wpos:
                                topbound = l
                                
                        if l in bpos:
                                topbound = l-8


                for a in range(leftbound,position,-1):
                        accum = accum + [a]
                for b in range(botbound,position,8):
                        accum = accum + [b]
                for c in range(rightbound,position,1):
                        accum = accum + [c]
                for d in range(topbound,position,-8):
                        accum = accum + [d]

	if board[position] == 12: #whitebi
		pos = position
		nr = pos%8
		nl = 7-pos%8
		accum=[]
		ul = pos
		ll = pos
		ur = pos
		lr = pos
		for i in range(0,nr,1):
			lr -= 9
			if lr in range(0,64):
				if lr in wpos:
					break
				elif lr in bpos:
					accum += [lr]
					break
				else:
					accum += [lr]
		for i in range(0,nr,1):
			ur +=7
			if ur in range(0,64):
				if ur in wpos:
					break
				elif ur in bpos:
					accum += [ur]
					break
				else:
					accum += [ur]


		for i in range(0,nl,1):
			ul += 9
			if ul in range(0,64):
				if ul in wpos:
					break
				elif ul in bpos:
					accum += [ul]
					break
				else:
					accum += [ul]
		for i in range(0,nl,1):
			ll -= 7
			if ll in range(0,64):
				if ll in wpos:
					break
				elif ll in bpos:
					accum += [ll]
					break
				else:
					accum += [ll]
	

	if board[position] == 22: #blackbi
		pos = position
		nr = pos%8
		nl = 7-pos%8
		accum=[]
		ul = pos
		ll = pos
		ur = pos
		lr = pos
		for i in range(0,nr,1):
			lr -= 9
			if lr in range(0,64):
				if lr in bpos:
					break
				elif lr in wpos:
					accum += [lr]
					break
				else:
					accum += [lr]
		for i in range(0,nr,1):
			ur +=7
			if ur in range(0,64):
				if ur in bpos:
					break
				elif ur in wpos:
					accum += [ur]
					break
				else:
					accum += [ur]


		for i in range(0,nl,1):
			ul += 9
			if ul in range(0,64):
				if ul in bpos:
					break
				elif ul in wpos:
					accum += [ul]
					break
				else:
					accum += [ul]
		for i in range(0,nl,1):
			ll -= 7
			if ll in range(0,64):
				if ll in bpos:
					break
				elif ll in wpos:
					accum += [ll]
					break
				else:
					accum += [ll]

	if board[position] == 14: #white queen		
		

                rowright = position - position%8
                rowleft = rowright + 7
                colbot = position%8
                coltop = 56 + position%8

                #ONCE COMPUTED, BOUNDS ARE INCLUSIVE,THEREFORE VALID POSITIONS
                leftbound = rowleft
                rightbound = rowright
                topbound = coltop
                botbound = colbot

                for i in range (rowleft,position,-1):
                        if i in wpos:
                                leftbound = i
                        if i in bpos:
                                leftbound = i-1
                for j in range (colbot,position,8):
                        if j in wpos:
                                botbound = j
                        if j in bpos:
                                botbound = j+8
                for k in range(rowright,position,1):
                        if k in wpos:
                                rightbound = k
                                
                        if k in bpos:
                                rightbound = k+1
                               
                for l in range(coltop,position,-8):
                        if l in wpos:
                                topbound = l
                                
                        if l in bpos:
                                topbound = l-8
                                

                for a in range(leftbound,position,-1):
                        accum = accum + [a]
                for b in range(botbound,position,8):
                        accum = accum + [b]
                for c in range(rightbound,position,1):
                        accum = accum + [c]
                for d in range(topbound,position,-8):
                        accum = accum + [d]

		
	

		pos = position
		nr = pos%8
		nl = 7-pos%8
		accum=[]
		ul = pos
		ll = pos
		ur = pos
		lr = pos
		for i in range(0,nr,1):
			lr -= 9
			if lr in range(0,64):
				if lr in wpos:
					break
				elif lr in bpos:
					accum += [lr]
					break
				else:
					accum += [lr]
		for i in range(0,nr,1):
			ur +=7
			if ur in range(0,64):
				if ur in wpos:
					break
				elif ur in bpos:
					accum += [ur]
					break
				else:
					accum += [ur]


		for i in range(0,nl,1):
			ul += 9
			if ul in range(0,64):
				if ul in wpos:
					break
				elif ul in bpos:
					accum += [ul]
					break
				else:
					accum += [ul]
		for i in range(0,nl,1):
			ll -= 7
			if ll in range(0,64):
				if ll in wpos:
					break
				elif ll in bpos:
					accum += [ll]
					break
				else:
					accum += [ll]

	
	if board[position] == 24: #black queen

                rowright = position - position%8
                rowleft = rowright + 7
                colbot = position%8
                coltop = 56 + position%8

                #ONCE COMPUTED, BOUNDS ARE INCLUSIVE,THEREFORE VALID POSITIONS
                leftbound = rowleft
                rightbound = rowright
                topbound = coltop
                botbound = colbot

                for i in range (rowleft,position,-1):
                        if i in wpos:
                                leftbound = i
                        if i in bpos:
                                leftbound = i-1
                for j in range (colbot,position,8):
                        if j in wpos:
                                botbound = j
                        if j in bpos:
                                botbound = j+8
                for k in range(rowright,position,1):
                        if k in wpos:
                                rightbound = k
                                break
                        if k in bpos:
                                rightbound = k+1
                                break
                for l in range(coltop,position,-8):
                        if l in wpos:
                                topbound = l
                                break
                        if l in bpos:
                                topbound = l-8
                                break

                for a in range(leftbound,position,-1):
                        accum = accum + [a]
                for b in range(botbound,position,8):
                        accum = accum + [b]
                for c in range(rightbound,position,1):
                        accum = accum + [c]
                for d in range(topbound,position,-8):
                        accum = accum + [d]

		pos = position
		nr = pos%8
		nl = 7-pos%8
		accum=[]
		ul = pos
		ll = pos
		ur = pos
		lr = pos
		for i in range(0,nr,1):
			lr -= 9
			if lr in range(0,64):
				if lr in bpos:
					break
				elif lr in wpos:
					accum += [lr]
					break
				else:
					accum += [lr]
		for i in range(0,nr,1):
			ur +=7
			if ur in range(0,64):
				if ur in bpos:
					break
				elif ur in wpos:
					accum += [ur]
					break
				else:
					accum += [ur]


		for i in range(0,nl,1):
			ul += 9
			if ul in range(0,64):
				if ul in bpos:
					break
				elif ul in wpos:
					accum += [ul]
					break
				else:
					accum += [ul]
		for i in range(0,nl,1):
			ll -= 7
			if ll in range(0,64):
				if ll in bpos:
					break
				elif ll in wpos:
					accum += [ll]
					break
				else:
					accum += [ll]


	if board[position] == 11: # white knight
		boardnums = [a for a in range(0,64)]
		mid = [i for i in range(18,22)]+[j for j in range(26,30)]+[k for k in range(34,38)] +[l for l in range(42,46)]
		t1 = [i for i in range(50,54)] 
		t2 =[ j for j in range(57,61)]
		b1 = [i for i in range(2,6)]
		b2 = [ j for j in range(10,14)]
		l1 = [i for i in range(23,55,8)] 
		l2 =[j for j in range(22,54,8)]
		r1 = [i for i in range(16,48,8)] 
		r2 = [j for j in range(17,49,8)]
	
		
		if position in mid:
			change = [6, 10, 15, 17, -6, -10, -15, -17]
		elif position in t1:
			change = [6, 10, -6, -10, -15, -17]
		elif position in t2:
			change = [-6, -10, -15, -17]
		elif position in b1:
			change = [6, 10, 15, 17]
		elif position in b2:
			change = [6, 10, 15, 17,-6,-10]
		elif position in l1:
			change = [6, 15, -10, -17]
		elif position in l2:
			change = [6, -10, 15, 17, -15, -17]
		elif position in r2:
			change = [10, 15, 17, -6, -15, -17]
		elif position in r1:
			change = [10, 17, -6, -15]
		elif position == 0:
			change = [17,10]
		elif position == 1:
			change = [17,10,15]
		elif position == 8:
			change = [10,17,-6]
		elif position == 9:
			change = [10,17,15,-6]
		elif position == 6:
			change = [6,15,17]
		elif position == 7:
			change = [6,15]
		elif position == 14:
			change = [15,6,17,-10]
		elif position == 15:
			change = [15,6,-10]
		elif position == 48:
			change = [-6,-15,10]
		elif position == 49:
			change = [-6,-15,-17,10]
		elif position == 56:
			change = [-6,-15]
		elif position == 57:
			change = [-6,-15,-17]
		elif position == 54:
			change = [6,-10,-15,-17]
		elif position == 55:
			change = [6,-10,-17]
		elif position == 62:
			change = [-10,-17,-15]
		elif position == 63:
			change = [-10,-17]




		
		testpositions = map(lambda change:change+position,change)
		for i in testpositions:
			if i in boardnums:
				if i in bpos or board[i] == 0:
					accum = accum + [i]
	if board[position] == 21: # black knight
                boardnums = [a for a in range(0,64)]


		mid = [i for i in range(18,22)]+[j for j in range(26,30)]+[k for k in range(34,38)] +[l for l in range(42,46)]
		t1 = [i for i in range(50,54)] 
		t2 =[ j for j in range(57,61)]
		b1 = [i for i in range(2,6)]
		b2 = [ j for j in range(10,14)]
		l1 = [i for i in range(23,55,8)] 
		l2 =[j for j in range(22,54,8)]
		r1 = [i for i in range(16,48,8)] 
		r2 = [j for j in range(17,49,8)]
	
		
		if position in mid:
			change = [6, 10, 15, 17, -6, -10, -15, -17]
		elif position in t1:
			change = [6, 10, -6, -10, -15, -17]
		elif position in t2:
			change = [-6, -10, -15, -17]
		elif position in b1:
			change = [6, 10, 15, 17]
		elif position in b2:
			change = [6, 10, 15, 17,-6,-10]
		elif position in l1:
			change = [6, 15, -10, -17]
		elif position in l2:
			change = [6, -10, 15, 17, -15, -17]
		elif position in r2:
			change = [10, 15, 17, -6, -15, -17]
		elif position in r1:
			change = [10, 17, -6, -15]
		elif position == 0:
			change = [17,10]
		elif position == 1:
			change = [17,10,15]
		elif position == 8:
			change = [10,17,-6]
		elif position == 9:
			change = [10,17,15,-6]
		elif position == 6:
			change = [6,15,17]
		elif position == 7:
			change = [6,15]
		elif position == 14:
			change = [15,6,17,-10]
		elif position == 15:
			change = [15,6,-10]
		elif position == 48:
			change = [-6,-15,10]
		elif position == 49:
			change = [-6,-15,-17,10]
		elif position == 56:
			change = [-6,-15]
		elif position == 57:
			change = [-6,-15,-17]
		elif position == 54:
			change = [6,-10,-15,-17]
		elif position == 55:
			change = [6,-10,-17]
		elif position == 62:
			change = [-10,-17,-15]
		elif position == 63:
			change = [-10,-17]
                testpositions = map(lambda change:change+position,change)
                for i in testpositions:
                        if i in boardnums:
                                if i in wpos or board[i] == 0: # check if the spot is either empty or has opponent
                                        accum = accum + [i]
	if board[position] == 15: #white KING
		top = [i for i in range(56,64)]
		bot = [i for i in range(0,8)]
		l = [i for i in range(7,64,8)]
		r = [i for i in range(0,57,8)]

		if position == 7:
			change = [-1,7,8]
		elif position == 0:
			change = [8,9,1]
		elif position == 56:
			change = [1,-8,-7]
		elif position == 63:
			change = [-1,-8,-9]

		elif position in top:
			change = [1,-1,-9,-7]
		elif position in bot:
			change = [1,-1,9,7]
		elif position in l:
			change = [-1,8,-8,7,-7]
		elif position in r:
			change = [1,8,-8,9,-9]
		else:
			change = [-1,1,-8,8,-7,7,-9,9]
			
		boardnums = [a for a in range(0,64)]

		testpositions = map(lambda change:change+position,change)
		for i in testpositions:
			if i in boardnums:
				if i in bpos or board[i] == 0:
					accum = accum + [i]
	if board[position] == 25: #Black KING
                
		top = [i for i in range(56,64)]
		bot = [i for i in range(0,8)]
		l = [i for i in range(7,64,8)]
		r = [i for i in range(0,57,8)]

		if position == 7:
			change = [-1,7,8]
		elif position == 0:
			change = [8,9,1]
		elif position == 56:
			change = [1,-8,-7]
		elif position == 63:
			change = [-1,-8,-9]

		elif position in top:
			change = [1,-1,-9,-7]
		elif position in bot:
			change = [1,-1,9,7]
		elif position in l:
			change = [-1,8,-8,7,-7]
		elif position in r:
			change = [1,8,-8,9,-9]
		else:
			change = [-1,1,-8,8,-7,7,-9,9]
		boardnums = [a for a in range(0,64)]
                testpositions = map(lambda change:change+position,change)
		accum = list(testpositions)
		for i in testpositions:
                        if i in boardnums:
				if i in wpos or board[i] == 0:
                            	   	accum = accum +[i]

              #  for i in testpositions:
               #         testboard = list(board)
                #        if i in boardnums:
                 #               testboard[position] = 0
                  #              testboard[i] = 25
                   #             if i in bpos or board[i] == 0:
                   #                     if isKingInCheck(testboard,20) == False:
                    #                            accum = accum + [i]
	return accum

		
	
def IsPositionUnderThreat(board,position,player):

	if player == 10:
		opp = 20
	elif player == 20:
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
			
