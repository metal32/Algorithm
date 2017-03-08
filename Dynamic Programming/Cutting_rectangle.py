
import sys
def wastage(cut,n_row,n_col):
    DP=[[None for j in range(n_col+1)] for i in range(n_row+1)]
    for x in range(1,n_row+1):
        for y in range(1,n_col+1):
            if (x,y) in cut:
                DP[x][y]=0
            else:
                choice=[]
                choice.append(x*y)
                for j in range(1,x):
                    choice.append(DP[j][y]+DP[x-j][y])
                for i in range(1,y):
                    choice.append(DP[x][i]+DP[x][y-i])
                DP[x][y]=min(choice)
    return DP[n_row][n_col]


cut=[(3,1),(2,2)]
print wastage(cut,7,5)


    

        
