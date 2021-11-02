#min stack

class max_s:
    min_stack = []
    stack = []

    def push(self, item):
        if not self.min_stack:
            self.min_stack.append(item)

        self.stack.append(item)
        if item < self.min_stack[-1]:
            self.min_stack.append(item)
        else:
            self.min_stack.append(self.min_stack[-1])

        return True

    def pop(self):
        item = self.stack.pop()
        self.min_stack.pop()
        return item

    def get_min(self):
        return self.min_stack[-1]



stack = max_s()
stack.push(3)
stack.push(5)
stack.push(2)
print(stack.get_min())
