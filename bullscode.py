

class BullsCode:
    def __init__(self, code):
        self.code = code

    def check(self, bullcodes):
        count_b = 0
        count_c = 0
        d = {}

        for i in range(4):
            if self.code[i] == bullcodes.code[i]:
                count_b += 1
            else:
                if self.code[i] in d:
                    d[self.code[i]] += 1
                else:
                    d[self.code[i]] = 1

        for i in range(4):
            if (
                self.code[i] != bullcodes.code[i]
                and bullcodes.code[i] in d
                and d[bullcodes.code[i]] > 0
            ):
                count_c += 1

        return ["B"] * count_b + ["C"] * count_c
