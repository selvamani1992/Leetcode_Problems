class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0 
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n -= 1
        else:
            while i < len(flowerbed):
                if i == 0:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                elif i == len(flowerbed)-1:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                        n -= 1
                elif flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                i += 1
        if n > 0:
            return False
        else:
            return True