'''
Docstring for Dynamic programming.minimum_steps_to_reach_1
function takes n as a input, we need to figure out minimum steps it would require to reach number 1 by following three operations:
- subtract by 1
- divide by 2
- divide by 3 
'''
# Using recursion
def minimum_steps_to_reach_1_recursively(n):
    if n == 1:
        return 0
    steps = minimum_steps_to_reach_1_recursively(n-1)

    if n%3 ==0:
        steps = min(steps, minimum_steps_to_reach_1_recursively(n//3))
    
    if n%2 ==0:
        steps = min(steps, minimum_steps_to_reach_1_recursively(n//2))

    steps = steps +1

    return steps

print(minimum_steps_to_reach_1_recursively(7))


# Using memoization

def minimum_steps_to_reach_1_memoization(n, memo):
    if n == 1:
        return 0
    if memo[n] != -1:
        return memo[n]
    steps = minimum_steps_to_reach_1_memoization(n-1, memo)

    if n%3 ==0:
        steps = min(steps, minimum_steps_to_reach_1_memoization(n//3, memo))
    
    if n%2 ==0:
        steps = min(steps, minimum_steps_to_reach_1_memoization(n//2, memo))

    steps = steps +1
    memo[n] = steps

    return steps
n = 11
memo = [-1] * (n+1)


# Using tabulation
print(minimum_steps_to_reach_1_memoization(n, memo))

def minimum_steps_to_reach_1_tabulation(n):
    if n<=1:
        return 0
    
    memo = [-1] * (n+1)
    memo[1] = 0

    for i in range(2, n+1):
        steps = memo[i-1] + 1

        if i%2==0:
            steps = min(steps, memo[i//2] +1) 
        
        if i%3==0:
            steps = min(steps, memo[i//3] +1) 
        
        memo[i] = steps
    
    return memo[n]

print(minimum_steps_to_reach_1_tabulation(10))