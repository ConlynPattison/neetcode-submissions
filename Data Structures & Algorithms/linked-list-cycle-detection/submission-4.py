# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        single = head
        double = head

        if not single or not double.next or not double.next.next:
            return False

        double = double.next.next

        while double and single:
            if single == double: return True
            if not double.next or not double.next.next: return False
            single = single.next
            double = double.next.next
            

    def hasCycleSinglePass(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False