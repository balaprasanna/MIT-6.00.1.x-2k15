# LOOP THROUGH X
input = int(raw_input('Number to find square:'))
x = input
ans = 0
iters = x
while (iters != 0):
    ans = ans + x
    iters -= 1
    print(ans)
    print('')
print(str(x)+"*"+str(x)+"="+str(ans))