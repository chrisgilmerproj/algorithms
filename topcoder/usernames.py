
def new_member(existing_names,new_name):
	"""
	Problem Name: User Name
	Difficulty: Div II Easy
	"""
	n_list = filter(lambda name: new_name in name, existing_names)
	if not n_list or new_name not in n_list:
		return new_name
	for n in range(1,51):
		name = new_name + str(n)
		if name not in n_list:
			return name

def test_new_member():
	assert new_member(
		["MasterOfDisaster", "DingBat", "Orpheus", "WolfMan", "MrKnowItAll"],
		"TygerTyger") == "TygerTyger"
	
	assert new_member(
		["MasterOfDisaster", "TygerTyger1", "DingBat", "Orpheus", 
		 "TygerTyger", "WolfMan", "MrKnowItAll"],
		 "TygerTyger") == "TygerTyger2"

	assert new_member(
		["TygerTyger2000", "TygerTyger1", "MasterDisaster", "DingBat", 
		 "Orpheus", "WolfMan", "MrKnowItAll"],
		"TygerTyger") == "TygerTyger"
 
	assert new_member(
		["grokster2", "BrownEyedBoy", "Yoop", "BlueEyedGirl", 
		 "grokster", "Elemental", "NightShade", "Grokster1"],
		"grokster") == "grokster1"
    	
	assert new_member(
		["Bart4", "Bart5", "Bart6", "Bart7", "Bart8", "Bart9", "Bart10",
		 "Lisa", "Marge", "Homer", "Bart", "Bart1", "Bart2", "Bart3",
		 "Bart11", "Bart12"],
		"Bart") == "Bart13"
