# String and Numeric Values can operate together with * 
a, b =5, 10
spl = "&"
print(a*b*spl)

# String and String can operate with +
x, y = "5", 2
txt = "@"
print((x + txt)*y)

# Result of division operator with two integers will be float
e, f  = 20, 10
c = e/f
print(c)

# Integer Division with float and int  will give integer but displayed as float
m, n = 1.5, 3
print(m//n)

# Remainder is negative when denominator is negative
A, B = -5, 2
C= A%B
print(C)

A, B = 5, 2
C= A%B
print(C)

A, B = 5, -2
C= A%B
print(C)

