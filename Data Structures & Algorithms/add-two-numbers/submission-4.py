# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2 = l2

        head = ListNode(0,None)
        curr = head
        carryover = 0
        while curr1 or curr2:
            if not curr1:
                val1 = 0
            else:
                val1 = curr1.val
            
            if not curr2:
                val2 = 0
            else:
                val2 = curr2.val

            val  = val1 + val2 + carryover
            if val>9:
                carryover = val//10
                val = val%10
            else:
                carryover = 0

            print(val)
            curr.val = val

            if curr1:
                curr1 = curr1.next
            
            if curr2:
                curr2 = curr2.next

            if curr1 or curr2:
                curr.next = ListNode(0,None)
                curr = curr.next
        
        print(carryover)
        print(print_linked_list(head))

        if carryover != 0:
            curr.next = ListNode(carryover,None)

        return head
            
            
            
