"""
	This script contains implementations for:
	- Singly Linked Lists
	- Doubly Linked Lists
"""
from builtins import object, str

class Node(object):
    """
        Attributes include:
        value: The value of the Node
        next: The pointer to the next Node
    """
    def __init__(self, value):
        self.__value = value
        self.__next = None

    @property
    def value(self):
        """ Returns the value of the Node """
        return self.__value

    @value.setter
    def value(self, value):
        """ Sets the value of the Node """
        self.__value = value

    @property
    def next(self):
        """ Returns the next Node """
        return self.__next

    @next.setter
    def next(self, node):
        """ Sets the pointer to the next Node """
        if node == None or isinstance(node, Node):
            self.__next = node
        else:
            raise ValueError("cannot set next to a " + str(type(node)))

    def __str__(self):
        return str(self.__value)