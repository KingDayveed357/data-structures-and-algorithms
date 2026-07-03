from typing import Optional

class ListNode:
    def __init__(self, val: int=0, next: "ListNode"=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head):
        if head is None:
            return None

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None

def build_list(arr):
    dummy = ListNode()
    curr = dummy

    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next

def build_list_with_cycle(arr, pos):
    if not arr:
        return None

    head = build_list(arr)
    if pos == -1:
        return head

    tail = head
    cycle_node = None
    index = 0

    while tail.next:
        if index == pos:
            cycle_node = tail
        tail = tail.next
        index += 1

    if index == pos:
        cycle_node = tail
    if cycle_node is not None:
        tail.next = cycle_node
    return head

def print_list(head, limit=20)







