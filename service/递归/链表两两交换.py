class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        else:
            first_node = head.next
            second_node = head
            second_node.next = self.swapPairs(first_node.next)
            first_node.next = second_node
            return first_node


node1 = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(4)
node4 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4

node = Solution().swapPairs(node1)
while node.next:
    print(node.val)
    node = node.next
print(node.val)