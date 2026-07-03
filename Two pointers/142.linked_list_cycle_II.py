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

def print_list(head, limit=20):
    if head is None:
        print("Empty List")
        return

    seen = set()
    curr = head
    count = 0
    output = []
    while curr and curr not in seen and count < limit:
        seen.add(curr)
        output.append(str(curr.val))
        curr = curr.next
        count += 1

    if curr is None:
        output.append("None")
        print(" -> ".join(output))
    else:
        output.append(f"(cycle back to {curr.val})")
        print(" -> ".join(output))


# ---------- Test code ----------
if __name__ == "__main__":
    sol = Solution()

    print("=== Test cases for 142. Linked List Cycle II ===")

    # 1. List with cycle (pos = 1) – expected cycle start value 2
    head1 = build_list_with_cycle([3, 2, 0, -4], pos=1)
    print("List 1:", end=" ")
    print_list(head1)
    start = sol.detectCycle(head1)
    if start:
        print("Cycle starts at node with value:", start.val)  # Expected: 2
    else:
        print("No cycle")
    print()

    # 2. List without cycle (pos = -1)
    head2 = build_list_with_cycle([1, 2, 3, 4, 5], pos=-1)
    print("List 2:", end=" ")
    print_list(head2)
    start2 = sol.detectCycle(head2)
    if start2:
        print("Cycle starts at node with value:", start2.val)
    else:
        print("No cycle (correct)")  # Expected: No cycle
    print()

    # 3. Single node with self‑loop (pos = 0) – expected start value 1
    head3 = build_list_with_cycle([1], pos=0)
    print("List 3:", end=" ")
    print_list(head3)
    start3 = sol.detectCycle(head3)
    if start3:
        print("Cycle starts at node with value:", start3.val)  # Expected: 1
    else:
        print("No cycle")
    print()

    # 4. Empty list
    head4 = build_list_with_cycle([], pos=-1)
    print("List 4: Empty list")
    start4 = sol.detectCycle(head4)
    if start4:
        print("Cycle starts at node with value:", start4.val)
    else:
        print("No cycle (correct)")









