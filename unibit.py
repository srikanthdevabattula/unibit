def find_two_sum(nums, target):
    results = []
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            results.append([complement, num])
        seen.add(num)
    return results

def merge_array(nums):
    merged_array = sorted(nums)
    return merged_array

def find_double_sum(nums, target):
    results = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        results.append([nums[i], nums[j], nums[k], nums[l]])
    return results

nums = [1, 3, 2, 2, -4, -6, -2, 8]
target = 4
results = find_two_sum(nums, target)
merged_array = merge_array(nums)
double_target = target * 2
double_results = find_double_sum(merged_array, double_target)

#results.
print("First Combination For \"4\":", results)
print("Merge Into a single Array:", merged_array)
print("Second Combination For \"8\":", double_results)

