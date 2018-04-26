# a and b are distinct lists that contain the same elements
a = [10, 20, 30, 40]
b = [10, 20, 30, 40]
print('Is ', a, ' equal to ', b, '?', sep='', end=' ')
print(a == b)
print('Are ', a, ' and ', b, ' aliases?', sep='', end=' ')
print(a is b)
# c and d alias are distinct lists that contain the same elements
c = [100, 200, 300, 400]
d = c # Makes d an alias of c
print('Is ', c, ' equal to ', d, '?', sep='', end=' ')
print(c == d)
print('Are ', c, ' and ', d, ' aliases?', sep='', end=' ')
print(c is d)

#9.12

def list_copy(lst):
    result = []
    for item in lst:
        result += [item]
    return result
def main():
    # a and b are distinct lists that contain the same elements
    a = [10, 20, 30, 40]
    b = list_copy(a) # Make a copy of a
    print('a =', a, ' b =', b)
    print('Is ', a, ' equal to ', b, '?', sep='', end=' ')
    print(a == b)
    print('Are ', a, ' and ', b, ' aliases?', sep='', end=' ')
    print(a is b)
    b[2] = 35 # Change an element of b
    print('a =', a, ' b =', b)
main()
