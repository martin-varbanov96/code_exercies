# https://codeforces.com/contest/1490/problem/C
# sum_of_cubes.py

# TOO SLOW
# t = int(input())
# for i in range(t):
#     x = int(input())
#     max_range = int(x ** (1/3)) +1
#     found = False
#     too_big = False
#     print(max_range)
#     for i in range(1, max_range):
#         max_j_range = int((x - (i ** 3)) ** 1/3) + 1
#         print(f"{max_j_range}: max_j_range")
#         for j in range(i,  max_j_range):
#             print(f"i = {i}, j = {j}")
#             result = (i ** 3) + (j ** 3) 
#             if( result <  x):
#                 continue
#             elif(result ==  x):
#                 found = True
#                 break
#             else:
#                 break
#         if(found):
#             break
#     if(found):
#         print("YES")
#     else:
#         print("No")

# NOTE: This solution passes only for PyPy 3.7, Python3 is too slow
def solve(x):
    a = 1
    while(a*a*a < x):
        b_approx = int((x - (a*a*a)) ** (1/3))
        for i in range(-1, 2):
            b = b_approx + i
            result = b*b*b + a*a*a
            if(result > 0):
                if(result == x):
                    return("YES")
        a += 1
    return("NO")

t = int(input())
for i in range(t):
    x = int(input())
    print(solve(x))
# print(solve(35))
# print(solve(703657519796))  