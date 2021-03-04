from heapq import heappush, heappop, heapify

class Node:
    def __init__(self, val, prev, next_node):
        self.val = val
        self.prev = prev
        self.next = next_node

    def __repr__(self):
        return str(self.val)

    def __lt__(self, other):
         return self.val < other.val

T = int(input(''))
for _ in range(T):
    ans = 0
    N = int(input(''))
    nums = list(map(int, input('').split()))
    nodes = []
    N = len(nums)
    q = []
    prev = None
    for i in range(N):
        nodes.append(Node(nums[i], None, None))

    max_val = float('-inf')
    for i in range(N):
        max_val = max(max_val, nums[i])
        if i + 1 < N:
            nodes[i].next = nodes[i + 1]
        if i > 0:
            nodes[i].prev = nodes[i - 1]

        heappush(q, nodes[i])

    while q and q[0].val < max_val:
        node = heappop(q)
        val = node.val
        prev_val, next_val = float('inf'), float('inf')
        # print(q, node.prev, node, node.next)
        if node.prev:
            prev_val = node.prev.val
        if node.next:
            next_val = node.next.val

        if prev_val < next_val:
            node.prev.val += val
            max_val = max(max_val, node.prev.val)
        else:
            node.next.val += val
            max_val = max(max_val, node.next.val)

        if node.prev:
            node.prev.next = node.next
        else:
            node.next.prev = None

        if node.next:
            node.next.prev = node.prev
        else:
            node.prev.next = None
        heapify(q)
        ans += 1

    print(ans)
