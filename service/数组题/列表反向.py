class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printListFromTailToHead(listNode):
    # write code here
    if listNode == {} or listNode == None:
        return []
    array_list = []
    while listNode.next != None:
        array_list.insert(0, listNode.val)
        listNode = listNode.next
    array_list.insert(0, listNode.val)
    return array_list

node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

print(printListFromTailToHead(node1))