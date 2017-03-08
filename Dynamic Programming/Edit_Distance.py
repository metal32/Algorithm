## Text editing
## how many operations are required to convert a string inot another string
## Operations are addition, deletion, replace


def count(string1,string2):
    n=len(string1)
    m=len(string2)
    DP=[[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                if j==0:
                    DP[i][j]=i
                else:
                    DP[i][j]=j
            else:
                if string1[i-1]==string2[j-1]:
                    DP[i][j]=DP[i-1][j-1]
                else:
                    DP[i][j]=min(DP[i-1][j-1],DP[i][j-1],DP[i-1][j])+1
    o=[]
    def compute(i,j):
        if i>=0 and j>=0:
            if string1[i-1]==string2[j-1]:
                compute(i-1,j-1)
            else:
                if DP[i][j]-1==DP[i-1][j-1]:
                    o.append('replace')
                    compute(i-1,j-1)
                elif DP[i][j]-1==DP[i][j-1]:
                    o.append('delete')
                    compute(i,j-1)
                elif DP[i][j]-1==DP[i-1][j]:
                    o.append('add')
                    compute(i-1,j)
    compute(n,m)
    o.reverse()
    return o,DP[n][m]

string1='xyz'
string2='abcdef'

print count(string1,string2)