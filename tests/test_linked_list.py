from builtins import range
from unittest import TestCase
from pystructures.linked_lists import LinkedList, Node, DoublyLinkedList


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

class TestLinkedList(TestCase):
	def test_insert(self):
		""" A simple test to check if insertion works as expected in a singly linked list """
		l = LinkedList()
		results = [l.insert(val) for val in range(10, 100, 10)]
		self.assertEqual(len(set(results)), 1)
		self.assertTrue(results[0], msg="Testing for successful insertion...")
		self.assertEqual(len(results), l.size, msg="Testing if # of results equal list size...")

class TestDoublyLinkedList(TestCase):
    def test_init(self):
        """ A test to check instantiation of an empty DoublyLinkedList """
        dl = DoublyLinkedList()
        self.assertEqual(dl.head, None)

    def test_insert(self):
        """ A test to check the various states of the DoublyLinkedList when insertion is performed """
        dl = DoublyLinkedList()
        dl.insert("A")
        dl.insert("B")

        self.assertEqual(dl.head.value, "B")
        self.assertEqual(dl.tail.value, "A")
        self.assertEqual(dl.tail.previous.value, "B")
