# All the peaks have been converted into X
# peaks shouldn't be locate at the border and it's adjacent elements i.e. both right, left, top and bottom should be smaller
n = 4
grid =[[1,1,1,2],[1,10,1,2],[1,8,9,2],[1,2,3,4]]


def peakfind(s,col):
    i=1
    index=[]
    while i<n-1:
        if s[i][col]>s[i-1][col] and s[i][col]>s[i+1][col]:
            index.append(i)
        i+=1
    return index

def peakfind2d(s):
    arr=[]
    col=1
    while col<n-1:
        index=peakfind(s,col)
        i=0
        while i<len(index):
            if s[index[i]][col]>s[index[i]][col-1] and s[index[i]][col]>s[index[i]][col+1]:      
                arr.append((index[i],col))
            i+=1
        col+=1
    return arr

peaks=peakfind2d(grid)
for t in peaks:
    grid[t[0]][t[1]]='X'
for i in grid:
    print ''.join(map(str,i))