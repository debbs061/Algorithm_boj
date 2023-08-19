from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.existMap = defaultdict(int)
        self.groupMap = defaultdict(list)
        self.maxGroupNum = 1

    def push(self, val: int) -> None:
        # 1. existMap 에 해당 value 가 있냐?
        self.existMap[val] += 1
        curGroupNum = self.existMap[val]
        # 2. groupMap 에 넣어준다.
        self.groupMap[curGroupNum].append(val)
        # 3. maxGroupNum 트래킹
        self.maxGroupNum = max(self.maxGroupNum, curGroupNum)

    def pop(self) -> int:
        # 1. groupMap[maxGroupNum][-1] return
        val = self.groupMap[self.maxGroupNum].pop()
        # 2. len(groupMap[maxGroupNum]) == 0 이면, maxGroupNum -= 1 해준다.
        if len(self.groupMap[self.maxGroupNum]) == 0:
            self.maxGroupNum -= 1
        self.existMap[val] -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
