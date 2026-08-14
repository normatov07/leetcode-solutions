class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.stack = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.max_freq = max(self.freq[val], self.max_freq)
        self.stack[self.freq[val]].append(val)    

    def pop(self) -> int:
        res = self.stack[self.max_freq].pop()
        self.freq[res] -= 1

        if not self.stack[self.max_freq]:
            self.max_freq -= 1

        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()