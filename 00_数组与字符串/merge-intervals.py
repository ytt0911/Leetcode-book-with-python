class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按照区间左值大小进行排序
        intervals.sort(key = lambda x: x[0])

        ans = []
        for x in intervals:
            # 如果ans已经不为空，且ans最后一个区间的右边界大于等于x右边界，则可以合并
            if ans and ans[-1][1]>=x[0]:
                ans[-1][1] = max(ans[-1][1], x[1])
            # 否则不合并，直接添加区间到ans
            else: 
                ans.append(x)

        return ans