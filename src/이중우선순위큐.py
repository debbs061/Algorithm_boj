import heapq
from collections import defaultdict


def solution(operations):
    mapping = defaultdict(int)
    min_heap = []
    max_heap = []
    for op in operations:
        if op.startswith("I"):
            num = int(op[2:])
            mapping[num] += 1
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif op.startswith("D -1"):
            while min_heap:
                num = heapq.heappop(min_heap)
                if mapping[num] > 0:
                    mapping[num] -= 1
                    break
        else:
            while max_heap:
                num = -heapq.heappop(max_heap)
                if mapping[num] > 0:
                    mapping[num] -= 1
                    break

    if not min_heap or not max_heap:
        return [0, 0]

    # synchronize the min_heap and max_heap
    while mapping[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while mapping[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    return [-max_heap[0], min_heap[0]]
