a = [1, 2, 1, 5, 8, 3, 13, 21, 34, 55, 89]

lessFnums = []

#for x in a:
#    if x<5:
#        print(x)

num = int(input('digite um num\n'))

for x in a:
    if x<num:
        lessFnums.append(x)
        lessFnums.sort()
        #print(x)
print(lessFnums)

