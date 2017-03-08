# Coins changing problem
# Similar to knapSack problem
import sys
coins=[7,2,3,6]
tot=17

def min_coins(coins,tot):
    n=len(coins)
    DP=[sys.maxint for i in range(tot+1)]
    position=[-1 for i in range(tot+1)]
    DP[0]=0
    for i in range(n):
        for j in range(tot+1):
            if coins[i]<=j:
                DP[j]=min(DP[j],1+DP[j-coins[i]])
                if DP[j]==1+DP[j-coins[i]]:
                    position[j]=i

    return DP[tot],position

min,position= min_coins(coins,tot)

u=17
result=[]
while u>0:
    result.append(coins[position[u]])
    u-=result[-1]

result.reverse()

print min, result

