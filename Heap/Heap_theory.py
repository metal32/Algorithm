"""                                               Heap is an abstract data type  (priority queue)                                         """ 
## Heap is basically an array visualised as nearly complete binary tree 
##Property if Parent[i]=i/2 and left[i]=2i+1 and right[i]=2i+2 where i starts from 0
## Heap can only perform insertions, deletion, max and min and sorting it can't find the next max or the next min easily.
## Advantage of heap on BST is that it consumes less space as it has no pointer.

### maxHeap Property: the key of a node>=the key of it's children
## so we can perform maxHeap to get the maximum number in a an array

### minHeap Property: the key of a node<=the key of it's children
## so we can perform minHeap to get the minimum number in a an array

""" Functions"""
###heap_size: gives the size of the array
###build_max_heap: produces a maxHeap from an unordered array
###max_heapify: Correct a single violation of the heap property in a subtree's root  ###(order complexity O(logn))
###           Pre-condition for using max_heapify is that left and right node should be in maxHeap form

"""Steps of Heap Sort"""
## Convert an array into a maxHeap
"""   build_max_heap: ## Complexity of buil_max_heap is O(n)
          for i=n/2 to 1:   ###n/2 since all A[n/2,n+1/2....n] are leaves in a tree
              max_heapify(A[i])
              """
## Find max elements A[1]
## Swap elements A[n] with A[1] --> So now the max element is at the end of the array
## Discard node n from heap and decreament the size of heap
## New root may violate maxHeap but the children are maxHeap so we can use max_heapify
## Recursion to step 2
## So setp 2 to 5 will have complexitiy of O(nlogn)


            

