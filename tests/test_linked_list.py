from unittest import TestCase
from pystructures.linked_lists import Node

class TestNode(TestCase):
	def test_value(self):
		""" A simple test to check the Node's value """
		node = Node(10)
		self.assertEqual(10, node.value)
