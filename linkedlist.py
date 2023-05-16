class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self,value,):
        newNode= Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    # Push is used to add a node to the tail (end) of a list       
    def push(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self

    # Pop is used to remove a node at the tail (end) of a list
    def pop(self):
        if self.head is None:
            print ("Linked list is empty")
            return None 
        pre = self.head
        current = self.head
        while current.next:
            pre=current
            current=current.next
        self.tail =  pre
        self.tail.next =  None
        self.length -= 1
        if self.length == 1:
            self.head = None
            self.tail = None
        return current

    # Unshift is similar to push but this time you are adding the new node before the head of the list. 

    def unshift (self,data):
        newNode = Node (data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self

    def shift (self):
        if self.head is None:
            print ("Linked List is Empty")
            return None
        current = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 1:
            self.tail = None
        current.next = None
        return current

    
            
# Reverse is used to turn the head of a linked list and to reverse the direction of the flow.

    def reverse (self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        next = temp.next
        prev = None

        for x in range (self.length):
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next

        return self
        
    def reverse2(self):
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
        return self
    
    


#Print method for printing

    def print(self):
        temp = self.head
        while(temp):
            print (temp.data,end="")
            temp = temp.next

newlist1 = Linkedlist("MONDAY")
newlist1.push("TUESDAY")
newlist1.push("WEDNESDAY")
newlist1.push("THURSDAY")
newlist1.push("FRIDAY")
newlist1.pop()
newlist1.print()
list2 = newlist1.reverse()
print("\n")
print("Reverse Linked List")
print("\n")
list2.print()
print("\n")
list3 = newlist1.reverse2()
def compare_linked_lists(llist1, llist2):
    temp1 = llist1.head
    temp2 = llist2.head
    while(temp1 and temp2):
        if temp1.data != temp2.data:
            return False
        temp1 = temp1.next
        temp2 = temp2.next
    if not temp1 and not temp2:
        return True
    return False

result = compare_linked_lists(newlist1, list3)
print(result) # This will print True if both the linked lists have equal node values, False otherwise.





#Palindrome Linked List
#class Solution(object):
 #   def isPalindrome(self, head):
  #      """
   #     :type head: ListNode
    #    :rtype: bool
#        """
#begin = head
#newArray = []
#while head:
 #   newArray.append(head.val)
  #  head= head.next

#i = -1
#while begin:
 #   if begin.val == newArray[i]:
  #      i -= 1
   #     begin = begin.next
    #else:
     #   return False

#return True
