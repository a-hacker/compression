"""
An AVL Tree implementation in Python.
A node's value must be a numeric.
This tree is meant to only add nodes with strictly increasing values.
"""

from math import fabs

class EmptyTreeException(ValueError):
	pass

class AVLNode():
	"""
	A node class for an AVL Tree
	"""

	def __init__(self, value):
		self.parent = None
		self.left_child = None
		self.right_child = None
		self.value = value
		self.balance_factor = 0

	def number_of_children(self):
		if not self.left_child and not self.right_child:
			return 0
		if self.left_child and self.right_child:
			return 2
		return 1 

	def which_child(self):
		if self.parent:
			if self.parent.left_child == self:
				return -1
			if self.parent.right_child == self:
				return 1
		return 0

	def __return_only_child__(self):
		"""
		Assumes there's only one child
		"""
		if self.left_child:
			return self.left_child
		return self.right_child

class AVLTree():
	"""
	A self-balancing tree of AVLNodes
	"""

	def __init__(self):
		self.head = None
		self.size = 0

	def nonempty_or_raise(self):
		if self.size == 0:
			raise EmptyTreeException

	def rightmost_node(self, start_node):
		self.nonempty_or_raise()

		current_node = start_node
		while current_node.right_child:
			current_node = current_node.right_child
		return current_node

	def add_node(self, node_to_be_added):

		"""
		edge case if tree is empty
		"""
		if not self.size: 
			self.head = node_to_be_added
			self.size = 1
			return
		"""
		add node to far right
		"""
		largest_node = self.rightmost_node(self.head)
		largest_node.right_child = node_to_be_added
		node_to_be_added.parent = largest_node
		self.size += 1
		self.check_balance(node_to_be_added)

	def delete_node(self, parent, child, which_child):
		if not child:
			if which_child == -1:
				parent.left_child = child
				child.parent = parent
			else:
				parent.right_child = child
				child.parent = parent
		else:
			if which_child == -1:
				parent.left_child = None
			else:
				parent.right_child = None

	def remove_node(self, node):
		"""
		remove node and adjust tree accordingly
		"""

		self.nonempty_or_raise()

		"""
		edge case if only one node
		"""
		if self.size == 1:
			self.size = 0
			self.head = None
			return

		"""
		case 1: node has no children
		"""
		if not node.number_of_children():
			"""
			remove node
			"""
			self.delete_node(node.parent, None, node.which_child())
			self.size -= 1
			self.check_balance(parent)
		"""
		case 2: node has one child
		"""
		if node.number_of_children() == 1:
			"""
			remove node and make the child the new child of the deleted node's parent
			"""
			child = node.__return_only_child__()
			self.delete_node(node.parent, child, node.which_child())
			self.size -= 1
			self.check_balance(child)
		"""
		case 3: node has two children
		"""
		if node.number_of_children() == 2:
			"""
			go as far right from the left child as possible
			"""
			insertion_position = self.rightmost_node(node.left_child)
			"""
			make the right child the child of this node
			"""
			insertion_position.right_child = node.right_child
			node.right_child.parent = insertion_position
			node.right_child = None
			"""
			treat as if case 2
			"""
			self.remove_node(node)
		

	def check_balance(self, node):
		self.nonempty_or_raise()

		if fabs(node.balance_factor) > 1:
			self.rebalance(node)
			return

		if node.parent != None:
			node.parent.balance_factor += node.which_child()

			if node.parent.balance_factor:
				self.check_balance(node.parent)

	def rebalance(self, node):

		if node.balance_factor > 0:
			if node.right_child.balance_factor < 0:
				self.rotate_right(node.right_child)
				self.rotate_left(node)
			else:
				self.rotate_left(node)

		elif node.balance_factor < 0:
			if node.left_child.balance_factor > 0:
				self.rotate_left(node.left_child)
				self.rotate_right(node)
			else:
				self.rotate_right(node)

	def rotate_left(self, node):
		new_root = node.right_child
		node.right_child = new_root.left_child
		if new_root.left_child:
		    new_root.left_child.parent = node
		new_root.parent = node.parent
		if self.head == node:
		    self.head = new_root
		else:
		    if node.which_child == -1:
		        node.parent.left_child = new_root
		    else:
		        node.parent.right_child = new_root
		new_root.left_child = node
		node.parent = new_root
		node.balance_factor = node.balance_factor - 1 - max(new_root.balance_factor, 0)
		new_root.balance_factor = new_root.balance_factor - 1 - min(node.balance_factor, 0)

	def rotate_right(self, node):
		new_root = node.left_child
		node.left_child = new_root.right_child
		if new_root.right_child:
		    new_root.right_child.parent = node
		new_root.parent = node.parent
		if self.head == node:
		    self.head = new_root
		else:
		    if node.which_child == 1:
		            node.parent.right_child = new_root
		    else:
		        node.parent.left_child = new_root
		new_root.right_child = node
		node.parent = new_root
		node.balance_factor = node.balance_factor + 1 + max(new_root.balance_factor, 0)
		new_root.balance_factor = new_root.balance_factor + 1 + min(node.balance_factor, 0)

	def go_left(self, current_position, end_value):
		return current_position.which_child() == -1 or current_position == self.head or current_position.parent.value < end_value

	def update_value(self, child):
		"""
		 -1 if no child(-2 if there's a child)
		"""
		if not child:
			return -1
		else:
			return -2

	def lookup_when_added(self, end_value, current_value=None, current_position=None):
		"""
		a method to lookup when the node was added based on the current position it occupies
		"""

		self.nonempty_or_raise()
		"""
		current_position = size of tree if no argument given
		current_value = rightmost node's value if no argument given
		"""
		if not current_position:
			current_position = self.rightmost_node(self.head)
			current_value = self.size

		if current_value == end_value:
			return self.size - current_value

		else:
			"""
			if current node is a left child or current node is the head or parent's value < value we're looking for
			"""
			if self.go_left(current_position, end_value):
				"""
				current position = current_position -1 if left child has no right child(-2 if there's a right child)
				"""
				current_value += self.update_value(current_position.left_child.right_child)
				self.lookup_when_added(end_value, current_value, current_position.left_child)

			else:
				"""
				current_position = current_position -1 if current node doesn't have a left child(-2 if there's a left child)
				"""
				current_value += self.update_value(current_position.left_child)
				self.lookup_when_added(end_value, current_value, current_position.parent)