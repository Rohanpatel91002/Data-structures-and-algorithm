def subsequences(s):
    if len(s) == 0:
        return ['']
    
    small_ans = subsequences(s[1:])
    ans = []
    
    for sub in small_ans:
        ans.append(sub)           
        ans.append(s[0] + sub)    
    
    return ans
print(subsequences("abc"))

def sub_sequence(s):

    if len(s) == 0: # our base case
        return ['']
    
    small_list = sub_sequence(s[1:]) # recursion call, we will assume that we will receive ['',b,c,bc] list 

    ansList = []
    ansList.extend(small_list) # adding small list to our anslist

    for subsequence in small_list:
        ansList.append(s[0] + subsequence)
    
    return ansList

print(sub_sequence("Rohan"))