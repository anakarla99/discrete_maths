from math import gcd

var = list(map(int, input().split())) 
mcd = gcd(var[2], var[3]) 
s = min(var[0]//(var[2]//mcd), var[1]//(var[3]//mcd)) 
print(str((var[2]//mcd)*s) + ' ' + str((var[3]//mcd)*s)) 