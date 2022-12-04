s = input()

alf0 = "АаУуОоЫыИиЭэЯяЮюЁёЕе"
alf1 = "БбВвГгДдЖжЗзЙйКкЛлМмНнПпРрСсТтФфХхЦцЧчШшЩщ"

count0 = 0
count1 = 0

for sym in s:
    for i in alf0:
        if sym == i:
            count0 += 1
            continue
    for i in alf1:
        if sym == i:
            count1 += 1
            continue

print(f"гласных - {count0}, согласных - {count1}")
