import random
from math import gcd

input_list = []
i = 4
while i > 0:
    input_list += [random.randint(1, 2 * 10^9)]
    i -= 1
mcd = gcd(input_list[2], input_list[3])
x = input_list[2]// mcd
y = input_list[3] // mcd
n = 0
while n* x<= input_list[0] and n*y <= input_list[1]:
    n += 1
n -=1
print(str(input_list[0]) + " " + str(input_list[1]) + " " + str(input_list[2]) + " " + str(input_list[3])+ '\n' + str(n*x) + " " + str(n*y))