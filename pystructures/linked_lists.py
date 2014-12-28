"""
	This script contains implementations for:
	- Singly Linked Lists
	- Doubly Linked Lists
"""
from __future__ import print_function
from future.utils import with_metaclass
from builtins import object, str, map
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
        pass

    @abstractmethod
    def __str__(self):
        """ Custom output format for the data structure """
        pass

    @property
    def size(self):
        """ Returns the size of the list """
        return self.__size
    
    @size.setter
    def size(self, new_size):
        """ Sets the current size to the one provided """
        self.__size = new_size

    @property
    def head(self):
        """ Returns the head node of the list """
        return self.__head

    @head.setter
    def head(self, node):
        """ Sets the head node of the list to the one provided """
        if isinstance(node, Node):
            self.__head = node
        else:
            raise ValueError("Cannot set head to a " + str(type(node)))
    

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

class LinkedList(AbstractList):
    """ A concrete implementation of a list
        Class represents a singly-linked list,
        where each node has only a value and a pointer to its next node.    
    """

    def insert(self, item):
        """ Given an item, this function prepends it to the current head.
            Returns true if item was inserted successfully.
            Raises an exception otherwise.
        """
        if not item or isinstance(item, Node):
            raise ValueError("Cannot insert a None or a Node type")

        if self.head == None:
            self.head = Node(item)
        else:
            node = Node(item)
            node.next = self.head
            self.head = node

        self.size += 1
        return True

    def remove(self, item):
        pass

    def __str__(self):
        """ Prints content in a linear structure """
        current, output = self.head, []
        if not current:
            return "Empty"
        else:
            while current != None:
                output.append(current.value)
                current = current.next
            output.append("EOL")
            res = " -> ".join(list(map(str, output)))
            return res

