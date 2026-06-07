# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_temp = curr.next   # 1. save
            curr.next = prev        # 2. reverse
            prev = curr             # 3. move prev
            curr = next_temp        # 4. move curr

        return prev

            

