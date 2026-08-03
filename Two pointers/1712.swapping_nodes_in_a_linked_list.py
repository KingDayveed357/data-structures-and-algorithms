class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def bruteForceSwapNodes(self, head, k):
         nodes = []
         current = head

         while current:
             nodes.append(current)
             current = current.next

         left = nodes[k - 1]
         right = nodes[len(nodes) - k]

         left.val , right.val = right.val, left.val
         return head


    def optimalSwapNodes(self, head, k):
        front = head
        for _ in range(k - 1):
            front = front.next

        fast , back = front, head
        while fast.next:
            fast = fast.next

        front.val, back.val = back.val, front.val
        return head

def build_list(array):
    curr = dummy = ListNode()

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
    head = build_list([1, 2, 3, 1])
    k = 2
    swap_nodes = solution.bruteForceSwapNodes(head, k)
    print_list(swap_nodes)


