class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList():
    def __init__(self,value):
        new_node= Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node            
        else :
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True
    
    def pop(self):
        if self.length==0:
            return None
        temp=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else :
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return True
    
    def popFirst(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:            
            self.head=temp.next
            self.head.prev=None
            temp.next=None
        self.length-=1
        return temp
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        else:
            if index<self.length/2:
                temp=self.head
                for _ in range(index):
                    temp=temp.next
            else:
                temp=self.tail
                for _ in range(self.length-1,index,-1):
                    temp=temp.prev
        return temp
    
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def insert(self,index,value):
        if index<0 or index>self.length:
            return None
        if index==0:
            return(self.prepend(value))
        if index==self.length:
            return(self.append(value))
        else:
            new_node=Node(value)            
            before=self.get(index-1)
            after=before.next
            new_node.prev=before
            new_node.next=after            
            before.next=new_node
            after.prev=new_node
        self.length+=1
        return True
    
    def remove(self,index):
        if index<0 or index >=self.length:
            return None
        if index == 0 :
            return self.popFirst()
        if index == self.length-1:
            return self.pop()
        temp=self.get(index)

        # Using two other temporary nodes
        # after=temp.next
        # before=temp.prev
        # before.next=after
        # after.prev=before

        #Using only one temporary node i.e. temp

        temp.next.prev=temp.prev
        temp.prev.next=temp.next
        temp.next=None
        temp.prev=None

        self.length-=1
        return temp
    
    def swap_pairs(self):
        # Creating a dummy node to reset my head pointer, A previous node I'll create which'll help me in swaping the nodes
        dummy_node=Node(0)
        dummy_node.next=self.head
        previous_node=dummy_node
        
        # Swap Logic
        while self.head and self.head.next is not None:
            #Intializing first and second node which will be required for swapping the nodes
            first_node=self.head
            second_node=first_node.next
            # Changing the next pointers of the pairs to swap
            previous_node.next=second_node
            first_node.next=second_node.next
            second_node.next=first_node
            # Changing the previous pointers of the pairs to swap
            first_node.prev=second_node
            second_node.prev=previous_node
            # If the next pair is available then shift the previous node, head accordingly which will be helpful fior next iteration
            if first_node.next is not None:
                first_node.next.prev=first_node
                self.head=first_node.next
                previous_node=first_node
        # After the loop is omplete our head is shifted to tail side so we need to bring it back to original position
        self.head=dummy_node.next
        # Detaching the dummy_node to release extra space
        if self.head is not None:
            self.head.prev=None
            
        






my_DLL = DoublyLinkedList(7)
my_DLL.append(10)
my_DLL.append(20)
my_DLL.append(30)
my_DLL.append(40)
# my_DLL.print_list()

# my_DLL.pop()
# print('After POP')
# my_DLL.print_list()

# print(my_DLL.pop())

# print('\nAfter prepend')
# my_DLL.prepend(100)
# my_DLL.print_list()


# print('\nAfter popFirst')
# my_DLL.popFirst()
# my_DLL.print_list()

# print(f'Index 2 : {my_DLL.get(2).value}')
# print(f'Index 4 : {my_DLL.get(4).value}')

# print(f'Setting 100 at 2 ')
# my_DLL.set_value(2,100)
# my_DLL.print_list()

# print('Inserting 100 at 2')
# my_DLL.insert(2,100)
# my_DLL.print_list()


# print('Removing node at inex 2')
# my_DLL.remove(2)
# my_DLL.print_list()

print('Before Swapping the DLL')
my_DLL.print_list()
print('After Swapping the DLL')
my_DLL.swap_pairs()
my_DLL.print_list()