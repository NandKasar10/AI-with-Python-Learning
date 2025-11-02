class Node :
    def __init__(self, value) : #constructor
         self.value = value
         self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node2.next = node3
node3.next = node4

class SLL:
     def __init__(self):
          self.head = node1

     def traversing(self):
          if self.head == None :
               print("Linked List is empty !!!!")
          else :
               temp = self.head
               while temp != None :
                    print(f"{temp.value} ")
                    temp = temp.next

sll = SLL()
sll.traversing()     
