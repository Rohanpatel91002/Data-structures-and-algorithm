from search_in_BST import *
class BST:
    def __init__(self, Value):
        self.data = Value
        self.left = None
        self.right = None

def search_data_in_range(root, low, high):
    if root == None:
        return
    
    if root.data > low:
        search_data_in_range(root.left, low, high)
    
    if low<= root.data <= high:
        print(root.data, end = " ")
    
    if root.data< high:
        search_data_in_range(root.right, low, high)
    
root = get_BST_example()

search_data_in_range(root, 25, 55)
