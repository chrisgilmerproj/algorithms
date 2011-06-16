import operator

def match_make(names_women, answers_women, names_men, answers_men, query_woman):
	"""
	Problem Name: Match Making
	Difficulty: Div I Easy
	"""
	# Put these in lexographical order
	combined = zip(names_women, answers_women)
	combined.sort()
	names_women, answers_women = zip(*combined)

	matches = {}
	for x, w_answer in enumerate(answers_women):
		best = 0
		b_list = []
		for y, m_answer in enumerate(answers_men):
			correct = map(operator.eq,w_answer,m_answer).count(True)
			if correct > best:
				best = correct
				b_list = [(names_men[y],y)]
			elif correct == best:
				b_list.append((names_men[y],y))
		b_list.sort()

		# Remove men from lists
		names_men.pop(b_list[0][1])
		answers_men.pop(b_list[0][1])

		# Set the match
		matches[names_women[x]] = b_list[0][0]
	return matches[query_woman]

def test_match_make():
	assert match_make(["Constance", "Bertha", "Alice"],
			["aaba", "baab", "aaaa"],
			["Chip", "Biff", "Abe"],
			["bbaa", "baaa", "aaab"],
			"Bertha") == "Biff"

	assert match_make(["Constance", "Bertha", "Alice"],
			["aaba", "baab", "aaaa"],
			["Chip", "Biff", "Abe"],
			["bbaa", "baaa", "aaab"],
			"Constance") == "Chip"

	assert match_make(["Constance", "Alice", "Bertha", "Delilah", "Emily"],
			["baabaa", "ababab", "aaabbb", "bababa", "baabba"],
			["Ed", "Duff", "Chip", "Abe", "Biff"],
			["aabaab", "babbab", "bbbaaa", "abbbba", "abaaba"],
			"Constance") == "Duff"

	assert match_make(["Constance", "Alice", "Bertha", "Delilah", "Emily"],
			["baabaa", "ababab", "aaabbb", "bababa", "baabba"],
			["Ed", "Duff", "Chip", "Abe", "Biff"],
			["aabaab", "babbab", "bbbaaa", "abbbba", "abaaba"],
			"Delilah") == "Chip"

	assert match_make(["Constance", "Alice", "Bertha", "Delilah", "Emily"],
			["baabaa", "ababab", "aaabbb", "bababa", "baabba"],
			["Ed", "Duff", "Chip", "Abe", "Biff"],
			["aabaab", "babbab", "bbbaaa", "abbbba", "abaaba"],
			"Emily") == "Ed"

	assert match_make(["anne", "Zoe"],
		["a", "a"],
		["bob", "chuck"],
		["a", "a"],
		"Zoe") == "bob"

	assert match_make(["F", "M", "S", "h", "q", "g", "r", "N", "U", "x", "H", "P",
			 "o", "E", "R", "z", "L", "m", "e", "u", "K", "A", "w", "Q",
			 "O", "v", "j", "a", "t", "p", "C", "G", "k", "c", "V", "B",
			 "D", "s", "n", "i", "f", "T", "I", "l", "d", "J", "y", "b"],
			["abaabbbb", "bbaabbbb", "aaabaaab", "aabbaaaa", "baabbaab",
			 "aaababba", "bbabbbbb", "bbbabbba", "aaabbbba", "aabbbaaa",
			 "abbabaaa", "babbabbb", "aaaaabba", "aaaabbaa", "abbbabaa",
			 "babababa", "abbaaaaa", "bbababba", "baaaaaba", "baaaaabb",
			 "bbbbabba", "ababbaaa", "abbbabab", "baabbbaa", "bbbaabbb",
			 "aababbab", "ababbabb", "abbaabba", "baabbabb", "aaabaaab",
			 "aabbbaba", "aabaaabb", "abababba", "aabbaaaa", "aabbabaa",
			 "bababaaa", "aabaaaab", "bbbbaabb", "baaababb", "abaabbab",
			 "aabbbaaa", "baabbaba", "bbabbbaa", "aabbbbaa", "abbbaaab",
			 "abababbb", "ababaaba", "bababaaa"],
			["f", "C", "v", "g", "Q", "z", "n", "c", "B", "o", "M", "F",
			 "u", "x", "I", "T", "K", "L", "E", "U", "w", "A", "d", "t",
			 "e", "R", "D", "s", "p", "q", "m", "r", "H", "j", "J", "V",
			 "l", "a", "k", "h", "G", "y", "i", "P", "O", "N", "b", "S"],
			["bbbaabab", "bbabaabb", "ababbbbb", "bbbababb", "baababaa",
			 "bbaaabab", "abbabbaa", "bbbabbbb", "aabbabab", "abbababa",
			 "aababbbb", "bababaab", "aaababbb", "baabbaba", "abaaaaab",
			 "bbaababa", "babaabab", "abbabbba", "ababbbab", "baabbbab",
			 "babbaaab", "abbbbaba", "bbabbbba", "baaabaab", "ababbabb",
			 "abbbaabb", "bbbbaabb", "bbbaaabb", "baabbaba", "bbabaaab",
			 "aabbbaab", "abbbbabb", "bbaaaaba", "bbbababa", "abbaabba",
			 "bababbbb", "aabaaabb", "babbabab", "baaaabaa", "ababbaba",
			 "aaabaabb", "bbaaabaa", "baaaaabb", "bbaabaab", "bbababab",
			 "aabaaaab", "aaaaabab", "aabbaaba"],
			"U") == "x"

	assert match_make(["q", "M", "w", "y", "p", "N", "s", "r", "a", "H", "o", "n",
			 "F", "m", "l", "b", "D", "j", "C", "u", "f", "I", "g", "L",
			 "i", "x", "A", "G", "O", "k", "h", "d", "c", "E", "B", "v",
			 "J", "z", "K", "e", "t"],
			["aabbaaabb", "baabababb", "bbaababba", "bbbaaaaaa", "abaaaabaa",
			 "bababbbab", "abbaabbaa", "aabababbb", "bababaaaa", "abbababaa",
			 "aabbbbbba", "bbabbabab", "babaabbba", "babbabbbb", "baaabbbbb",
			 "baaabaaaa", "aaabbaaab", "abbaabbbb", "abbabbbab", "bbaaaabba",
			 "babbaaabb", "aabbabbab", "baaababba", "ababaabab", "bbbaabbab",
			 "aaaabbabb", "babaaaaaa", "abbbbaaab", "aabaaabba", "bbbaaaaba",
			 "bbbbbbaab", "aabbaaabb", "aabaabbab", "aababaaba", "bbabbbbab",
			 "abbabaaab", "babaaabbb", "bababbaaa", "aabbaabaa", "baaabbabb",
			 "bbbbbbbbb"],
			["m", "k", "n", "q", "L", "E", "M", "l", "w", "x", "g", "e",
			 "i", "z", "F", "r", "a", "h", "f", "D", "J", "K", "j", "v",
			 "A", "t", "N", "y", "s", "c", "o", "p", "d", "b", "B", "G",
			 "O", "I", "u", "C", "H"],
			["bbaaabbba", "bbaaaaaab", "abaaababb", "baaaabbbb", "abbbababa",
			 "baaaaaaaa", "aabbbbbab", "aaaaabbba", "baabababb", "babaaabab",
			 "baaababaa", "bbbbaabba", "bbaabbabb", "bbaaababb", "abbabbaba",
			 "aababaaab", "abbbbbbaa", "aabbaabaa", "bbbaabbba", "abbabbaba",
			 "aaabbbaaa", "bbaabaaaa", "aabababbb", "abbbbabab", "baaabbbba",
			 "bababbbba", "aababbaab", "bbaabbaab", "bbbaaabbb", "babbbbabb",
			 "ababababb", "babaaabab", "bbaaaaaba", "aaaaabaaa", "abbaaabbb",
			 "bbbbababb", "baabababb", "bbaabaaaa", "aaababbbb", "abbbbbbba",
			 "bbaabbaaa"],
			"o") == "C"

