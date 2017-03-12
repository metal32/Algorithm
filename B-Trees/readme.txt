B-Trees are balanced search tress designed to work on secondary storage devices or disks.
They are good in minimizing input, output operations.
Every B-tree height is (log n) but in B-Tree the base factor can be very high.
They are used when the data accessing time is more than the data processing time.
As usual a disk rotates at a speed of 7200RPM so it takes around 8 to 11 millisecond to access the data, 
while in silicon memory that are the cache memory takes around 50 nanoseconds. 
In application the branching factor for a B-Tree is between 50 to 2000
In a B Tree we are assuming that any information associated with the key resides in the same node. 
B+ tree stores all the satellite information in the leaves and stores only keys and child pointers in the internal nodes, 
thus maximizing the branching factor of the internal nodes.

B-Tree constraints
A)	Every node except root should has at least t-1 keys and at most 2t-1 keys 
B)	Every node then will have at least t children and at most 2t children
C)	Root of the disk is always in the memory, so we don’t need to perform disk read on root.
Height= log (n+1)/2 base t
