from itertools import product

alf = "кор"

prod = [''.join(i) for i in product(alf, repeat= 5)]

print(prod[238-1])
