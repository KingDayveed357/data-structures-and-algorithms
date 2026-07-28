class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow, fast = head, head.next

        while fast and  fast.next:
            slow = slow.next
            fast = fast.next.next

        second_list = self.reverseList(slow.next)

        p1, p2 = head, second_list
        isPalindrome = True

        while isPalindrome and p2:
            if p1.val != p2.val:
                isPalindrome = False
            p1 = p1.next
            p2 = p2.next

        slow.next = self.reverseList(second_list)

        return isPalindrome



    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


def build_list(array):
    dummy = ListNode()
    curr = dummy

    for num in array:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

if __name__ == "__main__":
    solution = Solution()
    head = build_list([1, 2])
    palindrome = solution.isPalindrome(head)
    print(f"isPalindrome: {palindrome}")
    print("List after function call: ", end="")
    print_list(head)