Full Tree : In Full Tree every Node either points to zero Node or Two Nodes.
Perfect Tree : In the tree every level is complete.
Complete Tree : If the Tree is getting filled from left to right i.e. in a level we have values from left to right.

<img width="943" alt="image" src="https://github.com/GrowingStone07/python/assets/106248741/a0c0b459-431f-4140-a6c2-da6e21d6e085">

BST(Binary Search Tree):
For BST adding and removing a node : O(logn)
But for worst possible scenario : O(n) b ut the chance is very less so we are considering O(logn)
lookup() : O(n)
remove() : O(n)
insert() : O(n)


If my requirement is data insertion should be faster and retreival can be managed then LinkedList is better choice than BST.
Because for linkedlist insert is O(1).

### Hash Table : 
Its One Way and deterministic. Its not vice versa. Dictionary is a example of Hash table.

**Open Addressing :** ex- Linear Probing which means it'll check for the space and if its available then it'll store the value else it'll check next place.

**Separate Chaining :** Its like storing objects in the same memory. Hash Table table uses linkedlists for separate chaining.
**Hash Method** : O(1)

### Graphs :
Adding Vertex and adding relationships is O(1)


### Heap :
Heap is always a complete Tree(filling left to right).
Max Heap : Max value at top.
Min Heap : Min value at top.

Heaps are not good for search, they are useful to track max/min value which is at the top and to remove them. Its mainly used in priority queue.

Insert or remove in Heap : O(logn)






Big O Comparison:


<img width="456" alt="image" src="https://github.com/GrowingStone07/python/assets/106248741/0308b4d2-7c0c-427f-8acc-df85c86386f6">

<img width="440" alt="image" src="https://github.com/GrowingStone07/python/assets/106248741/5ac2fb16-7207-47e2-9c9e-dda3af26b6a9">

<img width="286" alt="image" src="https://github.com/GrowingStone07/python/assets/106248741/6db6e7d7-6a14-4bff-ae52-520a52067b71">

