
def sum_digits(num):
    if num < 10:
        return num
    s = 0
    while num != 0:
        s += num % 10
        num //= 10
    return s

def get_digits(temp):
    a,temp = temp//1000 , temp%1000
    b,temp = temp//100 , temp%100
    c,temp = temp//10 , temp%10
    d,temp = temp//1 , temp%1

    return a,b,c,d

for i in range(1000, 10000):
    if sum_digits(i) == 12:
        a,b,c,d = get_digits(i)
        if a-b == c and a+c == d:
            print(i)
