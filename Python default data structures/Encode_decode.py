def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(s):
    res = []
    i = 0

    while i< len(s):
        j = i
        while s[j] != "#":
            j+=1
        length = int(s[i :j])
        i = j +1
        res.append(s[i:j+length+1])
        i= i+length

    return res



strs = ["I", "love", "myself"]
s = encode(strs)
print(s)

d = decode(s)
print(d)