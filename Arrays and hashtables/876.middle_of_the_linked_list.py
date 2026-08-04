class ListNode:
    def __init__(self, val=0, next=None):
        self.val= val
        self.next = next

class Solution:
    def middleNode(self,head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

def build_list(arr):
    dummy = ListNode()
    curr = dummy

    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")




solution = Solution()
head = build_list([1, 2, 3, 4, 5])
middle = solution.middleNode(head)
print_list(middle)
