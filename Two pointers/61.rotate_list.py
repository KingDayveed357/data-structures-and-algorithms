class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotate_list(self, head, k):
        # Empty List, one node or no rotation
        if not head or not head.next or k == 0:
            return head

        #Step1: Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        #Step2: Reduce unnecessary rotations
        k %= length

        if k == 0:
            return head

        #Step3: Make the list circular
        tail.next = head

        #Step4: Find the new tail
        steps = length - k - 1

        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next

        #Step5: New head
        new_head = new_tail.next

        #Step6: Break the circle
        new_tail.next = None

        return new_head


def build_list(arr):
        dummy = ListNode()
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next

def print_list(node):
        while node:
            print(node.val, end='->')
            node =  node.next
        print("None")


if __name__ == "__main__":
    solution = Solution()
    k = 2
    head = build_list([1,2,3,4,5])
    rotate = solution.rotate_list(head, k)
    print_list(rotate)