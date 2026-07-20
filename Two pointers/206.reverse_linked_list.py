class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        previous = None
        current = head

        while current:
            #Save the node after the current node
            next_node = current.next

            # Reverse the node
            current.next = previous

            # Move the previous node one step ahead
            previous = current

            # Move to the next node as your new current node
            current = next_node

        # Previous is now your new head
        return previous


def build_linked_list(array):
    dummy = ListNode()
    current = dummy

    for val in array:
        current.next = ListNode(val)
        current = current.next

    return dummy.next

def print_list(head):
    current = head

    while current:
        print(current.val, end="->" if current.next else "")
        current = current.next
    print()

if __name__ == "__main__":
    my_solution = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    reverseList = my_solution.reverseList(head)
    print_list(reverseList)



