def longestSubstring(str):
    count = 0
    alreadySeen = []
    for i in str:
        if i not in alreadySeen:
            count += 1
            alreadySeen.append(i)
    return count

print(longestSubstring("abcabcbb")) 
print(longestSubstring("bbbbb")) 
print(longestSubstring("")) 
print(longestSubstring("pwwkew")) 
