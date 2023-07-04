class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while True:   
            if target > numbers[i] + numbers[j]:
                i += 1
            elif target < numbers[i] + numbers[j]:
                j -= 1
            else:
                return [i + 1, j + 1] 
