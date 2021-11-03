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

    def print_list(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr =curr.next

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

    def reverse(self):
        curr = self.head
        prev = None
        tmp = None
        while curr:
            tmp = Node(curr.data,curr.next)
            curr.next = prev
            prev = curr
            curr = tmp.next




        self.head = prev

        return self.head

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


#merge sorted lists
def merge_sortedlists(head1, head2):
    new_list_node = Node(0)
    tail = new_list_node
    while True:

        if head1 is None:
            tail.next = head2
            break
        if head2 is None:
            tail.next = head1
            break

        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    return new_list_node.next

llist = LinkedList()
llist.insert_at_end(20)
llist.insert_at_end(4)
llist.insert_at_end(15)
llist.insert_at_end(35)

llist.reverse()
llist.print_list()

