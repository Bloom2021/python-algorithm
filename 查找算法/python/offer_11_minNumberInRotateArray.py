# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here

        pre = rotateArray[0]

        for val in rotateArray[1:]:
            if pre > val:
                return val
            pre = val
        
        return rotateArray[0]


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0

        left = 0
        right = len(rotateArray) - 1

        while rotateArray[left] >= rotateArray[right]:

            if right - left == 1:
                return rotateArray[right]
            
            mid = (left + right) // 2

            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            
            if rotateArray[mid] <= rotateArray[right]:
                right = mid
                
        return rotateArray[right]
            

