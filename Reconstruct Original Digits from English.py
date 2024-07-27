class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)
        total_chars = len(s)
        digits = []
        if c["z"] != 0:
            count = c["z"]
            for i in range(count):
                digits.append("0")
            c["z"] -= count
            c["e"] -= count
            c["r"] -= count
            c["o"] -= count
        if c["w"] != 0:
            count = c["w"]
            for i in range(count):
                digits.append("2")
            c["t"] -= count
            c["w"] -= count
            c["o"] -= count
        if c["u"] != 0:
            count = c["u"]
            for i in range(count):
                digits.append("4")
            c["f"] -= count
            c["o"] -= count
            c["u"] -= count
            c["r"] -= count
        if c["x"] != 0:
            count = c["x"]
            for i in range(count):
                digits.append("6")
            c["s"] -= count
            c["i"] -= count
            c["x"] -= count
        if c["s"] != 0:
            count = c["s"]
            for i in range(count):
                digits.append("7")
            c["s"] -= count
            c["e"] -= 2 * count
            c["v"] -= count
            c["n"] -= count
        if c["o"] != 0:
            count = c["o"]
            for i in range(count):
                digits.append("1")
            c["o"] -= count
            c["n"] -= count
            c["e"] -= count
        if c["v"] != 0:
            count = c["v"]
            for i in range(count):
                digits.append("5")
            c["f"] -= count
            c["i"] -= count
            c["v"] -= count
            c["e"] -= count
        if c["r"] != 0:
            count = c["r"]
            for i in range(count):
                digits.append("3")
            c["r"] -= count
            c["t"] -= count
            c["h"] -= count
            c["e"] -= 2 * count
        if c["h"] != 0:
            count = c["h"]
            for i in range(count):
                digits.append("8")
            c["e"] -= count
            c["i"] -= count
            c["g"] -= count
            c["h"] -= count
            c["t"] -= count
        if c["n"] != 0:
            count = c["i"]
            for i in range(count):
                digits.append("9")
            c["n"] -= 2 * count
            c["i"] -= count
            c["e"] -= count
        digits.sort()
        return "".join(digits)