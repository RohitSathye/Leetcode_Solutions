# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
        Pool = []

        while head:
            if head.next in Pool:
                return True
            else:
                Pool.append(head.next)
                head = head.next

        return False

        