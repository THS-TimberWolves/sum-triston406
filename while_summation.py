#while summation code following directions from Readme
def while_summation(summation):
    total = 1
    num = 1
    while  num < summation:
        num += 1
        total += num
    return total 
    

summation = int((input()))



print((while_summation(summation)))
