class Solution:
    def maxProduct(self, nums) -> int:
        """
        （1）思路：
                动态规划，类似与最大子序和的那道题，利用dp数组来表示前i个元素的最大乘积。但是存在的问题是 正数 * 负数会
            导致乘积由最大值变为最小值。所以需要同时维护一个最小值的dp数组，这样就存在两种情况，以 nums[i] 正负区分：
                - nums[i] >= 0, 那么 dp_max[i] = max(dp_max[i-1] * nums[i], nums[i])
                                    dp_min[i] = min(dp_min[i-1] * nums[i], nums[i])
                - nums[i] < 0, 那么 dp_max[i] = max(dp_min[i-1] * nums[i], nums[i])
                                    dp_min[i] = min(dp_max[i-1] * nums[i], nums[i])
                综合两种情况，可以发现，整体可以用下面的式子来表达。
                dp_max[index] = max(max(dp_max[i-1] * nums[i], nums[i]), dp_min[i-1] * nums[i])
                dp_min[index] = min(min(dp_max[i-1] * nums[i], nums[i]), dp_min[i-1] * nums[i])
        （2）复杂度：
            - 时间复杂度：O（n）
            - 空间复杂度：O（n） 如果不存在数组中，以单个变量存储也可以，则为O（1）
        """
        nums_len = len(nums)
        # 处理特殊情况
        if nums_len == 0:
            return 0
        elif nums_len == 1:
            return nums[0]
        else:
            # 初始化result，由于是从1开始遍历，这是初始化为nums[0]
            result = nums[0]
            # 构建dp数组，dp_max和dp_min分别代表前i个元素的最大值和最小值
            dp_max, dp_min = [0] * nums_len, [0] * nums_len
            dp_max[0], dp_min[0] = nums[0], nums[0]
            for index in range(1, len(nums)):
                # 如果nums[index] 大于0
                if nums[index] >= 0:
                    # 前index个元素的最大值就是dp_max[index-1] * nums[index] 和 nums[index] 两者中的较大值
                    # 例如 nums=[-4,3] 那么dp_max[1] = nums[1] = 3 而不是 dp_max[0]*nums[1] = -12
                    dp_max[index] = max(dp_max[index-1] * nums[index], nums[index])
                    # 前index个元素的最小值就是dp_min[index-1] * nums[index] 和 nums[index] 两者中的较小值
                    # 例如 nums=[4,3] 那么dp_min[1] = nums[1] = 3 而不是 dp_min[0]*nums[1] = 12
                    dp_min[index] = min(dp_min[index-1] * nums[index], nums[index])
                else:
                    # 如果nums[index]小于0，那么dp_max[index-1] * nums[index]只会越来越小，所以最大值出现只能是由原来
                    # 最小值乘以现在的负数变成最大值
                    # 例如 nums=[4,-3] 那么dp_max[1] = nums[1] = -3 而不是 dp_min[0]*nums[1] = -12
                    dp_max[index] = max(dp_min[index-1] * nums[index], nums[index])
                    # 例如 nums=[-4,-5] 那么dp_min[1] = nums[1] = -5 而不是 dp_max[0]*nums[1] = 20
                    dp_min[index] = min(dp_max[index-1] * nums[index], nums[index])

                # # 不区分大于0和小于0，那么整体可以写成
                # dp_max[index] = max(max(dp_max[index-1] * nums[index], nums[index]), dp_min[index-1] * nums[index])
                # dp_min[index] = min(min(dp_max[index-1] * nums[index], nums[index]), dp_min[index-1] * nums[index])
                result = max(result, dp_max[index])
            return result

print(Solution().maxProduct([1, -1, 2,3,2,4]))