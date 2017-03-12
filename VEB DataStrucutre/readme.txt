'''                                                           Van Embde Boas Trees Theory                                            '''
This data structure support priority queues operations and the running time is O (loglog n) 
while the size of the key is restricted in the range of 0 to n-1 and there can’t be any duplicated keys.
In it instead of superimposing a binary tree on top of the bit vector, we superimpose a tree of degree sqrt (u). 
We use recursive structure. Starting with a universe of size u, we make a structure having u1/2 items which themselves 
holds u1/4 items, which holds structure of u1/8 items and so on, down to base size of 2.
For finding minimum (maximum) you just move to the left (right) most entry having 1 in the summary and then 
do the linear search in cluster for the leftmost (rightmost) point.
For finding Successor (predecessor) you should move to the right (left) in the same cluster if you find an entry with 1 
then it is done otherwise let i=x/sqrt(u) search right(left) of this index in summary and the first position that holds 
1 gives the index of the cluster, search within the cluster for the leftmost (rightmost) point.
We use min and max value to store in each vEB tree to reduce the recursive calls for finding successor and
predecessor and we can easily find min and max too.
Size of u will be power 2k.
Note: Easy explanation of vEB: just think that the number of bit b that you have to store at each level reduced by half,
so the number of level will be log b until it reaches to 1 bit and as we already know b= log u 
so overall complexity is (loglog u).







