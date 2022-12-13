class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def nxt(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        print(result)
        return self


a = Fibonacci()
a.nxt()
a.nxt().nxt()
a.nxt().nxt().nxt()
a.nxt().nxt().nxt().nxt()
a.nxt().nxt().nxt().nxt().nxt()
a.nxt().nxt().nxt().nxt().nxt().nxt()

