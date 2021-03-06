# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # rev1 = self.reverseLink(l1)
        # rev2 = self.reverseLink(l2)
        rev1 = l1
        rev2 = l2
        ret = l = ListNode(0)
        carry = 0
        while rev1 or rev2:
            sum_ = (rev1.val if rev1 else 0) + (rev2.val if rev2 else 0) + carry
            if sum_ >= 10:
                carry = 1
                sum_ -= 10
            else:
                carry = 0
            l.val = sum_
            rev1 = rev1.next if rev1 else None
            rev2 = rev2.next if rev2 else None
            if rev1 or rev2:
                l.next = ListNode(0)
            elif carry:
                l.next = ListNode(1)
            else:
                l.next = None
            l = l.next
        return ret

    # def reverseLink(self, l):
    #     prev = None
    #     node = None
    #     next_ = l
    #     while next_.next:
    #         prev = node
    #         node = next_
    #         next_ = next_.next
    #         node.next = prev
    #     next_.next = node
    #     return next_
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        carry = 0
        p = result
        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                p = p.next
        if carry:
            p.next = ListNode(carry)
        return result.next
