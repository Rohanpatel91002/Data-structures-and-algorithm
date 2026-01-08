from common import *

def find_diameter_optimized(root):
    if root == None:
        return 0,0 # height, diameter
    
    left_height,left_diameter = find_diameter_optimized(root.left)
    right_height,right_diameter = find_diameter_optimized(root.right)

    diameter_through_root = left_height + right_height

    answer_diameter = max(diameter_through_root, left_diameter, right_diameter)
    current_tree_height = 1 + max(left_height, right_height)


    return current_tree_height, answer_diameter


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
height,diameter = find_diameter_optimized(root)
print(diameter)