# Node Creation
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class LinkedList:
  def __init__(self):
    # Inintially it be an empty list
    self.head=None


# ==========================================================
    # 1.Insertion
    # 1.1 Insert at begining
  def insert_begin(self,data):
      # step 1: Create a newnode
      new_node=Node(data)
      # step 2: linking the newnode.nxt to the curr.head
      new_node.next=self.head
      # step 3: Update the headnode
      self.head=new_node
# ========================================================= 
    # 1.2 Insert at End
  def insert_end(self,data):
      # step 1: node creation
      new_node=Node(data)
      # step 2: If list is empty
      if self.head is None:
        self.head=new_node
        return
      # step 3: Traverse to last node
      temp=self.head
      while temp.next is not None:
        temp=temp.next
      # step 4: Link the newnode to the last node
      temp.next=new_node
# ============================================================
    # Insert at position
  def insert_pos(self,data,pos):
      # step 1: Node creation
      new_node=Node(data)
      # step 2: If pos=0
      if pos==0:
        new_node.next=self.head
        self.head=new_node
        return
      # step 3:traverse to the (pos-1)th node
      temp=self.head
      for i in range(pos-1):
        if temp is None:
          print("Position Out of Range, Please enter valid one")
          return
        temp=temp.next
      
      # step 4: Linking the node
      new_node.next=temp.next
      temp.next=new_node
# ==================================================
    # 2.Traversal
  def traverse(self):
      temp=self.head

      if temp is None:
        print("List is empty")
        return
      count=0
      while temp is not None:
        print(temp.data,end=" -> ")
        temp=temp.next
        count+=1
      print("None")
      print("The count of linked list is :" ,count)
# ===================================================
    # 3.Deletion
  def delete_begin(self):
    if self.head is None:
      print("List is empty")
      return
    self.head=self.head.next
 # ===================================================
    # Delete at end
  def delete_end(self):
    if self.head is None:
      print("List is empty")
      return
    if self.head.next is None:
      self.head=None
      return
    temp=self.head
    while temp.next.next is not None:
      temp=temp.next
    temp.next=None
# ===================================================
    # Delete at pos
  def del_pos(self,pos):
     if self.head is None:
       print("List is empty")
       return
     if pos==0:
       self.head=self.head.next
       return 
     temp=self.head
     for i in range(pos-1):
         if temp is None:
             print("Position out of range ! ")
             return
         temp=temp.next
         temp.next=temp.next.next
        
  def count(self):
     temp=self.head
     count=0
     while temp is not None:
       temp=temp.next
       count+=1
     return count
        
  def middle(self):
     length=self.count()
     if length ==0:
       return None
     else:
        mid=length//2
        temp=self.head
        for i in range(mid):
            temp=temp.next
        return temp.data
                
def main():
  ll=LinkedList()

  print("Initial List")
  ll.traverse()
  print()

  # Insert at begin
  ll.insert_begin(10)
  ll.insert_begin(20)
  ll.insert_begin(30)
  ll.insert_begin(40)
  ll.insert_begin(50)
  ll.insert_begin(60)

  print("After Inserting at begin")
  ll.traverse()
  print()

  # Insert at end
  ll.insert_end(100)
  ll.insert_end(200)
  ll.insert_end(300)

  print("After Inserting at end")
  ll.traverse()
  print()

  # insert at pos
  print("Insert at Position")
  ll.insert_pos(1000,0)
  ll.insert_pos(2000,1)
  ll.traverse()
  print()
  ll.insert_pos(3000,2)
  ll.traverse()
  print()

  print("Invalid Pos test")
  ll.insert_pos(4000,20)
  ll.traverse()

  print("Deletion at begin")
  ll.delete_begin()
  ll.traverse()
  print()

  print("Deletion at end")
  ll.delete_end()
  ll.traverse()
  
  ll.delete_end()
  ll.traverse()
  ll.delete_end()
  ll.traverse()

  print(ll.middle())
main()