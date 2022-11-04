"""
Write a recursive Python program to calculate the value of 'a' to the power 'b'
Test Data :
(power(3,4) -> 81
"""
# 3 ^ 4
# 3 * 3^3
# 3 * 3 * 3^2
# 3 * 3 * 3 * 3^1
# 3 * 3 * 3 * 3

def power(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif a == 0:
        return 0
    else:
        return a * power(a, b-1)

print(power(3,4))
