"""                                                       Hashing   (constant time with high probability)                                        """
## Most important data structure 
## insert item, overwrites any existing key. ## delete item  ## search "key" not the item but we can return the item by the given key.

## Simple approach for understanding 
## 1) There is a direct access table i.e. a very big array and the indices of the array are the keys 
## 2) Store items in the aray indexed by key

## Problems:
## 1) Hard to interpret as keys may not be integers
## 2) keys can be gigantic

## Solution for 1st problem
## pre-hash
## It maps your keys to non-negative integers
## python has this pre-hash funciton in the name of hash.

## Solution for 2nd problem i.e. reducing space i.e. hashing function
## reduce the universe of keys(integers) down to reasonable size m for table : hashing function does that we define it by h
## We define a function h which instead of making the whole set of keys just make 2 times or 3 times the exact number of keys being used.
## But it will cause collision among two keys in it.
## There are two ways in which collisions can be handled.
## 1) Chaining (it is a linked list of colliding elements)
## So the worst cas with chaining can be O(n) , but in reality it generally doesn't happens
## 2) Open addressing

## For proving the above statement we have to take an assumption i.e. Simple uniform hashing that is btw not true in reality
## Simple uniform hashing means each key is equally likely to be hashed to any slot of the table, independent of where the other keys hashing.
## There are n keys with m slot so total expected length for 1 key is 1/m so overall it will be n/m and as m is O(n) is this whole will become constant

### HASH FUNCTIONS
###1) DIVISION METHOD
###2) MULTIPLICATION METHOD
###3) UNIVERSAL MEHOD

## Table doubling in which whenver the size of n increases the size m we increase the size of m to 2m and so by amortization 1 insertion become constant
## time, while when the size of n is reduced by m/2 we reduce the size of m by m/4 so again amortization causes 1 deletion in constant time

### How do you search a substring into a string where substring of length s and string of length t
### By simple algorithm if we search, it will take O(s*t),now that's a whole lot of time, so we are gonna use Rolling hash 
### The data abstract type used for it is know as Rolling hash (KARP RABIN ALGORITHM)

### """ Rolling HASH """
# First we create a window of the size of the string we need to search then we move it to the whole string by sliding it one character forward in each step. 
##  STEPS {First append the next character, then pop the first character and in the last make it a hash} total 3 steps 
## hash of key function will be h(k)=K mod m where m will be a random prime number.
### The time for doing all of it is O(1), that's the magic of hashing

### """ KARP RABIN ALGORITHM """ for string matching
### First we compute the hash value of substring and make a hash funciton for it 
### we hash the first s characters in t if it is match then good otherwise we add one character in the end remove one character from the start

### Now moving towards """Open Addressing""" where we don't need to form a link list or worry about two keys having same slot
### It need let space as compare to the first method as it doesn't need pointers.
### First the size that are storing th keys should be greater than the number of elements 
### If m is the size of array having keys and n is the number of elements then the m>=n

### """ Crystographic Hashing"""" used in password storage in which even the administrator can't know your passwords
## Given h(x)=Q it is very difficult to find the x that equals h(x)=Q
## So what it does is that it takes the password x* the password you inserted and hash it in to and it is equal to h(x) and so
## in system x is stored not x*

""" SUMMARY """

## So to maintain a good hash function it should do collision resolution so no two keys will be stored in a same location and
## it should have dynamic size allocation so that our load factor i.e. n/m shouldn't become hughe otherwise the cost will become O(n)
 

