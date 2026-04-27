"""
Stack using Linked List in Python

Stack is a linear data structure that follows LIFO principle:
LIFO = Last In First Out

The last inserted element will be removed first.

In Linked List Stack:
- top points to the first node

OPERATIONS:
1. Push    : Insert element at top
2. Pop     : Remove top element
3. Peek    : View top element
4. IsEmpty : Check stack empty or not
5. Display : Show stack elements
6. Exit    : Stop program

ADVANTAGE:
Stack size is dynamic (no fixed size)

TIME COMPLEXITY:
Push    : O(1)
Pop     : O(1)
Peek    : O(1)
Display : O(n)
"""

# Node creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack using Linked List
class Stack:
    def __init__(self):
        self.top = None

    # Push element
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    # Pop element
    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return

        temp = self.top
        self.top = self.top.next
        print("Popped element:", temp.data)

    # Peek top element
    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return
        return self.top.data

    # Check empty
    def isempty(self):
        return self.top is None

    # Display stack
    def display(self):
        temp = self.top

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
s = Stack()

print("Stack Operations")

while True:
    print("\n1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.IsEmpty")
    print("5.Display")
    print("6.Exit")

    choice = int(input("Enter choice 1/2/3/4/5/6: "))

    if choice == 1:
        s.push(int(input("Enter a number: ")))

    elif choice == 2:
        s.pop()

    elif choice == 3:
        print("Top element:", s.peek())

    elif choice == 4:
        print(s.isempty())

    elif choice == 5:
        s.display()

    elif choice == 6:
        print("Done")
        break

    else:
        print("Invalid choice")