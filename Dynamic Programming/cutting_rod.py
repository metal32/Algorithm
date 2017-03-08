# You have a rode and you can sell it by cutting it into certain lengths.


def max_profit(values,length):
    n=len(values)
    DP=[[0 for _ in range(length+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,length+1):
            if i>j:
                DP[i][j]=DP[i-1][j]
            else:
                DP[i][j]=max(DP[i-1][j],DP[i][j-i]+values[i-1])

    o=[]
    def compute(i,j):
        if i>0 and j>0:
            if DP[i-1][j]==DP[i][j]:
                compute(i-1,j)
            else:
                o.append(i)
                compute(i,j-i)
    compute(n,length)
    return DP[n][length], o


values=[2,5,7,8]
length=5
print max_profit(values,length)