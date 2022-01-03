class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]

    def print(self):
        return self.stack

    def remove(self):
        if len(self.stack) <= 0:
            return ("No elements in the Stack")
        else:
            return self.stack.pop()

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
print(AStack.peek())

AStack.add("Fri")
AStack.add("Sar")
print(AStack.peek())

print(AStack.print())

print("-------------------\n")

AStack.remove()
print(AStack.print())


