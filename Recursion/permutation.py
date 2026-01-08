def return_permutation(s):

    if s == '': # base case
        return ['']
    
    small_ans = return_permutation(s[1:])
    ans = []

    for permutation in small_ans:

        for position in range(0,len(permutation)+ 1):

            ans.append(permutation[0:position] + s[0] + permutation[position:])
        
    
    return ans

print(return_permutation('abc'))



# for the understanding

#  permutation = [1,2,3]
#  print(permutation[0:0])
# this gives [] answer
