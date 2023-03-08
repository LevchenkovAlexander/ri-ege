def num_of_divs(number):
    count = 2
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            count += 2
        if i**2 == number:
            count -= 1
    return count


n = int(input())
for i in range(n):
    number = int(input())
    print(num_of_divs(number))