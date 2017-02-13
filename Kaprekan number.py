## Kaprekar numbers: numbers whose square if divided into left part and right part and then if their sum equals to x then they are kaprekan numbers
## Ex:45 as 45**=2025 left part=20 and right part=25 sum of both, 20+25=45
def kaprekarNumber(x):
    y=str(x**2)
    z=str(x)
    # Right half of the square of x should be of d digits i.e. equal to the digits of x
    # The left half of the square should of d or d-1 digits  
    d=len(z)
    L=len(y)
    if L-d!=0:
        part1=y[:L-d]
        part2=y[L-d:]
    else:
        part1=0
        part2=y
    if int(part1)+int(part2)==x:
        return True
    else:
        return False

# For finding all kaprekan numbers between p and q both inclusive
p=input()
q=input()

alist=[i for i in range(p,q+1) if kaprekarNumber(i)]
print ' '.join(map(str,alist))