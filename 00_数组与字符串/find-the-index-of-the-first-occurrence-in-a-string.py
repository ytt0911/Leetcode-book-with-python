class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # haystack的指针
        i = 0
        # needle的指针
        j = 0

        lps = self.lps(needle)

        while i < len(haystack):
            # 如果字符相同
            if haystack[i]==needle[j]:
                # 指针同时后移一位
                i += 1
                j += 1
                # 如果已经对比完了，返回起始索引
                if j==len(needle):
                    return i-j
            # 如果字符不同
            else:
                # 若j不为0，则令其回退到前一个字符
                if j!=0:
                    j = lps[j-1]
                # j为0不能回退，则只能i后移
                else:
                    i += 1
        return -1

    def lps(self, needle):
        # 初始化最长前缀后缀表
        lps = [0]*len(needle)
        # 初始化最长前缀后缀长度为0
        length = 0
        # 从第二个字符（索引为1）开始比较
        i = 1

        while i < len(needle):
            # 如果字符相同
            if needle[i]==needle[length]:
                # 最长前缀后缀长度+1
                length += 1
                lps[i] = length
                i += 1
            # 如果字符不相同
            else:
                # 若最长前缀后缀长度不为0，回退到前一个字符
                if length!=0:
                    length = lps[length-1]
                # 为0则说明没有匹配的前后缀
                else:
                    lps[i] = 0
                    i += 1
        return lps