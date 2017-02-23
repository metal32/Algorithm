# Find the length of the longest common subsequence in O(m*n)

# We will use DP to solve it
# We wil create a matrix all of all the characters of first string in rows and second string in the columns
# we will initialize the whole first column with 0 and the whole first row with 0

def LCS(string1,string2):
    m=len(string1)
    n=len(string2)
    l=[[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            # Initializing the matrix
            if i==0 or j==0:
                l[i][j]=0
            elif string1[i-1]==string2[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    index=l[m][n]
    sequence=[]
    i=m
    j=n
    while i>0 and j>0:
        if string1[i-1]==string2[j-1]:
            sequence.append(string1[i-1])
            i-=1
            j-=1
        elif l[i-1][j]>l[i][j-1]:
            i-=1
        else:
            j-=1
    sequence.reverse()
    sequence=''.join(map(str,sequence))
    return 'LCS of {} and {} is {} of length {}'.format(string1,string2,sequence,l[m][n])

string1='HIEROGLYPHOLOGY'
string2='MICHAELANGELO'
print LCS(string1,string2)
