class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        num_len = len(nums)
        _buffer = [0] * num_len
        bbuffer = [False] * num_len
        def backtrack(position):
            if  _buffer in ans:
                return
            if position == num_len:
                ans.append(_buffer[:])
                return
            for n in xrange(num_len):
                if bbuffer[n]:
                    continue
                else:
                    bbuffer[n] = True
                    _buffer[position] = nums[n]
                    backtrack(position+1)
                    bbuffer[n] = False
        backtrack(0)
        return ans
