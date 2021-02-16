#dense_array.py
# https://codeforces.com/contest/1490/problem/A

def counter(x, y):
    count = 0
    if(y < x):
        b = x 
        x = y
        y = b
    while(x * 2 < y):
        count += 1
        x *= 2
    return count

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    # a = [int(input()) for i in range(n)]
    count = 0 
    for i in range(1, n):
        count += counter(a[i-1], a[i])
    print(count)
