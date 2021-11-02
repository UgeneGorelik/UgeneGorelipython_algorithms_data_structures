class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head  = None

    def insert_at_start(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next =self.head
            self.head=node

    def get_last_node(self):
        current =self.head
        while current.next:
            current = current.next
        return current

    def insert_at_end(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        last_node = self.get_last_node()
        last_node.next=node

    def insert_after_specifc_node(self,insert_after,data):
        node = Node(data)
        node.next =insert_after.next
        insert_after.next  = node


# Nth-to-last Linked List Element
def nth_last(linked_list,n):
    pointer1 = linked_list.head
    pointer2 = linked_list.head

    for i in range(0,n):
        pointer1 = pointer1.next

    while pointer1:
        pointer1=pointer1.next
        pointer2=pointer2.next

    print(pointer2.data)


llist = LinkedList()
llist.insert_at_start(20)
llist.insert_at_start(4)
llist.insert_at_start(15)
llist.insert_at_start(35)

nth_last(llist,2)