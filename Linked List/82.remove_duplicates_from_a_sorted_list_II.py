from collections import Counter
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def bruteForce(self, head):
        freq = Counter()
        curr = head

        while curr:
            freq[curr.val] += 1
            curr = curr.next

        dummy = ListNode(0)
        tail = dummy
        curr = head

        while curr:
            if freq[curr.val] == 1:
                tail.next = curr
                tail = tail.next
            curr = curr.next

        tail.next = None
        return dummy.next

    def optimal(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy.next
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                duplicate = curr.val

                while curr and curr.val == duplicate:
                    curr = curr.next

                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummy.next



def build_list(arr):
    dummy = ListNode()
    curr = dummy

    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def print_list(node):
    curr = node

    while curr:
        print(curr.val, end="->" if curr.next else "")
        curr = curr.next
    print("None")

if __name__ == "__main__":
    solution = Solution()
    head = build_list([1, 2, 3, 3, 4, 4, 5])
    deleteDuplicatesBruteForce = solution.bruteForce(head)
    deleteDuplicatesOptimal = solution.optimal(head)
    print_list(deleteDuplicatesOptimal)
    print_list(deleteDuplicatesBruteForce)





