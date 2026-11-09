# ASSIGNMENT 1: STACK AND ITS REAL APPLICATIONS
# Course  : CSC 3xx - Data Structures
# Name    : ______________________
# Matric  : ______________________
# School  : Crawford University
#
# A stack is a LIFO structure (Last In, First Out).
# The last item pushed in is the first one that comes out,
# just like a pile of plates.
#
# REAL APPLICATIONS OF STACK (where it is operational)
# 1. Undo / Redo in text editors (MS Word, VS Code, Notepad)
# 2. Back button of a web browser (pages visited are pushed on a stack)
# 3. Checking balanced brackets in compilers  e.g. ( [ { } ] )
# 4. Function calls / recursion (the call stack in memory)
# 5. Reversing a word or string
# 6. Converting and evaluating expressions (infix to postfix)
#
# Below I made demos for 4 of them and then used an array of
# my class (10 students) to perform all the stack operations.


# ---------------- Stack class (array based) ----------------
class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size   # fixed size array
        self.top = -1              # -1 means stack is empty

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, item):
        if self.is_full():
            print("Stack Overflow! cannot push", item)
            return
        self.top += 1
        self.arr[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! stack is empty")
            return None
        item = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.arr[self.top]

    def count(self):
        return self.top + 1

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("TOP")
        for i in range(self.top, -1, -1):
            print("  |", self.arr[i], "|")
        print("BOTTOM")


# ---------------- Application 1: Undo in a text editor ----------------
def undo_demo():
    print("\n--- Application 1: Undo in a text editor ---")
    undo_stack = Stack(10)
    words = ["Hello", "my", "name", "is", "Tunde"]
    for w in words:
        undo_stack.push(w)
        print("Typed:", w)
    print("User presses Ctrl+Z twice")
    print("Removed:", undo_stack.pop())
    print("Removed:", undo_stack.pop())
    print("Text left in the editor:", undo_stack.arr[:undo_stack.count()])


# ---------------- Application 2: Browser back button ----------------
def browser_demo():
    print("\n--- Application 2: Browser back button ---")
    history = Stack(10)
    pages = ["google.com", "crawforduniversity.edu.ng", "portal.crawforduniversity.edu.ng"]
    for p in pages:
        history.push(p)
        print("Visited:", p)
    print("Currently on:", history.peek())
    history.pop()
    print("Clicked back, now on:", history.peek())


# ---------------- Application 3: Balanced brackets ----------------
def check_brackets(text):
    s = Stack(len(text) + 1)
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in text:
        if ch in "([{":
            s.push(ch)
        elif ch in ")]}":
            if s.is_empty():
                return False
            if s.pop() != pairs[ch]:
                return False
    return s.is_empty()


def bracket_demo():
    print("\n--- Application 3: Balanced brackets (compiler) ---")
    tests = ["(a + b) * [c - d]", "{[(1 + 2)]}", "(a + b]", "((x)"]
    for t in tests:
        if check_brackets(t):
            print(t, "-> Balanced")
        else:
            print(t, "-> Not balanced")


# ---------------- Application 4: Reverse a string ----------------
def reverse_word(word):
    s = Stack(len(word))
    for ch in word:
        s.push(ch)
    result = ""
    while not s.is_empty():
        result += s.pop()
    return result


def reverse_demo():
    print("\n--- Application 4: Reversing a string ---")
    w = "CRAWFORD"
    print(w, "reversed is", reverse_word(w))


# ---------------- Class array: all stack operations ----------------
def class_demo():
    print("\n--- Stack operations using my class array (size 10) ---")
    class_list = ["Ade", "Chioma", "Bola", "Emeka", "Fatima",
                  "Gbenga", "Hauwa", "Ife", "Joy", "Kemi"]
    print("Class array:", class_list)

    stack = Stack(len(class_list))

    print("\n1. isEmpty at the start:", stack.is_empty())

    print("\n2. PUSH the names one by one")
    for name in class_list:
        stack.push(name)
        print("pushed", name)

    print("\n3. DISPLAY")
    stack.display()

    print("\n4. isFull:", stack.is_full())
    print("5. Size of stack:", stack.count())

    print("\n6. Trying to push one more student (overflow test)")
    stack.push("Lola")

    print("\n7. PEEK (top element):", stack.peek())

    print("\n8. POP three times")
    for i in range(3):
        print("popped:", stack.pop())

    print("\n9. Stack after popping")
    stack.display()
    print("Size now:", stack.count())
    print("Top now:", stack.peek())

    print("\n10. Pop everything left (underflow test)")
    while not stack.is_empty():
        stack.pop()
    stack.pop()
    print("isEmpty:", stack.is_empty())


# ---------------- Main ----------------
def main():
    print("========== STACK ASSIGNMENT ==========")
    undo_demo()
    browser_demo()
    bracket_demo()
    reverse_demo()
    class_demo()
    print("\nEnd of program")


main()
