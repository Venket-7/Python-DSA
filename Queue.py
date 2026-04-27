"""
Queue using List in Python

Queue is a linear data structure that follows FIFO principle:
FIFO = First In First Out

The element inserted first will be removed first.

OPERATIONS:
1. Enqueue : Insert element at rear end
2. Dequeue : Remove element from front end
3. Display : Show all queue elements
4. Peek    : View front element
5. Exit    : Stop program

ALGORITHM:
STEP 1: Create an empty list for queue
STEP 2: Insert elements using append()
STEP 3: Remove front element using pop(0)
STEP 4: Display queue elements
STEP 5: Peek first element using q[0]
STEP 6: Repeat until user exits

TIME COMPLEXITY:
Enqueue : O(1)
Dequeue : O(n)   # because pop(0) shifts elements
Peek    : O(1)
Display : O(n)
"""

q = []

while True:
    print("\nQueue Operations")
    print("1. Enqueue operation")
    print("2. Dequeue operation")
    print("3. Display")
    print("4. Peek element")
    print("5. Exit")

    c = int(input("Enter choice 1/2/3/4/5: "))

    if c == 1:
        ele = int(input("Enter an element: "))
        q.append(ele)
        print("Queue after enqueue:", q)

    elif c == 2:
        if len(q) != 0:
            p = q.pop(0)
            print("Deleted element:", p)
            print("Queue is:", q)
        else:
            print("Queue is empty")

    elif c == 3:
        if len(q) != 0:
            print("Queue is:", q)
        else:
            print("Queue is empty")

    elif c == 4:
        if len(q) != 0:
            print("Front element is:", q[0])
        else:
            print("Queue is empty")

    elif c == 5:
        print("Done")
        break

    else:
        print("Invalid choice")