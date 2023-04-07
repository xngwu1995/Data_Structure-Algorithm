class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


START = 0
class MyLinkedList:

    def __init__(self):
        self.head = None
    
    def get(self, location):
        cur = self.head
        for _ in range(location):
            cur = cur.next
        return cur.val

    def add(self, location, val):
        new_node = ListNode(val)
        if location == START:
            prev = self.head
            self.head = new_node
            self.head.next = prev
        elif location > START:
            prev = self.head
            for _ in range(location - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
    
    def set_node(self, location, val):
        cur = self.head
        for _ in range(location):
            cur = cur.next
        cur.val = val
    
    def remove(self, location):
        prev = self.head
        for _ in range(location - 1):
            prev = prev.next
        prev.next = prev.next.next
    
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

if __name__ == '__main__':
    ll = MyLinkedList()
    ll.add(0, 1)
    ll.add(1, 2)
    ll.add(2, 5)
    ll.add(3, 6)
    linked_list = ll.traverse()
    assert linked_list == "1->2->5->6"
    ll.set_node(1, 100)
    linked_list = ll.traverse()
    assert linked_list == "1->100->5->6"
    assert ll.get(1) == 100
    ll.remove(3)
    linked_list = ll.traverse()
    assert linked_list == "1->100->5"