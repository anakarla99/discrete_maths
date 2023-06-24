from math import factorial
import random


input_number = random.randint(1, 4000)
mod = 10**9 + 7
list_fac = [0]*(input_number+1)
for i in range(0, input_number+1):
    list_fac[i] = factorial(i)
 
dp = [0] * (input_number + 1) 
dp[0] = 1
res = 0
 
for i in range(1, input_number + 1):
    cur = 0
    for j in range(0,i):
        cur += (list_fac[i-1]//(list_fac[j]*list_fac[(i-1)-j])) * dp[j]
        cur %= mod
    dp[i] = cur
    res += (list_fac[input_number]//(list_fac[i-1]*list_fac[input_number+1-i])) * dp[i-1]
    res %= mod
print(str(input_number) + '\n' + str(res))