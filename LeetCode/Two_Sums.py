def two_sums(nums, target):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []
results = two_sums(nums = [1,2,3,4,5,6,7,8,9,0], target = int(input("Enter you target: ")))
print(results)
