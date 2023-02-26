def is_even(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return 0
    return 1


def divs(num):
    cnt = 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if is_even(i): cnt += 1
            if is_even(num//i): cnt += 1
    return cnt
    
    
count = 0
for i in range(2, 20000 + 1):
    if divs(i) > 3: count += 1

print(count)