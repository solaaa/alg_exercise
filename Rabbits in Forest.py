# leetcode 781. Rabbits in Forest
class Solution:
    def numRabbits(self, answers):
        table = {}
        for num in answers:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1
        res = 0
        for key in table:
            if table[key]%(key+1) != 0:
                res += (table[key]//(key+1) + 1) * (key+1)
            else:
                res += table[key]
        return res