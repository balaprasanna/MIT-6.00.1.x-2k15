x = int(raw_input('ENTER A NUMBER TO FIND CUBE ROOT'))
x = abs(x)
ans = 0
for ans in range(0, x+1):
    if (ans**3 == x):
        break
if ans**3 != x:
    print(str(x) + 'is not a perfect cube')
else:
    print('Cube root of ' +str(x) +'is '+ str(ans) )