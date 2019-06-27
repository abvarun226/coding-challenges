class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# your task is to complete this function
# function shouldn't return anything
# use self.head to access head in the method
def reverseList(self):
    if self.head is None:
        return None
    
    if self.head.next is None:
        return self.head

    p = None
    f = self.head
    while f.next is not None:
        f.next, p, f = p, f, f.next
    f.next = p
    self.head = f