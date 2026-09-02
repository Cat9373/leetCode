class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nodesBetweenCriticalPoints(head):

    if head is None or head.next is None or head.next.next is None:
        return [-1, -1]

    prev = head
    curr = head.next

    index = 1

    first = -1
    last = -1

    minDist = float('inf')
    maxDist = -1

    while curr.next:

        next_node = curr.next

        # Local maximum
        is_max = curr.val > prev.val and curr.val > next_node.val

        # Local minimum
        is_min = curr.val < prev.val and curr.val < next_node.val

        if is_max or is_min:

            if first == -1:
                # First critical point
                first = index
            else:
                # Distance from previous critical point
                minDist = min(minDist, index - last)

                # Distance from first critical point
                maxDist = index - first

            last = index

        prev = curr
        curr = next_node
        index += 1

    if first == -1 or first == last:
        return [-1, -1]

    return [minDist, maxDist]


# Helper function to create a linked list
def create_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# Examples

head = create_list([3, 1])
print(nodesBetweenCriticalPoints(head))
# [-1, -1]

head = create_list([5, 3, 1, 2, 5, 1, 2])
print(nodesBetweenCriticalPoints(head))
# [1, 3]

head = create_list([1, 3, 2, 2, 3, 2, 2, 2, 7])
print(nodesBetweenCriticalPoints(head))
# [3, 3]