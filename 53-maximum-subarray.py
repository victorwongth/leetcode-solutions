class Solution:

    def kadane(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
  
    def divide_and_conquer(nums, i, j):
        def recursive(nums, i, j):
            if i == j-1:
                return nums[i],nums[i],nums[i],nums[i]
            # we will compute :
            # a which is max contiguous sum in nums[i:j] including the first value
            # m which is max contiguous sum in nums[i:j] anywhere 
            # b which is max contiguous sum in nums[i:j] including the last value
            # s which is the sum of all values in nums[i:j]

            # compute middle index to divide array in two halves
            mid = i+(j-i)//2
            # compute a, m, b, s for left half
            a1, m1, b1, s1 = divide_and_conquer(nums, i, mid)
            # compute a, m, b, s for right half
            a2, m2, b2, s2 = divide_and_conquer(nums, mid, j)

            # combine a, m, b, s values from left and right halves to form a, m, b, s for whole array (bottom up)
            a = max(a1, s1 + a2)
            b = max(b2, s2 + b1)
            m = max(m1, m2, b1 + a2)
            s = s1 + s2
            return a,m,b,s

        _, m, _, _ = divide_and_conquer(nums, 0, len(nums))
        return m
