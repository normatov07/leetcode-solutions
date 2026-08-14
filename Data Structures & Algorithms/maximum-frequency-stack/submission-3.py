class FreqStack:

    def __init__(self):
        self.stack = {}
        self.id = 1

    def push(self, val: int) -> None:
        if val not in self.stack:
            self.stack[val] = []

        self.stack[val].append(self.id)
        self.id += 1        

    def pop(self) -> int:
        max_k, max_id, max_v = 0, -1, -1

        for key, value in self.stack.items():
            if max_v < len(value) or (max_id < value[-1] and max_v == len(value)):
                max_k, max_id, max_v = key, value[-1], len(value)
        
        self.stack[max_k].pop()

        if not self.stack[max_k]:
            self.stack.pop(max_k)

        return max_k


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()