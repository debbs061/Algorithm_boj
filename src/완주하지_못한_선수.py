def solution(participant, completion):
    answer = ''

    map = {}  # key: name, val: count
    for name in participant:
        map[name] = map.get(name, 0) + 1

    for name in completion:
        if name in map:
            map[name] -= 1
            if map[name] == 0:
                del map[name]

    return list(map.keys())[0]

