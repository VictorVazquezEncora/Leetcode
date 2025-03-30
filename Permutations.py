class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cur_per = []
        res = []

        def backtrack():
            if len(cur_per) == len(nums):
                res.append(cur_per[:])
                return

            for num in nums:
                if num not in cur_per:
                    cur_per.append(num)
                    backtrack()
                    cur_per.pop()

        backtrack()
        return res