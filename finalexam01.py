def m(i):
    temp = 0
    for j in range(i):
        jj = j + 1
        temp = temp + (pow(-1, jj + 1))/((2*jj)-1)
    temp = temp * 4
    return temp

i = 1
print("i\t\tm(i)")
while i < 999:
    print("{0:d}\t\t{1:f}".format(i,m(i)))
    i = i + 100

