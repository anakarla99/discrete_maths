mod = 10**9 + 7 
n = int(input())
f = [0]*(n+1)
f[0] = 1
count = 1
for i in range(1, n+1):
      for j in range (0, i):
            f[(count + j + n + 1)% (n+1)]  = (f[(count - i + j + n + 1) % (n+1)] + f[(count + j +n) % (n+1)]+ mod)% mod
      count = (count + i + n +1) %(n+1)
print(f[(count -1 +n)%(n+1)]) 