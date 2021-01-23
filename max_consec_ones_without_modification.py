# https://leetcode.com/problems/max-consecutive-ones/

class List(list):
    def __init__(self, *args, **kwargs):
        super(List, self).__init__(args[0])

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        len_nums = len(nums)
        for i in range(len_nums):
            if(nums[i] == 1):
                count += 1
            else:
                count = 0
            max_count = max(max_count, count)
        return max_count

# class Solution:
#     def longestOnes(self, A: List[int], K: int) -> int:
#         count = 0
#         max_count = 0
#         len_A = len(A)
#         index_queue = queue.SimpleQueue()
#         for i in range(len_A):
#             if(A[i] == 1):
#                 count += 1
#             elif( K != 0):
#                 K -= 1
#                 count += 1
#                 index_queue.put(i)
#             else:
#                 if(index_queue.empty()):
#                     count = 0
#                 else:
#                     first_zero = index_queue.get()
#                     index_queue.put(i)
#                     count = i - first_zero 
#             max_count = max(max_count, count)
#         return max_count

if __name__ == "__main__":
    sol = Solution()
    input_list= [1,1,0,1,1,1]

    result = sol.findMaxConsecutiveOnes(input_list)
    print(result)
