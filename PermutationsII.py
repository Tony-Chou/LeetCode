class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = []
        ll = len(nums)
        _buffer = [0]*ll
        bbuffer = [False]*ll
        return self.backtrack(nums, 0, ll, l, _buffer , bbuffer)
    def backtrack(self, nums, i, ll, l, _buffer , bbuffer):
        if  _buffer in l:
            return
        if i == ll:
            l.append(_buffer[:])
            return
            
        for n in xrange(ll):
            if bbuffer[n]:
                continue
            else:
                bbuffer[n] = True
                _buffer[i] = nums[n]
                self.backtrack(nums, i+1, ll, l, _buffer , bbuffer)
                bbuffer[n] = False
        return l