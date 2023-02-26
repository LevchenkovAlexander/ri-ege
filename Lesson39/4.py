count = 0
nums = {}
for x in range(10):
    for y in range(10):
        a = int(f'12345{x}6{y}8')
        if a % 17 == 0:
            nums[a] = a // 17

for i in range(len(nums)):
    print(list(nums.keys())[i], list(nums.values())[i])