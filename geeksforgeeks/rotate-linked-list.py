class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# This function should rotate list counter-
# clockwise by k and return new head (if changed) 
def rotateList(head, k):
    length = 0
    
    # Find the length of the list.
    f = head
    while f is not None:
        f = f.next
        length += 1

    # The current last element has to point to
    # the current head element.
    last = head
    while last.next is not None:
        last = last.next
    last.next = head
    
    # Find the new head element
    for i in range(0, k):
        head = head.next

    # Find the new last element and 
    # set the next pointer to None
    f = head
    for i in range(0, length-1):
        f = f.next
    f.next = None
    
    return head