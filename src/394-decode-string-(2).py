class Solution:
    def decodeString(self, s: str) -> str:
        decoded = []

        def getRepeatNum(i):
            startNumIdx = i
            while s[i] != "[":
                i += 1
            return int(s[startNumIdx:i]), i

        def recurse(repeatNum, i):
            tmp = []
            while s[i] != "]":
                if s[i].isnumeric():
                    num, idx = getRepeatNum(i)
                    decodedStr, endIdx = recurse(num, idx + 1)
                    tmp.append(decodedStr)
                    i = endIdx + 1
                else:
                    tmp.append(s[i])
                    i += 1
            return [repeatNum * ("".join(tmp)), i]

        i = 0
        while i < len(s):
            if s[i].isnumeric():
                repeatNum, idx = getRepeatNum(i)
                decodedStr, endIdx = recurse(repeatNum, idx + 1)
                decoded.append(decodedStr)
                i = endIdx + 1  # 숫자가 있는 다음 index 로 이동
            else:
                decoded.append(s[i])
                i += 1

        return "".join(decoded)
