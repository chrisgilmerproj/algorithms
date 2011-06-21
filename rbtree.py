

class rbnode(object):

	def __init__(self, key):
		self._key   = key
		self._red   = False
		self._left  = None
		self._right = None
		self._p     = None
	
	key    = property(fget=lambda self: self._key  , doc="The node's key")
	red    = property(fget=lambda self: self._red  , doc="The node's color")
	left   = property(fget=lambda self: self._left , doc="The node's left child")
	right  = property(fget=lambda self: self._right, doc="The node's right child")
	p      = property(fget=lambda self: self._p    , doc="The node's parent")

	def __str__(self): return str(self.key)
	def __repr__(self): return str(self.key)

class rbtree(object):

	def __init__(self):
		self._nil  = rbnode(key=None)
		self._root = self._nil

	nil  = property(fget=lambda self: self._nil,  doc="The tree's nil node")
	root = property(fget=lambda self: self._root, doc="The tree's root node")

