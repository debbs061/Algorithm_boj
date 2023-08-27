class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def recurse(op, i):
            alphaCnt = {'t': 0, 'f': 0}
            while expression[i] != ")":
                if expression[i] in ("&", "|", "!"):
                    subEva, i = recurse(expression[i], i + 1)
                    alphaCnt[subEva] += 1
                elif expression[i].isalpha():
                    alphaCnt[expression[i]] += 1
                i += 1

            # 최종 evaluation 진행
            if op == "&":
                return ['f', i] if alphaCnt['f'] > 0 else ['t', i]
            elif op == "|":
                return ['t', i] if alphaCnt['t'] > 0 else ['f', i]
            else:
                return ['f', i] if alphaCnt['t'] > 0 else ['t', i]

        return False if recurse(expression[0], 1)[0] == 'f' else True
