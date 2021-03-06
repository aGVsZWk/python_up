# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         l = nums[:k]
#
#         for i in range(k, len(nums)):
#             if nums[i] > min(l):
#                 l.remove(min(l))
#                 l.append(nums[i])
#         return min(l)
#
#
#
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heapq.heapify(nums)
        for i in range(len(nums) + 1 -k):
            t = heapq.heappop(nums)
        return t

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.findKthLargestHelper(nums, 0, len(nums) - 1, len(nums) + 1 - k)

    def findKthLargestHelper(self, nums, p, r, i):
        if p == r:
            return nums[p]
        q = self.randomPartation(nums, p, r)
        k = q - p + 1
        if i == k:
            return nums[q]
        elif i < k:
            return self.findKthLargestHelper(nums, p, q-1, i)
        else:
            return self.findKthLargestHelper(nums, q+1, r, i-k)

    def randomPartation(self, nums, p, r):
        import random
        t = random.randint(p, r)
        nums[r], nums[t] = nums[t], nums[r]
        return self.partation(nums, p, r)

    def partation(self, nums, p, r):
        j = p - 1
        key = nums[r]
        for i in range(p, r):
            if nums[i] <= key:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[j+1], nums[r] = nums[r], nums[j+1]
        return j+1

if __name__ == '__main__':
    s = Solution()
    l = [1, 5, 6, 4, 2, 3]
    t = s.findKthLargest(l, 2)
    print(t)
