#armstrong number

def armstrong_num(num):
    res = 0
    num_1 = num
    while num!=0:
        r = num%10
        res = res + r**3
        num //= 10
    return num_1 == res

inp = int(input('Enter a number: '))
if armstrong_num(inp):
    print(f'Given number {inp} is an armstrong number')
else:
    print(f'Given number {inp} is Neil armstrong')