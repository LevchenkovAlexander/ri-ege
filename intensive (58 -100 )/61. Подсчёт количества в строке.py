str = input()

eng_alf_count = 0
even_num_count = 0
upper_let_count = 0
eng_alf = "qwertyuioplkjhgfdsazxcvbnm"

for i in str:
    if i in "02468":
        even_num_count += 1
        
    if i.lower() in eng_alf:
        eng_alf_count += 1
        
    if i == i.upper() and i.lower() in eng_alf:
        upper_let_count += 1
        
print(even_num_count, eng_alf_count, upper_let_count, sep= '\n')
