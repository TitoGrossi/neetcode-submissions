from dataclasses import dataclass
from typing import Optional


class Deque:

    @dataclass
    class Node:
        value: int
        previous: Optional["Deque.Node"] = None
        next: Optional["Deque.Node"] = None

    def __init__(self):
        self.head: Optional["Deque.Node"] = None
        self.tail: Optional["Deque.Node"] = None

    def isEmpty(self) -> bool:
        return self.head is None

    def append(self, value: int) -> None:
        node = Deque.Node(value)

        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

    def appendleft(self, value: int) -> None:
        node = Deque.Node(value)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node

    def pop(self) -> int:
        if not self.tail:
            return -1

        value = self.tail.value

        if self.head is self.tail:
            self.head, self.tail = None, None
        else:
            self.tail.previous.next = None
            self.tail = self.tail.previous

        return value

    def popleft(self) -> int:
        if not self.head:
            return -1

        value = self.head.value

        if self.head is self.tail:
            self.head, self.tail = None, None
        else:
            self.head.next.previous = None
            self.head = self.head.next

        return value
