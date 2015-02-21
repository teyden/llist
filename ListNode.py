class ListNode:
   def __init__(self, item, next):
      self.item = item
      self.next = next

class LinkedList:
   def __init__(self):
      "create an empty list"
      self.head = None
      self.tail = None
      self.size = 0

      
   def append(self, item):
      """
      Precondition: item is any Python object or type 
      Assumptions:  Empty list already initialized
      Postcondition: Adds a list node carrying item to
      the linked list
      """
      # Make new list node
      newListNode = ListNode(item, None)
      if self.head == None and self.tail == None: 
         self.head = newListNode
         self.tail = newListNode
      else:
         self.tail.next  = newListNode
         self.tail = newListNode
      self.size += 1
      
      
   def __str__(self):
      """
      Postcondition: Returns a string representing
      all the nodes in the linked list. If the list is empty,
      prints an empty list "[]"
      """
      if self.tail == None and self.head == None:
         return "[]"
      
      currNode = self.head
      l = []
      while currNode != None:
         l += [currNode.item]
         currNode = currNode.next
      return str(l)
   
   

   def __len__(self):
      """
      Postcondition: Returns the length of the
      linked list
      """
      return self.size
   
   def remove (self, i):
      if type(i) != type (1):
         raise TypeError, "Invalid input type; must be an int"
      if i < 0:
         raise ValueError, "Index must be non-negative"
      if (i > self.size):
         raise ValueError, "Index %d is " %i + "out of bounds"
      if (self.head == None):
         raise ValueError, "Cannot remove from empty list"
      
      try:
         currNode = self.head
         prevNode = None
         k = 0
         
         while (k != i) and (currNode != None):
            prevNode = currNode
            currNode = currNode.next
            k+= 1
            
         if (k == i):
            self.size -= 1
            item = currNode.item
            prevNode.next = currNode.next
            return item
         
      except Exception:
         raise IndexError, "Index %d not found " %(i)
      

      
      
   def pop(self, i):
      """
      Precondition: i is an int and 0 <= i <= self.size-1
      Postcondition: Removes the list node at the given index
      from the linked list and then returns the item in the node
      at the given index. If i > (length-1) then raise
      an IndexError
      """
      if self.size == 0:
         raise IndexError, "Cannot pop from empty list"
      if i < 0: 
         raise ValueError, "Input must be non-negative"
      if i >= self.size:
         raise IndexError, "pop index out of range"
      
      try:
         if i == 0:
            item = self.head.item
            self.head = self.head.next
         else:
            currNode = self.head 
            prevNode = None
            for k in range(i+1):
               if k == i:
                  item = currNode.item
                  prevNode.next = currNode.next 
               elif k < i:
                  prevNode = currNode
                  currNode = currNode.next
            if i == (self.size-1):
               self.tail = prevNode
         self.size -= 1
         return item
      except Exception:
         raise IndexError, "pop index is out of range"
      
   
   def insert(self, i, anItem):
      """
      If index is greater, do we add it at the end?
      Precondition: i is an int where 
      0 <= i <= self.size and anItem is any type
      Postcondition: Inserts anItem at the 
      position i, or raises an IndexError if i is too large
      
      """
      if i < 0:
         raise ValueError, "Input must be non-negative"
      if i > self.size:
         raise IndexError, "Index out of range"
      
      try:
         newNode = ListNode(anItem, None)
         if self.size == 0:
            self.head = newNode
            self.tail = newNode
         
         elif i == 0:  
            newNode.next = self.head
            self.head = newNode
         
         else:
            currNode = self.head
            prevNode = None
            for k in range(i+1):
               if k == i:
                  prevNode.next = newNode
                  newNode.next = currNode
               else:
                  prevNode = currNode
                  currNode = currNode.next
         if i == self.size:
            self.tail = newNode
         self.size += 1
         
      except Exception:
         raise IndexError, "Index out of range"
      
      
   def count(self, anItem):
      """
      Precondition: anItem is any type
      Postcondition: Returns the number of times
      anItem appears in the linked list
      """
      currNode = self.head
      x = 0; i = 0
      while currNode != None and i < self.size:
         if currNode.item == anItem:
            x += 1
         i += 1
         currNode = currNode.next
      return x

                  
            
                  
                  
                  
                 
