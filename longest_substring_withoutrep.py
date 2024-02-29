left = 0
right = 0
st = set()
longest = 0
s = "abcabcbb"
n = len(s)

while right < n:
    if s[right] not in st:
        st.add(s[right])
        right += 1
        longest = max(longest, right - left)
    else:
        st.remove(s[left])
        left += 1

print(longest)
