# https://codeforces.com/contest/1487/problem/B
# cat_cycle.py

# t = int(input())
# for i in range(t):
#     n, k = map(int ,tuple(input().split(" ")))
#     A = 0
#     B = n
#     for i in range(k):
#         A = A-1 if A > 1 else n
#         B = B+1 if B < n else 1
#         if(A == B):
#             B = B+1 if B < n else 1
#     print(B)


t = int(input())
for i in range(t):
    n, k = map(int ,tuple(input().split(" ")))
    if(n // 2 == 0):
        if(n > k):
            print(n) 
        else:
            times = int(k / n)
            print(k - (times * n) )
 

