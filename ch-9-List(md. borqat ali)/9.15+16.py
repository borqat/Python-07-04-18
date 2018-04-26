lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst) # [10, 20, 30, 40, 50, 60, 70, 80]
print(lst[0:3]) # [10, 20, 30]
print(lst[4:8]) # [50, 60, 70, 80]
print(lst[2:5]) # [30, 40, 50]
print(lst[-5:-3]) # [40, 50]
print(lst[:3]) # [10, 20, 30]
print(lst[4:]) # [50, 60, 70, 80]
print(lst[:]) # [10, 20, 30, 40, 50, 60, 70, 80]
print(lst[-100:3]) # [10, 20, 30]
print(lst[4:100]) # [50, 60, 70, 80]

a = [1, 2, 3, 4, 5, 6, 7, 8]
print('Prefixes of', a)
for i in range(0, len(a) + 1):
    print('<', a[0:i], '>', sep='')
print('------------------------------------')
print('Suffixes of', a)
for i in range(0, len(a) + 1):
    print('<', a[i:len(a) + 1], '>', sep='')
