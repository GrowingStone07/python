

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=Node(value)

        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.length+=1
            return True
    
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def pop(self):

        if self.length==0:
            return None
        else:
            temp=self.head
            pre=self.head
            while(temp.next):
                pre=temp
                temp=temp.next
            self.tail=pre
            self.tail.next=None
            self.length-=1
            if self.length==0:
                self.head=None
                self.tail=None
            return temp.value
        
    def prepend (self,value):
        new_node=Node(value)        

        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.length+=1
            return True
    
    def pop_first (self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp

    def get(self,index):
        if index<0 or index >=self.length :
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp

    def set_value(self,index,value):
        # if index < 0 or index >=self.length:
        #     return None
        # temp=self.head
        # for _ in range(index):
        #     temp=temp.next
        # temp.value=value
        # return temp.value

        #       OR

        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node = Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node        
        self.length+=1
        return True
    
    def remove(self,index):
        if index<0 or index >= self.length:
            return None
        if index==0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        # temp = self.get(index)  -- We wont use this as get() method is O(n)
        temp=prev.next  #It becomes O(1)
        prev.next = temp.next
        temp.next = None
        self.length-=1
        return temp
    
    # def reverse(self):
    #     temp = self.head
    #     self.head=self.tail
    #     self.tail=temp
    #     after = temp.next
    #     prev=None
    #     for _ in range(self.length):
    #         after = temp.next
    #         temp.next=prev
    #         prev = temp
    #         temp=after
         






    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after






                



x= LinkedList(4)
x.append(10)
x.append(20)
x.append(30)
x.append(40)
x.append(50)
x.append(60)


x.print_list()
# print('Before POP')
# # print('hhh')
# # print(f'Before pop {x.pop().value}')
# x.pop()
# x.print_list()
# # print(f'After pop {x.pop().value}')

# print(x.pop())
# print(x.pop())
# print(x.pop())
# print('Before Prepend')
# x.print_list()
# print('After Prepend')
# x.prepend(100)
# x.print_list()
# print('After 2nd Prepend')
# x.prepend(200)
# x.print_list()
# print('After pop First')
# x.pop_first()
# x.print_list() 
# print('After 2nd pop First')
# x.pop_first()
# x.print_list()

# print('Get method value')
# print(x.get(2).value)
# print(x.get(3).value)
# print(x.get(4).value)

# print('Set method value')
# print(x.set_value(2,100))
# print('xyz')
# x.print_list()


# print('After Insertion') 
# x.insert(3,300)
# x.print_list()
# x.insert(7,600)
# x.print_list()


# print('After Remove')
# x.remove(0)
# x.print_list()

print('Reverse list')
x.reverse()
x.print_list()
        