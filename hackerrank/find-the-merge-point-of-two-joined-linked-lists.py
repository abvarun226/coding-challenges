# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def findMergeNode(head1, head2):
    ''' Optimal Solution - O(n) '''

    p1, p2 = head1, head2
    l1, l2 = 0, 0

    # Get the length of first and second list
    while p1 is not None:
        l1 += 1
        p1 = p1.next
    while p2 is not None:
        l2 += 1
        p2 = p2.next
    
    # Get the difference in length between them
    d = l1 - l2 if l1 > l2 else l2 - l1

    # Traverse the bigger list `d` steps, so that we are at a point
    # where both lists have equal nodes remaining in traversal.
    p1 = head1
    p2 = head2
    if l1 > l2:
        for _ in range(d):
            p1 = p1.next
    else:
        for _ in range(d):
            p2 = p2.next

    # Now traverse both lists one by one until p1 == p2, 
    # which is the merge point
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    
    # Return the data at the merge point.
    return p1.data

def findMergeNodeBruteForce(head1, head2):
    ''' Brute Force - O(nm) '''
    p1 = head1
    p2 = head2
    while p1 is not None:
        while p2 is not None:
            if p1 == p2:
                return p1.data
            p2 = p2.next
        p1 = p1.next
        p2 = head2
    return None