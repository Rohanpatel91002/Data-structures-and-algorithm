def get_char(n):
    if n<=0 or n>26:
        return ''
    
    return chr(97+n-1)

# solution uses backtarcking
def return_codes(s):
    
    if s=='':
        return ['']
    
    if len(s)==1:
        return [get_char(int(s))]
    
    single_digit = int(s[:1])
    double_digit = int(s[:2])

    small_ans = return_codes(s[1:])
    ans = []

    for code in small_ans:
        ans.append(get_char(single_digit)+code)
    
    if double_digit >=10 and double_digit<=26:
        small_ans_without_double_digit = return_codes(s[2:])
        for code in small_ans_without_double_digit:
            ans.append(get_char(double_digit)+code)

    return ans

print(return_codes("1123"))





