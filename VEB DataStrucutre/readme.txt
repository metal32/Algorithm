'''                                                           Van Embde Boas Trees Theory                                            '''
# One of the most used data-structures in network routing tables O(loglogu) complexity for insert, delete and successor operations
# It is exponential times faster than balanced binary search trees

## It is not practically used in many places despite being very good running time as the running time is for universe so 
## If we are not having many elements especially in the range of 2**20 then this algo will be very inefficient as the universe is 2**32

""" General STEPS """
# Bit vector of size u O=Absent and 1=Present
# Split universe in square root of u (sqrt(u)) clusters, of size sqrt(u)
# Summary vector is the list of all the decisions of all the clusters, so if there are total 4 clusters then summary vector size will be 4.
# For ex u=16 now we have divided it into 4 cluster of size 4 eac h 
# and the summary vector has the decision of all the clusters so it will be of size 4

## So any integer can be represented in the form of  x=i*sqrt(u)+j, where i the cluseter and j is the element in the cluster
## So 9 can be represented as =2*4+1 ; where u =16 so sqrt(u)=4 so i=2 and j=1 where cluster and its elements index starts from 0.

''' Steps for inserting '''
##for inserting a number first find the cluster by diving the number by sqrt(u) like what we did in our above example =>  high(x)=x//sqrt(u)
## and the remainder to be the position to be stored in that cluster => low(x)=x%sqrt(u) 







