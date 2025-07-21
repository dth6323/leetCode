class Solution(object):
    def basicMerge(self, nums1, m, nums2, n):
        for i in range(m,m+n):
            nums1[i] = nums2[-(m+n-i)]
        nums1.sort()
        return nums1
    def Merge2(self, nums1, m, nums2, n):
        tmp=[0]*(m+n)
        i,j,k=0,0,0
        while i<m+n:
            if j==m:
                tmp[i] = nums2[k]
                i+=1
                k+=1
            elif j<m and nums1[j]<=nums2[k]:
                tmp[i] = nums1[j]
                i+=1
                j+=1
                print("i="+str(i)+"j="+str(j))
            elif nums1[j]>nums2[k]:
                tmp[i]=nums2[k]
                i+=1
                k+=1
                print("i="+str(i)+"k="+str(k))
        return tmp
    def Merge3(self, nums1, m, nums2, n):
        if m + n - 1 > 0:
            for i in range(m + n - 1, 0, -1):
                if m > 0 and (n == 0 or nums1[m - 1] >= nums2[n - 1]):
                    nums1[i] = nums1[m - 1]
                    m -= 1
                else:
                    nums1[i] = nums2[n - 1]
                    n -= 1
        # Trường hợp đặc biệt: chỉ có i = 0
        if m + n - 1 == 0:
            if m > 0 and (n == 0 or nums1[m - 1] >= nums2[n - 1]):
                nums1[0] = nums1[m - 1]
            else:
                nums1[0] = nums2[n - 1]
        return nums1

                

s = Solution()
nums1=[0]
m=0
nums2=[1]
n = 1
print(s.Merge3(nums1,m,nums2,n))