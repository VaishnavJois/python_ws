#filter
#ls1 = divisible by 5
#ls2 = prime numbers
nums = [i for i in range(1,201)]

ls1 = list(filter(lambda x:x%5 == 0,nums))


def is_pr(num):
    if num < 2:
        return False
    
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    return True
    
ls2 = list(filter(is_pr,nums))

print(f'ls1 : {ls1} \n')

print(f'ls2 : {ls2} \n')