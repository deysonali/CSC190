if board[i] == 12: #whitebi
	nr = pos%8
	nl = 7-pos%8
	accum=[]
	ul = pos
	ll = pos
	ur = pos
	lr = pos
	for i in range(0,nr,1):
		ur += 7
		lr -= 9
		if lr in range(0,64):
			if lr in wpos:
				break
			elif lr in bpos:
				accum+ = [lr]
				break
			else:
				accum+ = [lr]
		if ur in range(0,64):
			if ur in wpos:
                                break
                        elif ur in bpos:
                                accum+ = [ur]
                                break
                        else:
                                accum+ = [ur]


	for i in range(0,nl,1):
		ul += 9
		ll -= 7
		if ul in range(0,64):
			if ul in wpos:
                                break
                        elif ul in bpos:
                                accum+ = [ul]
                                break
                        else:
                                accum+ = [ul]
		if ll in range(0,64):
			if ll in wpos:
                                break
                        elif ll in bpos:
                                accum+ = [ll]
                                break
                        else:
                                accum+ = [ll]

			
