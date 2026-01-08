phone = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
def return_words(s):

    if s == '':
        return ['']
    
    small_words = return_words(s[1:]) 

    my_word = phone[s[0]]

    ans = []

    for char in my_word:

        for word in small_words:
            ans.append(char + word)

    return ans

print(return_words('26'))