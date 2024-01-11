Full Tree : In Full Tree every Node either points to zero Node or Two Nodes.
Perfect Tree : In the tree every level is complete.
Complete Tree : If the Tree is getting filled from left to right i.e. in a level we have values from left to right.

BST(Binary Search Tree):
For BST adding and removing a node : O(logn)
But for worst possible scenario : O(n) b ut the chance is very less so we are considering O(logn)
lookup() : O(n)
remove() : O(n)
insert() : O(n)


If my requirement is data insertion should be faster and retreival can be managed then LinkedList is better choice than BST.
Because for linkedlist insert is O(1).
