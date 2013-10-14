class LLNode:

	def __init__(self, prev=None, next=None):
		self.previous = prev
		self.next = next
		self.position = 0

class LinkedList:

	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def update_positions(self, node=self.tail):
		if node == head:
			node.position = 0
		else:
			self.update_positions(node.previous)
			position = node.previous.position + 1

	def add_to_head(self, node):
		node.position = 0
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.head.previous = node
			self.head = node
		self.update_positions()

	def move_to_head(self, node):
		if self.head == node:
			return
		if node == self.tail:
			self.tail = node.previous
			node.previous.next = None
			node.next = self.head
			node.previous = None
			self.head = node
		else:
			node.previous.next = node.next
			node.next.previous = node.previous
			node.next = self.head
			node.previous = None
			self.head = node
		self.update_positions()

