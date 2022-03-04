while True:
    nums = input()

    if nums == '0 0 0':
        break

    nums = list(map(int, nums.split()))
    nums.sort()
    answer = 'right' if (nums[0]**2 + nums[1]**2) == nums[2]**2 else 'wrong'
    print(answer)

