
# Make a list containing 100 zeros
v = [0] * 100
print(v)
# User enters x at run time
x = int(input("Enter an integer: "))
# Ensure index is within list bounds
if 0 <= x < len(v):
    v[x] = 1 # This should be fine
else:
    print("Value provided is out of range")
