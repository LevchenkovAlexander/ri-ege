for x in range(10):
        a = int(f'3{str(x)}da', 14) + int(f'5{str(x)}a6', 12)
        if a % 81:
            print(a // 81)
            break