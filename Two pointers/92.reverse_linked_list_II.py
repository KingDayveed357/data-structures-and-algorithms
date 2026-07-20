class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        current = prev.next
        tail = current

        previous = None

        for _ in range(right - left + 1):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        prev.next = previous
        tail.next = current

        return dummy.next

def build_linked_list(array):
    dummy = ListNode()
    curr = dummy

    for val in array:
        curr.next = ListNode(val)
        curr = curr.next

    return dummy.next

def print_list(head):
    curr = head

    while curr:
        print(curr.val, end="->" if curr.next else "")
        curr = curr.next
    print()


if __name__ == "__main__":
    my_solution = Solution()
    left = 2
    right = 4
    head = build_linked_list([1, 2, 3, 4, 5, 6])
    reverseBetween = my_solution.reverseBetween(head, left, right)
    print_list(reverseBetween)
