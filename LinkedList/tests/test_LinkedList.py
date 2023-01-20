import unittest
import pytest
from LinkedList.main import Node, LinkedList


class TestLinkedList(unittest.TestCase):
    def test_Node(self):
        temp = Node(1)
        assert temp.data == 1

    def test_LinkedListAdd(self):
        testList = LinkedList()

        for i in range(1, 5):
            testList.add_element(i)

        i = 1
        temp = testList.head
        while (temp != None):
            assert temp.data == i
            i += 1
            temp = temp.next

    def test_LinkedListDeleteFirst(self):
        testList = LinkedList()

        for i in range(1, 5):
            testList.add_element(i)

        testList.delete_first()

        i = 1
        temp = testList.head
        while (temp != None):
            assert temp.data == i + 1
            i += 1
            temp = temp.next

    def test_LinkedListDeleteLastEmpty(self):
        testList = LinkedList()

        testList.add_element(1)
        testList.delete_last()

        assert testList.head == None

    def test_LinkedListDeleteLast(self):
        testList = LinkedList()

        for i in range(1, 5):
            testList.add_element(i)

        testList.delete_last()

        i = 1
        temp = testList.head
        while (temp != None):
            assert temp.data == i
            i += 1
            temp = temp.next

    def test_LinkedListDeleteAtPosition(self):
        testList = LinkedList()

        for i in range(1, 5):
            testList.add_element(i)

        testList.delete_at_position(2)

        i = 1
        temp = testList.head
        while (temp != None):
            if (i == 2):
                i += 1
                break
            assert temp.data == i
            i += 1
            temp = temp.next

    def test_LinkedListDeleteAtPositionEmpty(self):
        testList = LinkedList()
        testList.delete_at_position(0)

        assert testList.head == None

    def test_LinkedListDeleteAtFirstPosition(self):
        testList = LinkedList()

        testList.add_element(1)
        testList.delete_at_position(0)

        assert testList.head == None
