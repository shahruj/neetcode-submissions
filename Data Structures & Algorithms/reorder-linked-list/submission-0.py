# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # find the mid point and end
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        

        #reverse the second half
        # reverse second half
        prev = None
        curr = slow.next

        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # iterate through from front and second half stringing the results together
        printLinkedList(head)
        printLinkedList(prev)

        output = ListNode(0)
        currout = output
        i=0
        while head and prev:
            print(i % 2)
            if i % 2 == 0:
                currout.next = head
                head = head.next
            else:
                currout.next = prev
                prev = prev.next   
            currout = currout.next
            i+=1        

        currout.next = head or prev
        printLinkedList(output)
         

        # return output