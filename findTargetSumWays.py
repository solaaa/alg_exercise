# leetcode 494
# 1. TL
class Solution1:
    def search(self, nums, cur, S):
        if len(nums) == 1:
            if cur + nums[0] == S:
                self.cnt += 1
            if cur - nums[0] == S:
                self.cnt += 1
            return 
        self.search(nums[1:], cur-nums[0], S)
        self.search(nums[1:], cur+nums[0], S)
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.cnt = 0
        self.search(nums, 0, S)
        return self.cnt
#s = Solution1()
#print(s.findTargetSumWays([42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47], 38))

# 2.
# sum(p) - sum(q) = target
# ==> sum(p) = (sum(q) + sum(p) + target)/2
# ==> sum(p) = (sum(nums) + target)/2
# this is a package-problem 
class Solution:
    def findTargetSumWays(self, nums, S):
        # 1. specail situation
        if sum(nums) < S:
            return 0        
        target = (sum(nums) + S)
        if target%2 != 0:
            return 0
        target = target//2
        
        # 2. delete zeros, and count them
        cnt = 0
        k = 0
        while k<len(nums):
            if nums[k] == 0:
                cnt += 1
                del nums[k]
            else:
                k += 1
        # 3. if nums only has zeros
        if nums == []:
            return 2**cnt
        
        # 4. the normal problem (nums[i]>0)
        dp = [0] * (1 + target)
        dp[0] = 1
        if nums[0] <= target:
            dp[nums[0]] = 1
        for i in range(1, len(nums)):
            tmp = dp.copy()
            for j in range(1, target+1):
                if j >= nums[i]:
                    dp[j] = tmp[j] + tmp[j-nums[i]]
                else:
                    dp[j] = tmp[j]
        return dp[-1]*(2**cnt)
s = Solution()
print(s.findTargetSumWays([0,0,0,0,0,0,1,0,0], 1))