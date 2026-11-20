s = input("enter a string :")
d = {}
count = 0
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
        count += 1
if count > 0:
    print("Repetition exists")       
else:
    print("Repetition does not exists")