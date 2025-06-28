# Leetcode
Python Solutions for Leetcode.

**附上Leetcode官方学习路线：**
![学习路线](image.png)

## 数组与字符串

| 题目原址 | 难易程度 | 题解 | 解题思路 |
| :----: | :----: | :----: | :----: |
| [1991.寻找数组的中心索引](https://leetcode-cn.com/problems/find-the-middle-index-in-array/) | 💚简单 | [✅](00_数组与字符串\find-the-middle-index-in-array.py) | left_sum + mid_value + right_sum = total,<br>即2*left_sum + mid_value = total,<br>找出第一个满足该式的值即可 |
| [35.搜索插入位置](https://leetcode.cn/problems/search-insert-position/description/) | 💚简单 | [✅](00_数组与字符串\search-insert-position.py) | 二分查找，不断逼近大于等于target的值，最终的左指针位置即为插入位置或匹配位置 |