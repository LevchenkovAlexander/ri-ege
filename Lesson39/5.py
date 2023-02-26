mask = [None] + ['0'+str(i) for i in range(10)] + [str(i) for i in range(100)]
nums = {}

for x in mask:
    for y in mask:
        a = int(f'12{x if x != None else ""}45{y if y != None else ""}')
        if a < 10**6 and a % 51 == 0:
            nums[a] = a//51

for i in range(len(nums)):
    print(list(nums.keys())[i], list(nums.values())[i])