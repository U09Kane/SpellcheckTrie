from collections import deque

# ===== Balanced Delimiters ================================================= #

def is_matched(expression):
    stack = deque()
    for i in expression:

        if is_opening_term(i):
            stack.append(i)

        else:
            if len(stack) == 0 or not match(stack.pop(), i):
                return False

    if len(stack) == 0: return True
    return False
    
def match(left, right):
    limiters = {'{':'}', '[':']', '(':')'}
    if limiters[left] == right:
        return True

    else: return False

def is_opening_term(term):
    if term in ['{', '[', '(']:
        return True

    else: return False


# ===== Two Stacks = Queue ================================================== #

class Queue:

    def __init__(self):
        self.main_stack = deque()
        self.buffer_stack = deque()

    def dequeue(self):
        return self.main_stack.pop()

    def enqueue(self, *args):

        for arg in args:
            # Move everything to buffer stack
            while self.main_stack: # while not empty
                self.buffer_stack.append(self.main_stack.pop())

            self.main_stack.append(arg)

            while self.buffer_stack:
                self.main_stack.append(self.buffer_stack.pop())

# ===== Heaps =============================================================== #

class Min_Heap:
    '''Class to constuct and modify a Min Heap

    Uses a standard list to minimize overhead compared to a node class
    '''

    def __init__(self):
        self.items = items = []

    def swap(self, index_one, index_two):
        self.items[index_one], self.items[index_two] = self.items[index_two], self.items[index_one]

    def peek(index=0):
        if len(self.items) == 0:
            return
        else:
            return self.items[index]

    def insert(value, index=0):
        if self.peek(index)



