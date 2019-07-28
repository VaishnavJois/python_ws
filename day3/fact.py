#factorial of a given number
def fact(num):
    return 1 if num==0 else num * fact(num-1)

print(fact(5))