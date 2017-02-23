'''                     Rabin Karp Algo O(n) n-> length of the text you are looking into                                    '''
# d is the base and q is the prime number
# equation 1: append(val):((u*base)+val)modp = [(u mod p)*base+val] mod p
# equation 2: skip(val):[u-val(base**(u-1)modp)]modp=[(u mod p) - val(base**(u-1) mod p)] mod p
# magic number=base**(u-1) mod p

def RollingHash(text,pattern,d,q):
    n=len(text)
    m=len(pattern)
    magicNumber=pow(d,m-1)%q
    pattern_hash=0
    window_hash=0
    for i in range(m):# pre-processing
        # From equation 1
        pattern_hash=(pattern_hash*d+ord(pattern[i]))%q
        window_hash=(window_hash*d+ord(text[i]))%q
    result=[]
    for s in range(n-m+1):
        if pattern_hash==window_hash:
            # if both the hash values are same then we have to check whether both the character are same or not
            # As in hashing due to the presence of large universe, hash functions sometimes give same value for differenct char
            match=True
            for i in range(m):
                if pattern[i]!=text[s+i]:
                    match=False
                    break
            if match:
                result.append(s)
        if s<n-m:
            # update window hash value
            window_hash=(window_hash-ord(text[s])*magicNumber)%q  ## Equation 2 of skip
            window_hash=(window_hash*d+ord(text[s+m]))%q          ## Equation 1 of append
            widow_hash=(window_hash+q)%q                          # to make sure that window_hash is positive
    return result

print RollingHash("the fox is in the hat and my name is Ayush Mittal the mathematician", "the", 257, 23)

            