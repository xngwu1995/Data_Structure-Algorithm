import unittest


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


START = 0
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def check_length(self, location):
        if location >= self.length:
            raise ValueError("Incorrect length")

    def get(self, location):
        self.check_length(location)
        cur = self.head
        for _ in range(location):
            cur = cur.next
        return cur

    def add(self, location, val):
        new_node = ListNode(val)
        if location == START:
            prev = self.head
            self.head = new_node
            self.head.next = prev
        elif location > START:
            prev = self.get(location - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.length += 1
    
    def set_node(self, location, val):
        cur = self.get(location)
        cur.val = val
    
    def remove(self, location):
        self.check_length(location)
        prev = self.get(location - 1)
        prev.next = prev.next.next
        self.length -= 1
    
    def traverse(self):
        cur = self.head
        if not cur:
            return ""
        linked_list = ""
        while cur.next is not None:
            linked_list += str(cur.val) + "->"
            cur = cur.next
        linked_list += str(cur.val)
        return linked_list

class TestLinkedList(unittest.TestCase):
    def test_code(self):
        ll = MyLinkedList()
        linked_list = ll.traverse()
        self.assertEqual(linked_list, "")
        ll.add(0, 1)
        ll.add(1, 2)
        ll.add(2, 5)
        ll.add(3, 6)
        linked_list = ll.traverse()
        self.assertEqual(linked_list, "1->2->5->6")
        ll.set_node(1, 100)
        linked_list = ll.traverse()
        self.assertEqual(linked_list, "1->100->5->6")
        self.assertEqual(ll.get(1).val, 100)
        ll.remove(3)
        linked_list = ll.traverse()
        self.assertEqual(linked_list, "1->100->5")
        self.assertRaises(ValueError, ll.remove, 3)
        self.assertRaises(ValueError, ll.add, 4, 1000)
        self.assertRaises(ValueError, ll.set_node, 3, 13)
        self.assertRaises(ValueError, ll.get, 3)

if __name__ == '__main__':
    unittest.main()
