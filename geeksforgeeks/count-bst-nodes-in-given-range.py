"""
https://www.geeksforgeeks.org/count-bst-nodes-that-are-in-a-given-range/

Given a Binary Search Tree (BST) and a range, count number of nodes that lie in the given range.
"""

class Node:
    # Constructor to create a new node  
    def __init__(self, data):  
        self.data = data  
        self.left = None
        self.right = None

def countNodes(root, low, high):
    if root == None:
        return 0

    if root.data == high and root.data == low:
        return 1

    if root.data >= low and root.data <= high:
        return 1 + countNodes(root.left, low, high) + countNodes(root.right, low, high)

    elif low > root.data:
        return countNodes(root.right, low, high)

    else:
        return countNodes(root.left, low, high)

if __name__ == '__main__': 
    root = Node(10)
    root.left = Node(5)
    root.right = Node(50)
    root.left.left = Node(1)
    root.right.left = Node(40)
    root.right.right = Node(100)

    low = 5
    high = 45
    print(countNodes(root, low, high))