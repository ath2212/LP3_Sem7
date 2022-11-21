def knapsack(W, wt, val, n):
    mat = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] <= w:
                mat[i][w] = max(val[i-1] + mat[i-1][w-wt[i-1]], mat[i-1][w])
            else:
                mat[i][w] = mat[i-1][w]
    print(mat[n][w])

def recurssion(W, wt, values, val, n):
    if n==0 or W==0:
        return val
    if wt[n-1]>W:
        return val
    else:
        return max(recurssion(W-wt[n-1], wt, values, val+values[n-1], n-1), recurssion(W, wt, values, val, n-1))
    

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack(W, wt, val, n))

print(recurssion(W, wt, val, 0, n))
