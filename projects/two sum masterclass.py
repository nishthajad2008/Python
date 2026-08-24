def two_sum_brute(nums:list[int], target: int)-> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []
print(two_sum_brute(nums = [2, 7, 11, 15] ,target = 26))




