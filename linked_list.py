class LLNode:

	def __init__(self, prev=None, next=None):
		self.previous = prev
		self.next = next
		self.position = 0

class LinkedList:

	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def update_positions(self, node):
		if node == self.head:
			node.position = 0

		else:
			self.update_positions(node.previous)
			node.position = node.previous.position + 1

	def add_to_head(self, node):
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

