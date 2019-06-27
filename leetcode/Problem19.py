class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    listLen = 0
    d = ListNode(0)
    d.next = head

    curr = head
    while curr is not None:
        listLen += 1
        curr = curr.next

    listLen -= n
    curr = d
    while listLen > 0:
        curr = curr.next
        listLen -= 1
    curr.next = curr.next.next

    return d.next

def removeNthFromEndSinglePass(head: ListNode, n: int) -> ListNode:
    d = ListNode(0)
    d.next = head
    first = d
    second = d

    for i in range(0, n+1):
        first = first.next
    
    while first is not None:
        first = first.next
        second = second.next
    second.next = second.next.next

    return d.next

