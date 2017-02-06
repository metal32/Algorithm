# For checking whether paranthesis are balanced or not, we have to use stack data type as, 
# closing symbols match opening symbols in the reverse order of their appearance; they match from the inside out.

from Stacks import Stack

def parChecker(string):
    s=Stack()
    balanced=True
    index=0
    while index<len(string) and balanced:
        symbol=string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                top=s.pop()
                ## we have to see the top that we have removed matches the symbol
                if not matches(top,symbol):
                    balanced=False

        index+=1
    if balanced and s.isEmpty():
        return True
    else:
        return False
def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('((()))'))
print(parChecker('(()(()()))'))
print(parChecker('(()'))

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))