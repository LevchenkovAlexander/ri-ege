def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    return 1


def divs(num, k, char = []):
    if k == 2 and is_prime(num): 
        char += [num % 10]
        return sum(char) / len(char) == char[0]
    
    if k > 2: return 0
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if not is_prime(i) and not is_prime(num//i):
                return 0
            
            elif is_prime(i):
                return divs(num//i, k+1, char + [i % 10])
            
            elif is_prime(num//i):
                return divs(i, k+1, char + [num//i % 10])
    
            
ans = []
for i in range(416782, 498324 + 1):
    if divs(i, 0):
        ans.append(i)
print(max(ans) - min(ans))