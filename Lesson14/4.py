# я недавно узнал как задавать функии в питоне, и хотел потренироваться

def f(n):
    new = ""
    i = len(n) - 1

    while i > -1:
        new += n[i]
        i -= 1
    return new


print(f(input()))

