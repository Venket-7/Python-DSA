"""
Stack using List in Python

Stack is a linear data structure that follows LIFO principle:
LIFO = Last In First Out

The last inserted element will be removed first.

Python list can be used as stack.

OPERATIONS:
1. Push    : Insert element at top
2. Pop     : Remove top element
3. Peek    : View top element
4. Display : Show stack elements
5. Exit    : Stop program

ALGORITHM:
STEP 1: Create empty list as stack
STEP 2: Push using append()
STEP 3: Pop using pop()
STEP 4: Peek using stack[-1]
STEP 5: Display stack
STEP 6: Repeat until exit

TIME COMPLEXITY:
Push    : O(1)
Pop     : O(1)
Peek    : O(1)
Display : O(n)
"""

stack = []

while True:
    print("\nStack Operations")
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")

    choice = input("Enter your choice: ")

    # Push operation
    if choice == "1":
        num = int(input("Enter a number: "))
        stack.append(num)
        print("Element pushed")
        print("Your stack is:", stack)

    # Pop operation
    elif choice == "2":
        if stack:
            removed = stack.pop()
            print("Popped element:", removed)
            print("Your stack is:", stack)
        else:
            print("Stack is empty")

    # Peek operation
    elif choice == "3":
        if stack:
            print("Top element is:", stack[-1])
        else:
            print("Stack is empty")

    # Display operation
    elif choice == "4":
        print("Your stack is:", stack)

    # Exit
    elif choice == "5":
        print("Done")
        break

    else:
        print("Invalid choice")