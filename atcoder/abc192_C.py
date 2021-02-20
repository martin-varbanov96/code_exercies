
def solve(N, K):
    if(K == 0):
        return N
    f = N
    for _ in range(K):
        numbers = list(map(int, str(f)))
        numbers.sort(reverse=True)
        g_1_string ="".join(map(str, numbers)) 
        g_1 = int(g_1_string)
        g_2 = int(g_1_string[::-1])
        f = g_1 - g_2

    return f
N, K = tuple(map(int, input().split(" ")))

print(solve(N, K))