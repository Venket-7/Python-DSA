"""
Queue using Linked List in Python

Queue is a linear data structure that follows FIFO principle:
FIFO = First In First Out

The first inserted element will be removed first.

In Linked List Queue:
- front points to first node
- rear points to last node

OPERATIONS:
1. Enqueue : Insert element at rear
2. Dequeue : Delete element from front
3. Peek    : View front element
4. IsEmpty : Check queue empty or not
5. Display : Show queue elements
6. Exit    : Stop program

ADVANTAGE:
Queue size is dynamic (no fixed size)

TIME COMPLEXITY:
Enqueue : O(1)
Dequeue : O(1)
Peek    : O(1)
Display : O(n)
"""

# Node creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue creation using Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Insert element at rear
    def enqueue(self, data):
        node = Node(data)

        if self.rear is None:
            self.front = self.rear = node
            return

        self.rear.next = node
        self.rear = node

    # Delete element from front
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print("Deleted element:", temp.data)

    # View front element
    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return
        return self.front.data

    # Check queue empty
    def isempty(self):
        return self.front is None

    # Display queue elements
    def display(self):
        temp = self.front

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
c = Queue()

print("Queue Operations")

while True:
    print("\n1.Enqueue")
    print("2.Dequeue")
    print("3.Peek")
    print("4.IsEmpty")
    print("5.Display")
    print("6.Exit")

    choice = int(input("Enter choice 1/2/3/4/5/6: "))

    if choice == 1:
        c.enqueue(int(input("Enter a number: ")))

    elif choice == 2:
        c.dequeue()

    elif choice == 3:
        print("Front element:", c.peek())

    elif choice == 4:
        print(c.isempty())

    elif choice == 5:
        c.display()

    elif choice == 6:
        print("Done")
        break

    else:
        print("Invalid choice")