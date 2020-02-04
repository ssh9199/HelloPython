A = [ x**2 for x in range(0,10) ]
B = [ 2**x for x in range(1,11) ]
C = [ x for x in A if x % 2 and x >= 0 ]

print(A)
print(B)
print(C)
