class Node:
	def __init__(self, data):
		self.data = data 
		self.next = None


class LList:
	"""
	Linked list data structure. All methods implemented recursively 
	except insert and delete. 

	This is a linear singly linked list. Doubly linked lists have two pointers
	in each node, one for prior, one for next. Circular linked lists have a head 
	as well as a tail.

	APPLICATIONS:
	- LRU cache in O(1)

	PROS:
	- Great for if you need to do a lot of insertion/deletion (manipulation)
	because you only need to re-direct pointers to add or remove any elements 
	in a linked list. In an array, you'd have to shift all elements down/up. 

	CONS:
	- Not great for accession. It takes O(n) time, as you have to traverse through
	the entire list, in the worst case, to find an item. In arrays, you could 
	do this computationally since the elements in an array are all stored "adjacent"/next
	to one another in memory. You do this by computing the location of the desired element (by index)
	by taking the location of the index position in the list/array and add the offset times
	the size of the data type inside the array. 

	"""

	def __init__(self, data=None):
		self.head = None 
		self.__length = 0 

		if isinstance(data, Node):
			self.head = data 
			self.__updateLength()
		elif data:
			self.head = Node(data)
			self.__updateLength()


	def empty(self, node=None, count=0):
		if count == 0:
			node = self.head 

		if node is None and count == 0:
			return True 
		elif node is None and count > 0:
			return False
		else:
			return self.empty(node.next, count+1)


	def __updateLength(self):
		self.__length = self.length()


	def length(self, node=None, count=0):
		if count == 0:
			## Needs to be here for recursive function
			node = self.head 

		if node is None:
			return count
		else:
			return self.length(node.next, count+1)


	def lengthIt(self):
		count = 0
		curr = self.head
		while curr:
			count += 1
			curr = curr.next 
		return count 


	def insert(self, data, i):
		if not isinstance(data, Node):
			newNode = Node(data)
		else:
			newNode = data

		## Preprocesssing
		if i >= self.length() or i < 0:
			print "Index out of range." 
		elif i == 0:
			newNode.next = self.head 
			self.head = newNode 
			self.next = newNode.next
		else:
			priorNode = None
			currNode = self.head
			count = 0 
			while count < i:
				priorNode = currNode 
				currNode = currNode.next 
				count += 1

			tmp = priorNode.next    ## == currNode
			priorNode.next = newNode 
			newNode.next = tmp  


	def __lastNode(self, node):
		if node.next is None:
			return node 
		else:
			return self.__lastNode(node.next)


	def append(self, data):
		newNode = Node(data)
		if self.empty():
			self.head = newNode 
			self.head.next = newNode.next
		else:
			lastNode = self.__lastNode(self.head)
			lastNode.next = newNode
		self.__updateLength()
		return newNode


	def delete(self, i):
		if i >= self.length() or i < 0:
			print "Index out of range."
		elif self.empty():
			return 
		elif i == 0:
			tmp = self.head.next 	## self.next 
			self.head = tmp 
		else:
			priorNode = None 
			currNode = self.head
			count = 0
			while count <= i:
				priorNode = currNode
				currNode = currNode.next 
				count += 1
			priorNode.next = currNode.next   ## no error since currNode cannot be None


	def push(self, node, lst=None):
		assert(isinstance(node, Node))
		if lst is None:
			node.next = self.head
			self.head = node 
		else:
			node.next = lst
		self.__updateLength()


	def reverse(self):
		"""
		Reverses the linked list. 

		prev: is a pointer to the last node that was appended to a reversed 
		linked list that is being constructed

		curr: a pointer to the new head node in the original list

		next: a pointer to the next node in the original list; the rest of the list

		*** PREVIOUS:
		{data: 1}=> {data: 0}=> None

		*** CURRENT:
		{data: 2}=> {data: 3}=> {data: 4}=> {data: 5}=> {data: 6}=> {data: 7}=> {data: 8}=> {data: 9}=> None
		
		*** NEXT:
		{data: 3}=> {data: 4}=> {data: 5}=> {data: 6}=> {data: 7}=> {data: 8}=> {data: 9}=> None

		"""
		if self.head is None:
			pass
		else:
			prev = None 			## prev is always the head of the reversed list
			curr = self.head
			n = 0
			while curr:
				next = curr.next 	## next points to the head node for the rest of the orig list 
				curr.next = prev    ## curr node is now pushed to front of prev (its now detached from orig list)
				prev = curr 		## the head of reversed list now points to curr node
				curr = next 		## now curr points to the head of the rest of the orig list
			self.head = prev  		## point head to the head node of the reversed list 


	def printt(self, node=None):
		if node is None
			node = self.head

		while node:
			print "{data: %s}=>" % node.data,
			node = node.next
		print "None" 


	def index(self, node):
		try:
			if isinstance(node, Node):
				prev = None
				curr = self.head
				i = 0
				while curr:
					if curr == node:
						return i 
					else:
						prev = curr 
						curr = curr.next
						i += 1 
		except:
			print "ValueError: node is not in list"


	def swap(self, nodeI, nodeJ):
		if nodeI is None or nodeJ is None:
			return 
		else:
			## Check if they nodeI and nodeJ exist in the list
			i, j = self.index(nodeI), self.index(nodeJ)
			## If either are none, then don't swap.
			if (i and j) is not None:
				prev = None
				curr = self.head
				tmp1, tmp2 = Node('-'), Node('-')
				k = 0 
				while curr:
					if curr == nodeI:
						prev.next = tmp1
						tmp1.next = curr.next 
						curr.next = None
						prev = tmp1
						curr = tmp1.next
					elif curr == nodeJ:
						prev.next = tmp2 
						tmp2.next = curr.next 
						curr.next = None 
						prev = tmp2 
						curr = tmp2.next
					else:
						prev = curr 
						curr = curr.next
				self.insert(nodeI, j)
				self.insert(nodeJ, i)
				

	def pop(self, i):
		if self.head is None:
			return 
		elif i == self.__length-1: 
			pass 
		else:

			tmp = None 
			prev = None
			curr = self.head
			count = 0
			while count < i:
				prev = curr
				curr = curr.next 
				count += 1

			tmp = prev.next       		## tmp = curr did not work
			prev.next = curr.next 
			curr.next = None
			print "POP: ***"
			self.printt()
			self.__updateLength()
			return tmp 


	def swap2(self, nodeI, nodeJ):
		if nodeI is None or nodeJ is None:
			return 
		else:
			## Check if they nodeI and nodeJ exist in the list
			i, j = self.index(nodeI), self.index(nodeJ)
			## If either are none, then don't swap.
			if (i and j) is not None:
				if i < j:
					tmpI = self.pop(i)
					tmpJ = self.pop(j-1)
					self.insert(tmpJ, i)
					self.insert(tmpI, j)
			 	elif i > j:
			 		tmpJ = self.pop(j)
			 		tmpI = self.pop(i-1)
			 		self.insert(tmpI, j)
			 		self.insert(tmpJ, i)
			 	return self.printt()

				

if __name__ == "__main__":

	LList = LList()
	print LList.length()

	for x in range(10):
		LList.append(x)

	LList.printt()
	# LList.reverse()
	LList.printt()

	aNode = LList.append(100)
	LList.printt(aNode)

	newNode = Node(25)
	LList.push(newNode)
	LList.printt(newNode)


	newestNode = Node(200)
	print LList.index(aNode)
	print LList.index(newestNode)

	LList.printt()
	A = Node(1000)
	B = Node(2000)
	LList.insert(A, 5)
	LList.insert(B, 9)
	LList.printt()

	LList.swap2(A, B)

	# LList.push(Node(200))
	# LList.pop(0)
