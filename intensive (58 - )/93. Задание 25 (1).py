def is_even(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0: return 0
    return 1


ind = 0
for i in range(194441, 196500 + 1):
    if is_even(i) and i % 100 == 93:
        ind += 1
        print(ind, i)