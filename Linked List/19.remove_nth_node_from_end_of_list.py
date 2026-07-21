class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def bruteForce(self, head, n:int):
        dummy = ListNode(0, head)
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        current = dummy

        for _ in range(length - n):
            current = current.next
        current.next = current.next.next

        return dummy.next


    def Optimal(self, head, n:int):
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next




def build_linked_list(array):
    current = dummy = ListNode()

    for val in array:
        current.next = ListNode(val)
        current = current.next

    return dummy.next

def print_list(head):
    curr = head

    while curr:
        print(curr.val, end="->" if curr.next else "")
        curr = curr.next
    print()


if __name__ == "__main__":
    my_solution = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    n = 2
    removeNthNodeFromEnd = my_solution.Optimal(head, n)
    print_list(removeNthNodeFromEnd)