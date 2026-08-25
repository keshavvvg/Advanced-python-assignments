# 1. Memoization Approach (Top-Down)
def fib_memo(n, memo={}):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n not in memo:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]


# 2. Tabulation Approach (Bottom-Up)
def fib_tab(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

n = int(input("Enter n: "))
print("Fibonacci using Memoization:", fib_memo(n))
print("Fibonacci using Tabulation:", fib_tab(n))


#OUTPUT

'''
Enter n: 6
Fibonacci using Memoization: 8
Fibonacci using Tabulation: 8

'''
