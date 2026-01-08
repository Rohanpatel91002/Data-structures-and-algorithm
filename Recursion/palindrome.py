def is_palindrome(s, start, end):

    if start>=end:
        return True
    
    if s[start] != s[end]:
        return False

    return is_palindrome(s, start +1, end -1)

ans = "aba a"

print(is_palindrome(ans, 0, len(ans)-1))