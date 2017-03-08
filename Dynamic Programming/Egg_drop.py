def eggDrop(floors,eggs):
    DP=[[0 for _ in range(floors+1)] for _ in range(eggs+1)]
    for i in range(1,eggs+1):
        for j in range(0,floors+1):
            if i==1:
                DP[i][j]=j
            elif j==0:
                DP[i][j]=0
            elif i>j:
                DP[i][j]=DP[i-1][j]
            else:
                choice=[]
                for k in range(1,j+1):
                    choice.append(1+max(DP[i-1][k-1],DP[i][j-k]))
                DP[i][j]=min(choice)
    return DP[eggs][floors]

floors=100
eggs=2
print eggDrop(floors,eggs)