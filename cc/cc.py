"""输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。"""
from typing import List


def plusOne(digits: List[int]) -> List[int]:
    l = []
    c = ''
    for i in digits:
        c = c+str(i)
        # print(c)
    for i in str(int(c)+1):
        l.append(i)
    return l




print(plusOne([1, 2, 3]))
