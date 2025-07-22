class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        j=len(s)-1
        for i in range(0,int(len(s)/2)):
            if i == j:
                return s
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            j-=1
        return s
s1 = ["H","a","n","n","a","h"]
s = Solution()
print(s.reverseString(s1))