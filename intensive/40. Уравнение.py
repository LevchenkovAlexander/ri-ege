for n in range(int(365**0.5)):
    for k in range(int(365**0.5)):
        for m in range(int(365**0.5)):
            if 28*n + 30*k + 31*m == 365:
                print(f"({n}; {k}; {m})")
