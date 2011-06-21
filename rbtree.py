

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

	def search(self, key, x=None):
		if None == x:
			x = self.root
		while x != self.nil and key != x.key:
			if key < x.key:
				x = x.left
			else:
				x = x.right
		return x

	def minimum(self, key, x=None):
		if None == x:
			x = self.root
		while x.left != self.nil:
			x = x.left
		return x
		
	def maximum(self, key, x=None):
		if None == x:
			x = self.root
		while x.right != self.nil:
			x = x.right
		return x

	def insert_key(self, key):
		self.insert_node(rbnode(key=key))
	
	def insert_node(self, z):
		y = self.nil
		x = self.root
		while x != self.nil:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z._p = y
		if y == self.nil:
			self._root = z
		elif z.key < y.key:
			y._left = z
		else:
			y._right = z
		z._left = self.nil
		z._right = self.nil
		z._red = True
		self._insert_fixup(z)
	
	def _insert_fixup(z):
		while z.p.red:
			if z.p == z.p.p.left:
				y = z.p.p.right
				if y.red:
					z.p._red = False
					y._red = False
					z.p.p._red = True
					z = z.p.p
				else:
					if z == z.p.right:
						z = z.p
						self._left_rotate(z)
			else:
                y = z.p.p.left
                if y.red:
                    z.p._red = False
                    y._red = False
                    z.p.p._red = True
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self._right_rotate(z)
                    z.p._red = False
                    z.p.p._red = True
                    self._left_rotate(z.p.p)
        self.root._red = False

	def _left_rotate(self,x):
		y = x.right
		x._right = y.left
		if y.left != self.nil:
			y.left._p = x
		y._p = x.p
		if x.p == self.nil:
			self._root = y
		elif x == x.p.left:
			x.p._left = y
		else:
			x.p._right = y
		y._left = x
		x._p = y
	
	def _right_rotate(self,y):
		x = y.left
		y._left = x.right
		if x.right != self.nil:
			x.right._p = x
		x._p = y.p
		if y.p == self.nil:
			self._root = x
		elif y == y.p.right:
			y.p._right = x
		else:
			y.p._left = x
		x._right = y
		y._p = x
	
	
