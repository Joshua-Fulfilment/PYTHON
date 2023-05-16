#The Stack is a bit similar to the linkedlist.
#The Stack only allows operations from one end only. Insertion (PUSH) and Deletion (POP) can only be done from the top

#THE NODE CONSTRUCTOR
class Node:
    def __init__ (self, value=None, next=None):
        self.value = value
        self.next = next

#THE STACK CONSTRUCTOR
class Stack:
    def __init__ (self, value):
        newNode = Node (value)
        self.top = newNode
        self.length = 1

#THE PRINT STACK
    def printStack(self,):
        temp = self.top
        while temp:
            print(temp.value, end=" ")
            temp = temp.next

#THE getTop FUNCTION
    def getTop(self):
        if self.top is None:
            print ("Top: Null")
        else: 
            print ("Top: " + self.top.value)

#THE getLength FUNCTION
    def getLength(self):
        print ("Length: " + self.length)

#MAKE EMPTY FUNCTION i.e EMPTY STACK
    def makeEmpty(self):
        self.top = None
        self.length = 0

#N.B: The above functions are the UTILITY FUNCTIONS

#PUSH i.e. Insert at the top of the stack

    def push (self,value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top =  newNode
        self.length += 1
        return self

#POP i.e. Remove from the top

    def pop (self):
        if self.length == 0:
            return None

        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1
        
        return temp

myStack = Stack(4)

myStack.printStack()

print("\n")

myStack.push(5)

myStack.printStack()

print("\n")

myStack.push(20)

myStack.printStack()

print("\n")

myStack.pop()

myStack.printStack()


#QUEUE

#THE QUEUE CONSTRUCTOR
class Queue:
    def __init__(self, value):
        newNode = Node (value)
        self.first = newNode
        self.last = newNode
        self.length =1

#PRINT QUEUE
    def printQueue(self):
        temp = self.first
        while temp:
            print (temp.value, end=" ")
            temp = temp.next

#getFirst FUNCTION
    def getFirst(self):
        if self.first is None:
            print("First: null")
        else:
            print("First: " + self.first.value)

#getLast FUNCTION
    def getLast (self):
        if self.last is None:
            print ("Last: null")
        else: 
            print ("Last: " + self.last.value)

#getLength FUNCTION
    def getLength (self):
        print("Length: " + self.length)

#Make Empty Function i.e. EMPTY QUEUE
    def makeEmpty(self):
        self.first = None
        self.last = None
        self.length = 0

#ENQUEUE FUNCTION i.e. To insert an element into a queue
    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return self

#DEQUEUE FUNCTION i.e. To remove a data from the queue
    def dequeue (self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

myQueue = Queue(4)

myQueue.printQueue()

print("\n")

myQueue.enqueue(5)

myQueue.printQueue()

print("\n")

myQueue.enqueue(20)

myQueue.printQueue()

print("\n")

myQueue.dequeue()

myQueue.printQueue()  