
s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))
common = []
for i in s1:
    if i in s2:
        common.append(i)
print(common)




s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))
l = list(set(s1) & set(s2))
print(l)