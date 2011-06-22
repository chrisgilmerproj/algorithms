

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

	def minimum(self, x=None):
		if None == x:
			x = self.root
		while x.left != self.nil:
			x = x.left
		return x
		
	def maximum(self, x=None):
		if None == x:
			x = self.root
		while x.right != self.nil:
			x = x.right
		return x

	def print_tree(self, x=None):
		if None == x:
			x = self.root
		tree_list = []
		self._print_tree(x,tree_list)
		for level in tree_list:
			print level

	def _print_tree(self, x, tree_list, level=0):
		if len(tree_list) > level+1:
			tree_list[level].append(x and x.key or None)
		else:
			tree_list.insert(level,[x])
		if x:
			self._print_tree(x.left,  tree_list, level=level+1)
			self._print_tree(x.right, tree_list, level=level+1)

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
	
	def delete_key(self, key):
		z = self.search(key)
		self.delete_node(z)

	def delete_node(self, z):
		y = z
		y.orig = y.red
		if z.left == self.nil:
			x = z.right
			self._transplant(z,z.right)
		elif z.right == self.nil:
			x = z.left
			self._transplant(z,z.left)
		else:
			y = self.minimum(x=z.right)
			y.orig = y.red
			x = y.right
			if y.p == z:
				x._p = y
			else:
				self._transplant(y,y.right)
				y._right = z.right
				y.right._p = y
			self._transplant(z,y)
			y._left = z.left
			y.left._p = y
			y._red = z.red
		if not y.orig:
			self._delete_fixup(x)

	def _insert_fixup(self,z):
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

	def _transplant(u,v):
		if u.p == self.nil:
			self._root = v
		elif u == u.p.left:
			u.p._left = v
		else:
			u.p._right = v
		v._p = u.p

	def _delete_fixup(x):
		while x != self.root and not x.red:
			if x == x.p.left:
				w = x.p.right
				if w.red:
					w._red = False
					x.p._red = True
					self._left_rotate(x.p)
					w = x.p.right
				if not w.left.red and not w.right.red:
					w._red = True
					x = x.p
				else:
					if not w.right.red:
						w.left._red = False
						w._red = True
						self._right_rotate(w)
						w = x.p.right
					w._red = x.p.red
					x.p._red = False
					w.right._red = False
					self._left_rotate(x.p)
					x = self.root
			else:
				w = x.p.left
				if w.red:
					w._red = False
					x.p._red = True
					self._right_rotate(x.p)
					w = x.p.left
				if not w.right.red and not w.left.red:
					w._red = True
					x = x.p
				else:
					if not w.left.red:
						w.right._red = False
						w._red = True
						self._left_rotate(w)
						w = x.p.left
					w._red = x.p.red
					x.p._red = False
					w.left._red = False
					self._right_rotate(x.p)
					x = self.root
		x._red = False

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

