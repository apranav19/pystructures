"""
	This script contains implementations for:
	- Singly Linked Lists
	- Doubly Linked Lists
"""
from future.builtins import with_metaclass
from builtins import object, str
from abc import ABCMeta, abstractmethod

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

class AbstractList(with_metaclass(ABCMeta, object)):
    """ An abstract definition of an unordered list """

    def __init__(self):
        self.__head = None
        self.__size = 0

    @abstractmethod
    def insert(self, item):
        """ Appends an item to the list """
        pass

    @abstractmethod
    def remove(self, item):
        """ Remove an item from the list """

    @property
    def size(self):
        """ Returns the size of the list """
        return self.__size
    
    def is_empty(self):
        """ Returns true if size is 0 false otherwise """
        return self.__size == 0

    def contains(self, item):
        """ Search for an item in the list """
        res, current = False, self.__head

        while current != None:
            if current.value == item:
                res = True
                break
            current = current.next

        return res
        