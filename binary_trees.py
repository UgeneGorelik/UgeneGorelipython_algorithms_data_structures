from linked_list import Node,LinkedList

class TreeNode:
    def __init__(self, data, left=None, right=None ):
        self.left = left
        self.right = right
        self.data = data



def tree_in_order_to_list(root,head : LinkedList):
    if not root:
        return head

    tree_in_order_to_list(root.left,head)
    head.insert_at_end(root.data)
    tree_in_order_to_list(root.right, head)

    return head


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


a = TreeNode(20)
a.left = TreeNode(10)
a.right = TreeNode(30)
a.right.left = TreeNode(25)
a.right.right = TreeNode(100)

l = LinkedList()

x=tree_in_order_to_list(a,l)
print(1)