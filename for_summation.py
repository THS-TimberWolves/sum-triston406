#for Summation code here
def for_summation(x):
    total = 0
    for x in range(0,x+1,1):
        total += x
    return total 
x = int(input())
print(for_summation(x))
