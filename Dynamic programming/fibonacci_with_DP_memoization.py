memo = [-1] * (5000+1)

def fibonnacci(n):
    if n<=1:
        return 1

    if memo[n] != -1:
        return memo[n]
    
    fib1 = fibonnacci(n-1)
    fib2 = fibonnacci(n-2)

    memo[n-1] = fib1
    memo[n-2] = fib2

    ans = fib1 + fib2

    memo[n] = ans

    return ans

print(fibonnacci(5000)) 



