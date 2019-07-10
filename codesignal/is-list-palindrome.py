"""
https://app.codesignal.com/interview-practice/task/HmNvEkfFShPhREMn4

Given a singly linked list of integers, determine whether or not it's a palindrome.
"""

# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

# def isListPalindrome(l):
#     stack = []
#     ptr = l
#     while ptr is not None:
#         stack.append(ptr.value)
#         ptr = ptr.next
#     ptr = l
#     while ptr is not None:
#         if stack.pop() != ptr.value:
#             return False
#         ptr = ptr.next
#     return True

def isListPalindrome(l):
    length = 0
    ptr = l
    while ptr is not None:
        length += 1
        ptr = ptr.next
    
    if length == 0 or length == 1:
        return True
    if length == 2:
        ptr = l
        return ptr.value == ptr.next.value

    mid = int(length/2)
    
    ptr = l
    i = 0
    while i < mid:
        ptr = ptr.next
        i += 1
    if length % 2 != 0:
        ptr = ptr.next
    
    r = reverse(ptr)

    i = 0
    while i < mid:
        i += 1
        if l.value != r.value:
            return False
        l = l.next
        r = r.next

    return True
    
def reverse(l):
    prev = None
    curr = l
    while curr is not None:
        n = curr.next
        curr.next = prev 
        prev = curr 
        curr = n
    l = prev
    return l
