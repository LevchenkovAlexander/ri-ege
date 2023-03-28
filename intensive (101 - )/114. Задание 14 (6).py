def scale_of_not(num, base):
    if base == 10: return str(num)
    s = ""
    while num:
        s = str(num % base) + s
        num //= base
    return s


sum_ = 0
for i in range(2, 11):
    num = scale_of_not(609, i)
    if int(num[-1]) % 2 != int(num[0]):
        sum_ += i
print(sum_)