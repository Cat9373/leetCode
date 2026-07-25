# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

        return dummy.next


# ---------- Helper Functions ----------

def createLinkedList(arr):
    dummy = ListNode()
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


def printLinkedList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# ---------- Driver Code ----------

l1 = list(map(int, input("Enter first number (space separated): ").split()))
l2 = list(map(int, input("Enter second number (space separated): ").split()))

head1 = createLinkedList(l1)
head2 = createLinkedList(l2)

obj = Solution()
result = obj.addTwoNumbers(head1, head2)

print("Result Linked List:")
printLinkedList(result)