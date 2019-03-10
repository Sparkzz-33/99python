class Node:
	def _init_(self, data):
		self.data = data	
		self.next = None
class LinkedList:
	def _init_(self):
		self.head = None
	def printList(self):
		temp = self.head
		temp = temp.next
		while(temp):
			print(temp.data)
			temp = temp.next
list = LinkedList()
i = 1
list.head = Node()
temp = Node()
temp = list.head()
while(i<=10):
	if(temp == None):
		curr = Node()
		curr.data = i
		temp.next = curr
	temp = temp.next

list.printList()