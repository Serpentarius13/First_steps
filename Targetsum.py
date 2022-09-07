class Solution:
    """ Finds numbers in list that make a sum == target """
    def summa(self, nums, target):
        result = []

        while nums:
            if target - nums[0] in nums:
                a = nums.index(target - nums[0])
                b = nums.index(nums[0])
                result.append(a)
                result.append(b)
                result.sort()
                print(result)
                return result
            else:
                nums.remove(0)


play = Solution()
numbers = [2, 7, 11, 15]
a = play.summa(numbers, 9)


