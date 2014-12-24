from unittest import TestCase
from pystructures.linked_lists import Node


class TestNode(TestCase):
    def test_value(self):
        """ A simple test to check the Node's value """
        node = Node(10)
        self.assertEqual(10, node.value)

    def test_improper_node(self):
        """ A test to check if an invalid data type is set as a node's next"""
        node = Node(10)
        with self.assertRaises(ValueError):
            node.next = "Hello"
