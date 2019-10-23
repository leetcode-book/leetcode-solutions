import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = list(map(str, nums))

        # 看 b + a，a + b 哪个比较大
        def comp(a, b): return 1 if a + b > b + \
            a else -1 if a + b < b + a else 0
        # 1. 降序
        # 2. 比较的逻辑需要定制，不再是比较大小了
        s.sort(reverse=True, key=functools.cmp_to_key(comp))
        return str(int(''.join(s)))
