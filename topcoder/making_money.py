
def money_made(amounts, cents_per_dollar, final_result):
	"""
	Problem Name: Betting Money
	Difficulty: Div II Easy
	"""
	loss = amounts.pop(final_result)*cents_per_dollar.pop(final_result)
	gain = sum(amounts)*100
	return gain - loss

def test_money_made():
	assert money_made([10,20,30],[20,30,40],1) == 3400
	assert money_made([200,300,100],[10,10,10],2) == 49000
	assert money_made([100,100,100,100],[5,5,5,5],0) == 29500
	assert money_made([5000,5000],[100,2],0) == 0
	assert money_made([100],[10],0) == -1000

