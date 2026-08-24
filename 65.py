left = 0
seen = set()

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
