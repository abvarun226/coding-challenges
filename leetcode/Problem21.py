# 21. Merge Two Sorted Lists

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    d = ListNode(0)
    ptr = d
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            ptr.next = l1
            l1 = l1.next
        else:
            ptr.next = l2
            l2 = l2.next
        ptr = ptr.next
    while l1 is not None:
        ptr.next = l1
        ptr = ptr.next
        l1 = l1.next
    while l2 is not None:
        ptr.next = l2
        ptr = ptr.next
        l2 = l2.next

    return d.next