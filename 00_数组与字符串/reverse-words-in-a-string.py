class Solution:
    def reverseWords(self, s: str) -> str:
        # strip()去除两端空格，split()默认以任意空白分割，并自动忽略多余的空格
        # 由此得到一个干净的列表
        words = s.strip().split()
        # 反转列表，用空格拼接
        return ' '.join(reversed(words))

        # 注：由于 Python 中字符串是不可变类型，无法高效实现真正的 O(1) 原地解法。
        #     所以进阶部分在 Python 中并不适用