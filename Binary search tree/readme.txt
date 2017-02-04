"""                                     Binary Search Tree is an abstract data type      (priority queue)                                          """
## Arrays has binary search that can be done in O(logn) time but the insertion at the point leads to O(n) so total O(nlogn)
## Similarly in heaps it will take O(n) time to complete the above process i.e. insertion and checking the checkas it insert at the last then 
## you use maxheapify in O(logn) and after that search on the other side makes it total O(n)

### Binary tree property.( Priority Queue)
### Can perform insert, delete, find min/max and find next large or next smaller
### Binary tree node has one key, one left pointer, one right pointer and one parent pointer.
### Binary trees generally has asymtotic time of O(h) where h is the length of the longest path from the root to the leaf.
### Height of any node = {max(height of left child, heightof right child)}+1
### Size of a subtree is maintained by data augmentation 
### Binary trees are required for fast insertion, Balanced Binary trees have insertion in a sorted list of "O(logn)" even after having some kind oc check


###How to keep your trees balanced: By using AVL, AVL using rotation, it rotates the pointer
### Property of AVL tree is that the height of left child and right child differ max by +1 or-1.

### Inorder Transverse has O(n)
### 1 insertions takes O(logn) and all the n insertions will take O(nlogn)
