# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        out: Optional[ListNode] = ListNode()
        prev_out: ListNode = out
        prev_carry: int = 0
        prev_l1: Optional[ListNode] = l1
        prev_l2: Optional[ListNode] = l2
        not_none1: bool = prev_l1 is not None
        not_none2: bool = prev_l2 is not None
        not_nonec: bool = prev_carry != 0

        while not_none1 or not_none2 or not_nonec:

            if prev_l1 is not None:
                val1: int = prev_l1.val if prev_l1.val is not None else 0
            else:
                val1: int = 0
            if prev_l2 is not None:
                val2: int = prev_l2.val if prev_l2.val is not None else 0
            else:
                val2: int = 0

            new_carry, digit = divmod(val1+val2+prev_carry, 10)

            prev_carry = new_carry

            new_node = ListNode(val=digit)
            prev_out.next = new_node
            prev_out = new_node

            prev_l1 = prev_l1.next if prev_l1 else None
            prev_l2 = prev_l2.next if prev_l2 else None
            not_none1 = prev_l1 is not None
            not_none2 = prev_l2 is not None
            not_nonec = prev_carry != 0

        if out.next is not None:
            return out.next
        return out