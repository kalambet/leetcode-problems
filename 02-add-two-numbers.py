__author__ = 'kalambet'

# Accepted: false

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        result = None
        current_node = None
        inc_by_10 = 0

        current_l1 = l1
        current_l2 = l2

        while current_l1 is not None and current_l2 is not None:
            val = current_l1.val + current_l2.val + inc_by_10
            if inc_by_10 is not 0:
                inc_by_10 = 0

            if val >= 10:
                val %= 10
                inc_by_10 = 1

            current_l1 = current_l1.next
            current_l2 = current_l2.next

            new_node = ListNode(val)

            # Set result
            if result is None:
                result = new_node

            if current_node is None:
                current_node = new_node
            else:
                current_node.next = new_node

        return result

sol = Solution();

node1 = None
firstList = node1
for i in range(0, 3):
    new_node1 = ListNode(2 + i)

    node1 = node1.next

print node1