"""
WARNING: this doubly-linked list only works with the compression module. Not meant for use elsewhere.
"""

class LLNode:
	"""
	An incredibly basic node class to simply store position within list
	"""

	def __init__(self, prev=None, next=None):
		self.previous = prev
		self.next = next
		self.position = 0

class LinkedList:
	"""
	A linked list with trivial operations to perform the functions compression needs it to
	"""

	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def update_positions(self, node):
		"""
		keeps track of each node's position in the list
		"""
		if node == self.head:
			node.position = 0

		else:
			self.update_positions(node.previous)
			node.position = node.previous.position + 1

	def add_to_head(self, node):
		"""
		adds a new node to the head of the list
		must readjust each node's position in the list afterwards
		"""
		node.position = 0

		if self.head == None:
			self.head = node
			self.tail = node

		else:
			self.head.previous = node
			node.next = self.head
			self.head = node

		self.update_positions(self.tail)

	def move_to_head(self, node):
		"""
		takes a node currently in the list and moves it to the head
		this removes the node from it's original position
		node positions must be readjusted from the previous node to the front
		this method does not check if the node is not in the list simply assumes it does
		"""
		if self.head == node:
			return

		if node == self.tail:
			self.tail = node.previous
			node.previous.next = None
			node.next = self.head
			self.head.previous = node
			node.previous = None
			self.head = node
			self.update_positions(self.tail)

		if self.head != node and self.tail != node:
			previous_node = node.previous
			node.previous.next = node.next
			node.next.previous = node.previous
			node.next = self.head
			self.head.previous = node
			node.previous = None
			self.head = node
			self.update_positions(previous_node)

