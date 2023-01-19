def pair_count_f(s):
    s = s.replace(" ", "")
    pair_count = 0
    
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                pair_count += 1
            
    return pair_count


print( pair_count_f( input()))
