class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        """Add a node to the end of the list"""
        if not self.head:
            self.head = ListNode(val)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val)

    def get_node(self, index):
        """Get node at specific index (0-based)"""
        current = self.head
        count = 0
        while current and count < index:
            current = current.next
            count += 1
        return current

    def print_list(self):
        """Print the list for debugging"""
        current = self.head
        values = []
        while current:
            values.append(str(current.val))
            current = current.next
        print(" -> ".join(values) + " -> None")


def get_intersection_node(headA, headB):
    """
    Find the intersection node of two linked lists.
    Returns the intersecting node or None if no intersection.
    """
    if not headA or not headB:
        return None

    p1 = headA
    p2 = headB

    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA

    return p1


def create_intersecting_lists():
    """
    Helper function to create test lists with intersection.
    Returns (headA, headB, intersection_node)
    """
    # Create common nodes (intersection)
    c1 = ListNode(8)
    c2 = ListNode(4)
    c3 = ListNode(5)
    c1.next = c2
    c2.next = c3

    # Create list A: 4 -> 1 -> 8 -> 4 -> 5
    a1 = ListNode(4)
    a2 = ListNode(1)
    a1.next = a2
    a2.next = c1

    # Create list B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(1)
    b1.next = b2
    b2.next = b3
    b3.next = c1

    return a1, b1, c1


def create_non_intersecting_lists():
    """
    Helper function to create test lists with no intersection.
    Returns (headA, headB)
    """
    # List A: 1 -> 2 -> 3
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a1.next = a2
    a2.next = a3

    # List B: 4 -> 5 -> 6
    b1 = ListNode(4)
    b2 = ListNode(5)
    b3 = ListNode(6)
    b1.next = b2
    b2.next = b3

    return a1, b1


def main():
    """
    Test the solution with different scenarios
    """
    print("=" * 50)
    print("TEST 1: Intersecting Lists")
    print("=" * 50)

    headA, headB, intersection = create_intersecting_lists()

    print("List A:")
    LinkedList.print_list(None)  # We'll just use the helper
    # Print manually for clarity
    current = headA
    vals = []
    while current:
        vals.append(str(current.val))
        current = current.next
    print(" -> ".join(vals) + " -> None")

    print("List B:")
    current = headB
    vals = []
    while current:
        vals.append(str(current.val))
        current = current.next
    print(" -> ".join(vals) + " -> None")

    result = get_intersection_node(headA, headB)
    if result:
        print(f"\n✓ Intersection found at node with value: {result.val}")
        print(f"  (Expected intersection value: 8)")
    else:
        print("\n✗ No intersection found (incorrect)")

    print("\n" + "=" * 50)
    print("TEST 2: Non-Intersecting Lists")
    print("=" * 50)

    headA, headB = create_non_intersecting_lists()

    print("List A:")
    current = headA
    vals = []
    while current:
        vals.append(str(current.val))
        current = current.next
    print(" -> ".join(vals) + " -> None")

    print("List B:")
    current = headB
    vals = []
    while current:
        vals.append(str(current.val))
        current = current.next
    print(" -> ".join(vals) + " -> None")

    result = get_intersection_node(headA, headB)
    if result is None:
        print("\n✓ No intersection found (correct)")
    else:
        print(f"\n✗ Intersection incorrectly found at node: {result.val}")

    print("\n" + "=" * 50)
    print("TEST 3: Edge Cases")
    print("=" * 50)

    # Test with empty lists
    result = get_intersection_node(None, None)
    print(f"Both lists empty: {'✓' if result is None else '✗'}")

    # Test with one empty list
    headA, _ = create_non_intersecting_lists()
    result = get_intersection_node(headA, None)
    print(f"One list empty: {'✓' if result is None else '✗'}")


if __name__ == "__main__":
    main()