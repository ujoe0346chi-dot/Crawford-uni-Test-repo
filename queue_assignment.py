# ASSIGNMENT 2: QUEUE DATA STRUCTURE
# Course  : CSC 3xx - Data Structures
# Name    : ______________________
# Matric  : ______________________
# School  : Crawford University
#
# A queue is a FIFO structure (First In, First Out).
# The first person to join is the first to be served,
# like students lining up at the cafeteria.
#
# I used a circular array so that empty spaces at the front
# can be used again after dequeue.
#
# Operations: enqueue, dequeue, front, rear, isEmpty, isFull,
#             size, display and clear


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0       # index of the first element
        self.rear = -1       # index of the last element
        self.length = 0      # number of elements in the queue

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow! queue is full, cannot add", item)
            return
        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = item
        self.length += 1
        print(item, "has joined the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! queue is empty")
            return None
        item = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.length -= 1
        return item

    def peek_front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.arr[self.front]

    def peek_rear(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.arr[self.rear]

    def size(self):
        return self.length

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("FRONT -> ", end="")
        i = self.front
        for _ in range(self.length):
            print(self.arr[i], end=" ")
            i = (i + 1) % self.capacity
        print("<- REAR")

    def clear(self):
        self.arr = [None] * self.capacity
        self.front = 0
        self.rear = -1
        self.length = 0
        print("Queue has been cleared")


def menu():
    print("\n======== QUEUE MENU ========")
    print("1. Enqueue (add)")
    print("2. Dequeue (remove)")
    print("3. Front element")
    print("4. Rear element")
    print("5. Check if empty")
    print("6. Check if full")
    print("7. Size of queue")
    print("8. Display queue")
    print("9. Clear queue")
    print("0. Exit")


def main():
    print("Welcome to my Queue program")
    try:
        cap = int(input("Enter the size of the queue: "))
        if cap <= 0:
            print("Size must be more than 0, using 5 instead")
            cap = 5
    except ValueError:
        print("That is not a number, using 5 instead")
        cap = 5

    q = Queue(cap)

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            item = input("Enter item to add: ")
            q.enqueue(item)
        elif choice == "2":
            item = q.dequeue()
            if item is not None:
                print("Removed:", item)
        elif choice == "3":
            item = q.peek_front()
            if item is not None:
                print("Front element is", item)
        elif choice == "4":
            item = q.peek_rear()
            if item is not None:
                print("Rear element is", item)
        elif choice == "5":
            print("Queue is empty" if q.is_empty() else "Queue is not empty")
        elif choice == "6":
            print("Queue is full" if q.is_full() else "Queue is not full")
        elif choice == "7":
            print("Number of items in queue:", q.size())
        elif choice == "8":
            q.display()
        elif choice == "9":
            q.clear()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again")


main()
