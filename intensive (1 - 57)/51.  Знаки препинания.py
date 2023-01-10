def _count(string):
    alf = ".,:-!?)\""
    count = 0
    for i in string:
        if i in alf:
            count += 1
    if "\"" in string:
        return count-(s.count("\"") // 2)
    return count


s = input()

print(_count(s))
