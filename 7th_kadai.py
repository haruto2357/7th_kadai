import numpy as np
import random

a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
ans = (100 * a) + (10 * b) + c

i = 0
while i<5:
    num = int(input('Input number : '))
    x = num // 100
    y = (num % 100) // 10
    z = num % 10
    
    if ans == num:
        print('Your answer is right!!')
        break
    else:
        if i <= 2:
            if a == x:
                print('hundreds place is right')
            if b == y:
                print('tens place is right')
            if c == z:
                print('ones place is right')                

    i = i + 1
