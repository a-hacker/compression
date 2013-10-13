class LLNode:

	def __init__(self, prev=None, next=None):
		self.previous = prev
		self.next = next

class LinkedList:

	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def add_to_head(self, node):
		if self.head == None:
			self.head = node
		else:
			self.head.previous = node
			self.head = node

	def move_to_head(self, node):
		if self.head == node:
			return
		if node == self.tail:
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

