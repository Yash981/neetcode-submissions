class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l = 0
        r = n - 1
        pivot = -1
        while l <= r:
            mid = l + (r-l)//2

            if mid-1 >= 0 and mid + 1 < n:
                leftEle = mountainArr.get(mid-1)
                midEle = mountainArr.get(mid)
                rightEle = mountainArr.get(mid+1)
                if leftEle < midEle > rightEle:
                    if midEle == target:
                        return mid
                    pivot = mid
                    break
                elif leftEle > midEle > rightEle:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                l += 1
        print(pivot)
        left = 0
        right = pivot
        while left <= right:
            mid = left + (right - left)//2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        left2 = pivot+1
        right2 = n-1
        while left2 <= right2:
            mid = left2 + (right2-left2)//2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                left2 = mid + 1
            else:
                right2 = mid - 1
        return -1


        
