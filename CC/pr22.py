def distinctSubstring(s):
    substring = set()
    for i in range(len(s)):
        for j in range(len(s)):
            substring.add(s[i:j])
    return substring


inputString = "abababa"
ans = distinctSubstring(inputString)

print(ans)