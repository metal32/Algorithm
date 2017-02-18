Dynamic Programming is all about memorization, guessing and recursion. 

There are 5 easy steps to solve any program by using dynamic programming:
a) Define a subproblem ...... # of subproblems
b) guess (part of solution) .....# of choices
c) relate subproblem solution .....compute time/subproblem
d) recurse + memorization or build bottom up 
e) solve original problem


For eg: Fibonacci 
a) F(k) for 1<=k<=n .... # of subproblems are n
b) guess: we have to guess nothing in Fionacci as we know for sure. # of choices =1
c) recurrence=> F(k)=F(k-1)+F(k-2) .....time/subprob= O(1)
d) topological order, so total time O(n)
e) F(n) is the original problem, extra time: O(1)
 

The order of complexitiy for finding the shorted path for weighted edges in an acyclic graphs is O(V+E)
while for cyclic graph it is O(V*E)

