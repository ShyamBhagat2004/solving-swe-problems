class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #Getting midpoint and end of list 
        second = slow.next
        slow.next = None
        prev = None
        #Reversing the list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
        
