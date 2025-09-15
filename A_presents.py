n = int(input().strip())
p = list(map(int, input().split()))
ans = [0] * (n + 1)
for i in range(1, n + 1):
    j = p[i - 1]
    ans[j] = i
# Output the result from index 1 to n
result = []
for i in range(1, n + 1):
    result.append(str(ans[i]))
print(" ".join(result))