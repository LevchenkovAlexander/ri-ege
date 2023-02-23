def is_even(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


ind = 0

for i in range(2422000, 2422080):
    if is_even(i):
        ind += 1
        print(ind, i)