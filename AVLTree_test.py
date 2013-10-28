from testify import *

from AVLTree import AVLTree
from AVLTree import AVLNode
from AVLTree import EmptyTreeException

class AVLNodeTest(TestCase):

	@setup
	def setup(self):
		self.node = AVLNode(0)
		self.left_child = AVLNode(1)
		self.right_child = AVLNode(2)
		self.node.left_child = self.left_child
		self.node.right_child = self.right_child
		self.left_child.parent = self.node
		self.right_child.parent = self.node

	def test_number_of_children(self):
		assert_equals(self.node.number_of_children(), 2)
		assert_equals(self.left_child.number_of_children(), 0)

	def test_left_or_right(self):
		assert_equals(self.node.left_or_right(), 0)
		assert_equals(self.left_child.left_or_right(), -1)
		assert_equals(self.right_child.left_or_right(), 1)

	def test_return_only_child(self):
		self.right_child.left_child = AVLNode(6)
		self.left_child.right_child = AVLNode(7)
		assert_equals(self.right_child.__return_only_child__(), self.right_child.left_child)
		assert_equals(self.left_child.__return_only_child__(), self.left_child.right_child)

class EmptyTree(TestCase):
	@setup
	def setup(self):
		self.tree = AVLTree()

	def test_rightmost_node(self):
		self.assertRaises(EmptyTreeException, AVLTree.rightmost_node, self.tree, self.tree.head)

	def test_add_node(self):
		self.tree.add_node(AVLNode(0))
		assert_equals(self.tree.head.value, 0)

	def test_check_balance(self):
		self.assertRaises(EmptyTreeException, AVLTree.check_balance, self.tree, self.tree.head)

	def test_lookup_when_added(self):
		pass


class NominalCase(TestCase):
	
	@setup
	def setup(self):
		self.tree = AVLTree()
		self.root = AVLNode(1)
		self.left = AVLNode(0)
		self.right = AVLNode(2)
		self.tree.add_node(self.left)
		self.tree.add_node(self.root)
		self.tree.add_node(self.right)

	def test_rightmost_node(self):
		assert_equals(self.tree.rightmost_node(self.root).value, 2)
		assert_equals(self.tree.rightmost_node(self.left).value, 0)

	def test_add_node(self):
		self.tree.add_node(AVLNode(3))
		assert_equals(self.left.value, 0)
		assert_equals(self.root.value, 1)
		assert_equals(self.right.value, 2)
		assert_equals(self.right.right_child.value, 3)
		assert_equals(self.left.balance_factor, 0	)
		assert_equals(self.right.balance_factor, 1)
		assert_equals(self.root.balance_factor, 1)

	def test_remove_node_with_no_children(self):
		self.tree.remove_node(self.left)
		assert_equals(self.root.number_of_children(), 1)

	def test_remove_head(self):
		self.tree.remove_node(self.root)
		assert_equals(self.root.value, 0)
		assert_equals(self.right.value, 2)

	def test_remove_node_with_one_child(self):
		self.tree.add_node(AVLNode(3))
		self.tree.remove_node(self.right)
		assert_equals(self.right.value, 3)

	def test_check_balance(self):
		pass

	def test_rebalance(self):
		pass

	def test_rotate_left(self):
		pass

	def test_rotate_right(self):
		pass	

	def test_lookup_when_added(self):
		pass

if __name__ == "__main__":
	run()