
def max_points(toss):
	"""
	Problem Name: Yahtzee
	Difficulty: Div II Easy
	"""
	max = 0
	for i in range(1,7):
		s = sum(filter(lambda x: x == i,toss))
		if s > max: max = s
	return max

def test_max_points():
	assert max_points([2, 2, 3, 5, 4]) == 5 
	assert max_points([6, 4, 1, 1, 3]) == 6 
	assert max_points([5, 3, 5, 3, 3]) == 10 
