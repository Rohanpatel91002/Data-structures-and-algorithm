from common import *

def preorder_traversal(root):
    if root == None:
        return
    
    print(root.data, end= ", ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def postorder_traversal(root):
    if root == None:
        return
    
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=", ")

def inorder_traversal(root):
    if root == None:
        return
    
    inorder_traversal(root.left)
    print(root.data, end=", ")
    inorder_traversal(root.right)


root = Binary_Tree(1)

child1 = Binary_Tree(2)
child2 = Binary_Tree(3)
child3 = Binary_Tree(4)
child4 = Binary_Tree(5)
child5 = Binary_Tree(6)

root.left = child1
root.right = child2

child1.left = child3
child1.right = child4

child2.left = child5    

#     1
#    / \
#   2   3
#  / \  /
# 4   5 6
#
# preorder traversal - 1, 2, 4, 5, 3, 6
# postorder traversal - 4, 5, 2, 6, 3, 1
# inorder traversal - 4, 2, 5, 1, 6, 3

preorder_traversal(root)
postorder_traversal(root)
inorder_traversal(root)
