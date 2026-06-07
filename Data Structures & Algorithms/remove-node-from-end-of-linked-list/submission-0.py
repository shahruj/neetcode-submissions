class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # move both until fast reaches end
        while fast.next:
            slow = slow.next
            fast = fast.next

        # delete the node
        slow.next = slow.next.next

        return dummy.next