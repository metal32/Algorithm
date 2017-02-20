""" http://farazdagi.com/blog/2013/weighted-interval-scheduling/ """

                               FOR UNWEIGHTED INTERvAL SCHEDULING
# Greedy algorithm is a myopic algorithm that processes the input one piece at a time with no apparent look-ahead.
# Greedy Interval Scheduling
# STEP1: Use a simple rule to select a request i.
# STEP2: Reject all requests that are incompatible with i.
# Repeat to step 1 and step 2

## For rule: shortest and numerical doesn't work
## This also doesn't work: Find the number of incompatible request for each request and then select the request with the least incompatible requests.

## Complexicity is for sorting O(nlogn) and for selection is O(n) so overall complexicity is O(nlogn).


                               FOR WEIGHTED INTERVAL SCHEDULING
# Using DP instead of greedy approach for solving the weighted interal scheduling
# Subproblem is try every interval as the first one
# Here bisection takes O(logn) for 1 j and for j moving from 0...to n-1 then total O(nlogn)
# We do sorting so to calculate precomputation and it itself will take O(nlogn)
# the recursion itself will be of O(n) 
# SO overall complexicity for the algorithm is O(nlogn)
