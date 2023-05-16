class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    #INSERT
    def insert (self, value = None):
        newNode = Node (value)
        if self.root is None:
            self.root = newNode
            return self
        temp = self.root
        while True:
            if newNode.value == temp.value:
                return None
            if newNode.value < temp.value:
                if temp.left is None:
                    temp.left = newNode
                    return self
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newNode
                    return self
                temp =  temp.right
    #SEARCH
    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    #MINIMUM VALUE
    def minValueNode(self, currentNode):
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode.value

    #PRINT
    def print(self):
        leftValue = self.root.left
        rightValue= self.root.right
        lefts = "left values: "
        rights = "right values: "

        while leftValue:
            lefts += str(leftValue.value) + "->"
            leftValue = leftValue.left

        while rightValue:
            rights += str(rightValue.value) + "->"
            rightValue = rightValue.right

        print ('root: ' + str(self.root.value) + ' ' + lefts + ' ' + rights)

newTree = BST()
newTree.insert(20)
newTree.insert(50)
newTree.insert(10)
newTree.insert(5)
newTree.insert(100)
newTree.print()
print(newTree.minValueNode(newTree.root.left))