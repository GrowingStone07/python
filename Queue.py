class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    
    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def enqueue(self,value):
        new_node=Node(value)
        if self.first is None: # OR if self.length==0:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1
        return True
    
    def dequeue(self):
        if self.length==0:
            return None
        temp=self.first
        if self.length==1:
            self.first=None
            self.last=None
        else:
            self.first=temp.next
            temp.next=None
        self.length-=1
        return temp




my_queue=Queue(4)
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(40)
my_queue.print_queue()

print('After 1st Deque')
my_queue.dequeue()
my_queue.print_queue()
print('After 2nd Deque')
my_queue.dequeue()
my_queue.print_queue()