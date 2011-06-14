#!/usr/local/bin/python

def insertion_sort(A):
	for j in range(1,len(A)):
		key = A[j]
		i = j-1
		print key, j, i
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
