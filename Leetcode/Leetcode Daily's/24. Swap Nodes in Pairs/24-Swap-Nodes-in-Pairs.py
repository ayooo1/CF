 # Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            nxt = cur.next.next
            save = cur.next


            save.next = cur
            cur.next = nxt
            prev.next = save

            prev = cur
            cur = nxt

        return dummy.next

        
