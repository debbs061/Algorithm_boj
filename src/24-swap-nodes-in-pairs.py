# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            nextPair = cur.next.next
            second = cur.next

            # swap
            second.next = cur
            cur.next = nextPair
            prev.next = second

            # update
            prev = cur
            cur = nextPair

        return dummy.next

        # if not head:
        #     return None
        #
        # dummy = ListNode()
        # dummy.next = head.next if head.next else head
        # prev = dummy
        # cur = head
        # cnt = 1
        #
        # while cur:
        #     if not cnt % 2:
        #         real_next = cur.next
        #         nxt = cur.next.next if cur.next and cur.next.next else cur.next
        #         cur.next = prev
        #         prev.next = nxt
        #         cur = real_next
        #     else:
        #         prev = cur
        #         cur = cur.next
        #     cnt += 1
        #
        # return dummy.next
