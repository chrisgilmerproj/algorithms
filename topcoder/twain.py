import re

spelling = {
	1 : [
		{'pattern': r'\sx', 'repl': ' z'},
		{'pattern': r'x', 'repl': 'ks'},
	],
	2 : [
		{'pattern': r'y', 'repl': 'i'},
	],
	3 : [
		{'pattern': r'ce', 'repl': 'se'},
		{'pattern': r'ci', 'repl': 'si'},
	],
	4 : [
		{'pattern': r'c+k', 'repl': 'k'},
	],
	5 : [
		{'pattern': r'\ssch', 'repl': ' sk'},
		{'pattern': r'chr', 'repl': 'kr'},
		{'pattern': r'c', 'repl': 'k'},
		{'pattern': r'kh', 'repl': 'ch'},
	],
	6 : [
		{'pattern': r'\skn', 'repl': ' n'},
	],
	7 : [
		{'pattern': r'', 'repl': ''},
	],
}
def new_spelling(year,phrase):
	
	for i in range(1,8):
		if i <= year:
			for j in spelling[i]:
				p = j['pattern']
				r = j['repl']
				phrase = re.sub(p,r,phrase)
	return phrase

def test_new_spelling():
	assert new_spelling(1,'i fixed the chrome xerox by the cyclical church') == "i fiksed the chrome zeroks by the cyclical church"

	assert new_spelling(2,"i fixed the chrome xerox by the cyclical church") == "i fiksed the chrome zeroks bi the ciclical church"

	assert new_spelling(0,"this is unchanged") == "this is unchanged"

	assert new_spelling(7,"sch kn x xschrx cknnchc cyck xxceci") == "sk n z zskrks nchk sik zksesi"

	assert new_spelling(7,"  concoction   convalescence   cyclical   cello   "
	Returns: "  konkoktion   konvalesense   siklikal   selo   "
	Beware of extra spaces.
	5)	
	    	
			7
			""
			Returns: ""
			Don't forget the empty case.
			6)	
			    	
					7
					"cck xzz aaaaa"
					Returns: "k z aaaaa"

