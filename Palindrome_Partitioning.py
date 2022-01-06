
s = "aabbb"
result = []
a = 0
b = 1

for i in range (len(s)):
    newstring = "".join(s[a])
    reversestring = newstring[::-1]
    if newstring == reversestring:
        result.append(newstring)
        a += 1
a = 0
b = 2
for i in range (len(s)):

    newstring = "".join(s[a:b])
    reversestring = newstring[::-1]
    if newstring == reversestring:
        result.append(newstring)
        a += 1
        b += 1
        
print(result)
