def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0

        for num in nums:
            if (num - 1 ) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length +=1
                longest = max(length, longest)
        return longest

# nums = [100,4,200,1,3,2]
# print(longestConsecutive(nums))

