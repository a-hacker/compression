from testify import *

from linked_list import LinkedList
from linked_list import LLNode

class NodeTest(TestCase):

	@setup
	def setup(self):
		self.next = LLNode()
		self.prev = LLNode()
		self.node = LLNode(prev=self.prev, next=self.next)

	def test_contents_correct(self):
		assert_equals(self.node.previous, self.prev)
		assert_equals(self.node.next, self.next)

class EmptyList(TestCase):

	@setup
	def setup(self):
		self.linked_list = LinkedList()

	def test_add_to_head(self):
		node1 = LLNode()
		self.linked_list.add_to_head(node1)
		assert_equals(self.linked_list.head, node1)

class ThreeElementList(TestCase):

	@setup
	def setup(self):
		self.node1 = LLNode()
		self.node2 = LLNode(prev=self.node1)
		self.node3 = LLNode(prev=self.node2)
		self.node1.next = self.node2
		self.node2.next = self.node3
		self.linked_list = LinkedList(self.node1, self.node3)

	def test_add_to_head(self):
		node4 = LLNode()
		self.linked_list.add_to_head(node4)
		assert_equals(self.linked_list.head, node4)

	def test_move_to_front(self):
		self.linked_list.move_to_head(self.node2)
		assert_equals(self.linked_list.head, self.node2)

if __name__ == "__main__":
	run()