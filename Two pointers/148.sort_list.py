class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp


        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left , right)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        tail = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

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
    solution = Solution()
    head = build_linked_list([4, 2, 1, 3])
    sortList = solution.sortList(head)
    print_list(sortList)


