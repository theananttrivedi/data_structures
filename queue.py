class Queue(object):
    def __init__(self):
        self.elements = []

    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        return self.elements.pop(0)

    def rear(self):
        return self.elements[-1]

    def front(self):
        return self.elements[0]

    def is_empty(self):
        return len(self.elements) == 0
