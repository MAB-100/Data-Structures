import sys

class StackWithMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def Push(self, value):
        self.stack.append(value)
        if not self.max_stack:
            self.max_stack.append(value)
        else:
            # Push the maximum value between current value and the current top of max_stack
            self.max_stack.append(max(value, self.max_stack[-1]))

    def Pop(self):
        if self.stack:
            self.stack.pop()
            self.max_stack.pop()

    def Max(self):
        if self.max_stack:
            return self.max_stack[-1]
        return None  # Just a fallback; this should not happen as per problem constraints

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    
    num_queries = int(data[0])
    stack = StackWithMax()
    
    output = []
    for i in range(1, num_queries + 1):
        query = data[i].split()
        
        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            output.append(stack.Max())
    
    sys.stdout.write("\n".join(map(str, output)) + "\n")
