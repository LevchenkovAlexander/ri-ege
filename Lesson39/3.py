def m_func(num):
    divs = []
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divs.append(i)
            divs.append(num//i)
            break
    return divs[1]-divs[0] if len(divs) > 0 else 0


n = 350000
count = 0
nums = {}
while count < 6:
    m = m_func(n)
    if m % 23 == 9: 
        nums[n] = m
        count += 1
    n += 1

for i in range(6):
    print(list(nums.keys())[i], list(nums.values())[i])