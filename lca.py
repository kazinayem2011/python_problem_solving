# Make node for tree . . .
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None





# Find LCA . . .
def lca(root, node1, node2):
    if root is None:
        return None

    # If node1 or node2 is equal to root element
    if root.key == node1 or root.key == node2:
        return root.key

    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    if left and right:
        return root.key

    if left:
        return left
    else:
        return right


# Node structure according to tree diagram . . .
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)

# Let's print the output of LCA for two nodes . . .
node1 = 3
node2 = 7
l_c_a = lca(root, node1, node2)
print("The LCA of %d and %d is %d" % (node1, node2, l_c_a))