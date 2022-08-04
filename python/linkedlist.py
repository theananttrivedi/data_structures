# If the next_node = None, it means that the element is the tail
# and thus no element is after it and thus it points to an empty node

# If the prev_node is = None in a doubly linked list it means that the element
# is the head an hence cannot point to a previous element
class Node(object):
    """
    :value int
    :next_node Node
    :prev_node Node
    ->
    """

    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList(object):
    def __init__(self, values=None):
        self.head = None
        self.tail = None

        if values is not None:
            self.add_multiple_nodes(values)

    def add_node(self, value):
        if self.head is None:
            # means the linked list is empty
            self.head = self.tail = Node(value)
        else:
            self.tail.next_node = Node(value)
            self.tail = self.tail.next_node
        return self.tail

    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)

    def add_node_as_head(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.head = Node(value, next_node=self.head)
        return self.head

    def __str__(self):
        # This self will only act as an iterator when the __iter__ is implemented
        return ' -> '.join([str(node) for node in self])

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next_node
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next_node

    @property
    def values(self):
        # self is nothing but instance of this class
        return [node.value for node in self]


class DoublyLinkedList(LinkedList):
    def add_node(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next_node = Node(value, None, prev_node=self.tail)
            self.tail = self.tail.next_node
        return self.tail

    def add_node_as_head(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.head.prev_node = Node(
                value, next_node=self.head, prev_node=None)
            self.head = self.head.prev_node
        return self.head


ll = LinkedList([1, 2, 5, 7, 4, 8, 8, 10])
print(len(ll))
print(ll)
print(str(ll.values))
