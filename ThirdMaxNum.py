class Solution(object):
    def thirdMax(self, nums):
        First = None
        Second = None
        Third = None
        for num in nums:
            if num == First or num == Second or num == Third:
                continue
            if First == None or num > First:
                Third = Second
                Second = First
                First = num
            else:
                if Second == None or num > Second:
                    Third = Second
                    Second = num
                elif Third == None or num > Third:
                    Third = num
        return Third if Third != None else First 
                    
