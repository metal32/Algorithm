
# Finding median in linear time complexity  O(n) for n>140 and O(1) for n=<140
# This divide and conquer method can be used for finding any kth smallest element in an unsorted array in linear time

STEPS
# First select any x from S elements (now this selection is very important and it has to be done cleverly)
# find the rank of x (let we call it k), where rank of x is the number of elements less than or equal to x
# divide S into two B and C, where B has all the elements smaller than x and C has all the elements greater than x.
# if the rank of x i.e. k is greater than index we have to find then we recurse the same function using elements of C
  and index (i-k) 
# if the rank of x is smaller than index then recurse the funtion using elements of B and index (i)
# if the rank if x i.e. k=i then we found our x and return that value.

## Now how to select x from S (this is the trick here)
# Make n columns each of size 5, if there are 24 elements in S, then there will be 4 colums of size 5 and 1 column of size
  4, so overall 5 columns 
# Now we have to sort each column and find the median for each column, as columns are of fixed size so sorting is
  linear in time
# Find the median of all the medians
# return it as value of x.

