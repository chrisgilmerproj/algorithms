#!/usr/local/bin/python

import time

def print_timing(func):
	""" A decorator to determine how long an algorithm takes to complete """
	def wrapper(*arg,**kwargs):
		t1 = time.clock()
		res = func(*arg,**kwargs)
		t2 = time.clock()
		print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
		return res
	return wrapper

@print_timing
def insertion_sort(A):
	"""
	Best:	 n
	Average: n^2
	Worst:   n^2
	"""
	for j in range(1,len(A)):
		key = A[j]
		i = j-1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A



try:
	from IPython.Shell import IPShellEmbed
	IPShellEmbed()(local_ns=locals())
except:
	import code
	code.interact()
