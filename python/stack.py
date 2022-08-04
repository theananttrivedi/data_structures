class Stack(object):
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1
        # top is actually the index of the topmost element
        # us it directly to access element of arr

    def push(self, value):
        if self.isFull():
            print("Stack Overflow - Insertion not possible!")
        else:
            print(f"Added {value} to Stack")
            self.top += 1
            self.arr[self.top] = value

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.arr[self.top]

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty - Cannot Remove Element from Empty Stack")
        else:
            print("Removing Top Element from Stack")
            top_element = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return top_element

    def size(self):
        return self.top + 1

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity


# For furthur improvements, try replacing the print
# with error, maybe test it


stack = Stack(5)
print(stack.isFull())
print(stack.isEmpty())
stack.push(4)
stack.push(50)
print(stack.peek())
print(stack.size())
print(stack.isEmpty())
stack.push(2)
stack.push(18)
stack.pop()
print(stack.isFull())
stack.push(100)
print(stack.isEmpty())
print(stack.isFull())
