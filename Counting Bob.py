s = "dahuhudhbobbobbdfweebobwwbobweeejifbobbbob"
count = 0
numcount = 0
x = 0
y = 1
z = 2
length = len (s)
print length

while numcount < length -2:
    if s[x + numcount] == 'b' and s[y + numcount] == 'o' and s[z + numcount] == 'b':
        count += 1
        numcount += 1
    else:
        numcount += 1   
              


"Number of times bob occurs:" + str(count)