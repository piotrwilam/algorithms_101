### KARATSUBA Algorithm (KA)

# input - numbers to be multiplied, the number of digits is a power of 2

x = 1234
y = 5678

x = str(x)
y = str(y)

L = [x,y]

# div is a function that:
# 1) its argument is a list of pairs of numbers (saved as strings) that are to be multiplied by KA
# 2) div divides the string of the number into two equal parts (i.e. '1234' into '12' and '34')
# 3) makes the proper operations necesarry for KA
# 4) appends six relevant numbers for each pair of arguments into an output list

def div (L):
    l = len (L)
    M = []
    for i in range(0,l,2):
        x, y = L[i], L[i+1]
        k = int(len(x)/2)
        a, b, c, d = x[:-k], x[-k:], y[:-k], y[-k:]         
        a, b, c, d = int(a), int(b), int(c), int(d)
        new_int = [a, c, b, d, a+b, c+d]
        new_str = []
        for item in new_int:
            item = str(item)
            new_str.append(item)
        M.extend(new_str)
    return (M)
        
j = len (x)

# the division of numbers recursively
# the transformation of strings into integers
# making the multiplication on single digit numbers on lowest layer
# remark: in div some of the numbers will have one more digit as there is an operation (a+b) and (c+d) in div
#    in such cases the numbers must be split with bigger part first (i.e. '123' into '12' and '3') to make sure that KA works
#    for the same reason some of numbers on the lowest layer will have two digits not one

while j != 1:         
    L = div(L)
    j = len (L[0])            

L1 = []
for item in L:
    L1.append(int(item))

M = []
l = len (L1)
for k in range (0,l,2):
    w = L1[k] * L1[k+1]
    M.append(w)
        
# going up recursively         
# mul_a completes a single multiplication
# mul_b makes all multiplications on each layer 

def mul_a (i, L):
    w = pow(10,2*i)*L[0] + pow(10,i)*(L[2]-L[0]-L[1]) + L[1]
    return w

def mul_b (i, L):
    N = []
    l = len (L)
    for k in range (0,l,3):
        M = L[k:k+3]
        w = mul_a (i, M)
        N.append(w)
    return (N)

i = 1
while len(M) != 1:
    M = mul_b (i,M)
    i = 2*i

print ('the Karatsuba product of x and y: ', M[0])
