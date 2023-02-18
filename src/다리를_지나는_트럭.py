from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    total_weight = 0
    truck_weights = deque(truck_weights)
    on_bridge = deque([0] * bridge_length, maxlen=bridge_length)  # [0,0,0]

    while truck_weights:
        time += 1
        total_weight -= on_bridge.popleft()
        if total_weight + truck_weights[0] <= weight:
            truck_weight = truck_weights.popleft()
            on_bridge.append(truck_weight)
            total_weight += truck_weight
        else:
            on_bridge.append(0)

    time += bridge_length
    return time
