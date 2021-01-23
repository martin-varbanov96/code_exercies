# https://leetcode.com/problems/max-consecutive-ones-iii/

import queue


class List(list):
    def __init__(self, *args, **kwargs):
        super(List, self).__init__(args[0])

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        count = 0
        max_count = 0
        len_A = len(A)
        index_queue = queue.SimpleQueue()
        for i in range(len_A):
            if(A[i] == 1):
                count += 1
            elif( K != 0):
                K -= 1
                count += 1
                index_queue.put(i)
            else:
                if(index_queue.empty()):
                    count = 0
                else:
                    first_zero = index_queue.get()
                    index_queue.put(i)
                    count = i - first_zero 
            max_count = max(max_count, count)
        return max_count

if __name__ == "__main__":
    sol = Solution()
    input_list, K = [0,0,1,1,1,1,1,1,1,0,0, 1, 0, 1, 1, 1, 1, 1] , 0
    # input_list, K = [1,1,1,0,0,0,1,1,1,1,0] ,  2 # first example
    # input_list, K = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1] , 3 #2nd example

    result = sol.longestOnes(input_list, K)
    print(result)
