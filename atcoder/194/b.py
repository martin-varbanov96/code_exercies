# https://atcoder.jp/contests/abc194/tasks/abc194_b
N = int(input())
min_task_A = (10 ** 5 ) + 5
min_task_B = (10 ** 5 ) + 5

result = (10 ** 5) + 1
A = []
B = []
for i in range(N):
    # A_i, B_i = tuple(map(int, input().split(" ")))
    A_i, B_i = tuple(map(int, input().split(" ")))
    A.append(A_i)
    B.append(B_i)

for i in range(N):
    for j in range(N):
        current_value = A[i] + B[j] if i == j else max(A[i], B[j])
        result = min(result, current_value)

print(result) 



