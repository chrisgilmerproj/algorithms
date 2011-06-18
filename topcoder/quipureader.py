import re

def read_knots(knots):
	"""
	Problem Name: Quipu Reader
	Difficulty: Div I Mediume
	"""
	# Find the set of knot positions
	pos = []
	for knot in knots:
		for m in re.finditer(r'X{1,10}',knot):
			found = False
			for p in pos:
				if m.start() >= p[0] and m.start() < p[1] or \
				   m.end()   > p[0] and m.end()   <= p[1]:
					if m.start() < p[0]: p[0] = m.start()
					if m.end()   > p[1]: p[1] = m.end()
					found = True
				elif p[0] > m.start() and p[1] < m.end():
					p[0] = m.start()
					p[1] = m.end()
					found = True
			if not found: 
				pos.append([m.start(),m.end()])
	pos.sort()

	# Find the number of knots for each set of positions
	num_list = [[knot.count('X',p[0],p[1]) for p in pos] for knot in knots]

	# Return the summed numbers
	return [sum(n[i]*pow(10,len(n)-1-i) for i in xrange(0,len(n))) for n in num_list]

def test_read_knots():
	assert read_knots([
		"-XXXXXXX--XX-----XXXXX---",
		"---XX----XXX-----XXXX----",
		"-XXXXX---XXXXX--XXXXXXXX-"]) == [725,  234,  558]

	assert read_knots([
		"XX---XXXX",
		"XXX-----X"]) == [24,  31]
	
	assert read_knots([
		"-XXX---XX----X",
		"--X----X-XXXXX",
		"-XX--XXXX---XX"]) == [321,  115,  242]
	
	assert read_knots([
		"-------X--------",
		"--XXX----XXXX---",
		"--------------XX"]) == [100,  3040,  2]

	assert read_knots([
		"--XXX-XXXXXXXX----------XXXXXXXXX--XXXXXXXX-",
		"--XX----XXXX-----XXXXXX---XXX------XXXXXXXX-",
		"--------------------X----XXXXXXXX--XXXXXXXX-",
		"--XX-------X------XXXX----XXX-------XXXXXX--",
		"--XXX---XXXXX-------X------XX--------X------",
		"-XXXX--XXXXXXX-----------XXXXXXX----XXXXX---",
		"-----------X---XXXXXXXX----XX--------XXX----",
		"-----------X---XXXXXXXX----X----------------",
		"---X--XXXXXXXX--XXXXXXX---XXX---------------",
		"--XX---XXXXXXX--XXXXXXX----XX-------XXXXX---"]) == [38098,  24638,  188,  21436,  35121,  47075,  1823,  1810,  18730,  27725]
	
	assert read_knots(["X","-"]) == [1,0]

