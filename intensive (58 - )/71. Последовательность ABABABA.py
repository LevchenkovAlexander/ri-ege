s = input()
max_l = 1
l = 1
ans = ""
ans_m = []

for i in range(1, len(s)):
    if (s[i] == "A" and s[i - 1] == "B") or (s[i] == "B" and s[i - 1] == "A"):
        ans += s[i-1]
    else:
        ans += s[i]
        ans_m.append(len(ans)) if ans[0] == "A" else ans_m.append(len(ans) - 1)
        ans = ""
    
    if i == len(s) - 1:
        ans += s[i]
        ans_m.append(len(ans)) if ans[0] == "A" else ans_m.append(len(ans) - 1)
        
    
    
print(max(ans_m))
