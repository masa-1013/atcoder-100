import bisect

def twoSum(nums, target):
        nums_len = len(nums)
        search = sorted(nums)
        
        for i in range(nums_len):
            search_target = target - nums[i]
            
            if (search_target == nums[i]):
                right = bisect.bisect_right(search, search_target)
                left = bisect.bisect_left(search, search_target)
                if (right - left > 1):
                    return [i, nums.index(search_target, i + 1)]
            else:
                other = bisect.bisect_left(search, search_target)
                if (other > nums_len ): continue
                if (search[other] == search_target):
                    return [i, nums.index(search_target)]

nums = list(map(int, input().split()))
target = int(input())

print(twoSum(nums, target))