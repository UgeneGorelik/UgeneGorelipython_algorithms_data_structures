

class Node:
    def __init__(self, data, left=None, right=None ):
        self.left = left
        self.right = right
        self.data = data



def tree_in_order_to_list(root,head ):
    if not root:
        return head

    tree_in_order_to_list(root.left,head)
    head.insert_at_end(root.data)
    tree_in_order_to_list(root.right, head)

    return head




def height(node :Node):
    if not node:
        return 0
    return (1+max(height(node.left),height(node.right)))

def diameter(root: Node):
    if not root:
        return 0
    h_left = height(root.left)
    h_right = height(root.right)

    d1 = diameter(root.left)
    d2 = diameter(root.right)

    return max(1+h_left+h_right ,max(d1,d2) )


def find_lca(root,l,r):

    if not root:
        return None

    if root.data == l or root.data == r:
        return root

    left_lca = find_lca(root.left,l,r)
    right_lca = find_lca(root.right, l, r)

    if left_lca and right_lca:
        return root

    if left_lca:
        result = left_lca

    if right_lca:
        result =right_lca


    return result




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print ("LCA(4,5) = ", find_lca(root, 4, 5).data)
print ("LCA(4,6) = ", find_lca(root, 4, 6).data)
print ("LCA(3,4) = ", find_lca(root, 3, 4).data)
print ("LCA(2,4) = ", find_lca(root, 2, 4).data)