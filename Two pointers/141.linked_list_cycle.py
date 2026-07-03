from typing import Optional

# Linked List Node
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode'=None):
        self.val = val
        self.next = next


# Solution for Linked List Cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


# Helper Functions
def build_list(arr):
    """ Build a linked list from a list of values (no cycle). """
    dummy = ListNode()
    curr = dummy

    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next

def build_list_with_cycle(arr, pos):
    """
    Build a linked list and create a cycle at the given position
    - arr: list of node values
    - pos: index (0-based) of the node that the tail points to
    Returns the head of the list
    """
    if not arr:
        return None

    #Build the list normally
    head = build_list(arr)

    #No cycle
    if pos == -1:
        return head

    # Find the tail and the node at index 'pos'
    tail = head
    cycle_node = None
    index = 0
    while tail.next:
        if index == pos:
            cycle_node = tail
        tail = tail.next
        index += 1
    # Check the last node as well
    if index == pos:
        cycle_node = tail

    # Connect tail to the cycle_node
    if cycle_node is not None:
        tail.next = cycle_node

    return head

def print_list(head, limit = 20):
    """
    Safely print the list stop if a cycle is detected or limit exceeded.
    """
    if head is None:
        print("Empty list")
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
        print("->".join(output))
    else:
        output.append(f"(cycle back to {curr.val})")
        print(" -> ".join(output))



# Run Test Cases
if __name__ == "__main__":
    my_solution = Solution()
    head1 = build_list_with_cycle([1, 2, 3, 4, 5], pos=1)
    print("List 1:", end=" ")
    print_list(head1)
    print("hasCycle:", my_solution.hasCycle(head1))
    print()

    head2 = build_list_with_cycle([1,2,3,4,5], pos=-1)
    print("List 2:", end=" ")
    print_list(head2)
    print("hasCycle:", my_solution.hasCycle(head2))
    print()


