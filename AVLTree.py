
class AVLNode():
	"""
	A node class for an AVL Tree
	"""

	def __init__(self):
		pass

class AVLTree():
	"""
	A self-balancing tree of AVLNodes
	"""

	def __init__(self):
		pass

	def add_node(self):
		"""
		add node to far right
		check balance
		"""
		pass

	def remove_node(self):
		"""
		remove node and adjust tree accordingly

		case 1: node has no children
			remove node
			check balance
		case 2: node has one child
			remove node and make the child the new child of the deleted node's parent
			check balance
		case 3: node has two children
			go as far right from the left child as possible
			make the right child the child of this node
			treat as if case 2
		"""
		pass

	def check_balance(self):
		"""
		checks that the tree is properly balanced

		start at head
		if no children
			return
		if only one child
			if child has children
				adjust tree
		if two children

		"""
		pass

	def lookup_when_added(self, current_position=None, current_value=None):
		"""
		a method to lookup when the node was added based on the current position it occupies

		current_position = size of tree if no argument given
		current_value = rightmost node's value if no argument given
		if current_value is the value we're looking for
			return size of tree - current_position
		else
			if current node is a left child or current node is the head or parent's value < value we're looking for
				current position = current_position -1 if left child has no right child(-2 if there's a right child) 
				lokup_when_added(left child)
			if current node is not a left child and parent's value > value we're looking for
				current_position = current_position -1 if current node doesn't have a left child(-2 if there's a left child)
				lokup_when_added(parent)
		"""
		pass