def topKFrequent(nums, k):
        
        count = {}
        freq = [[] for i in range(len(nums) +1)]

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res

nums = [1,1,1,2,2,3] 
k = 2
print(topKFrequent(nums, k))
nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
print(topKFrequent(nums, k))
