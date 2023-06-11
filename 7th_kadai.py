import numpy as np
import random

a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
ans = (100 * a) + (10 * b) + c

i = 0
while i <= 5:
    num = int(input('Input number : '))
    x = num // 100
    y = (num % 100) // 10
    z = num % 10
    
    if ans == num:
        print('Your number is right!!')
        break
    else:
        if a != x and b != y and c != z:
            print('Your number is wrong')
        
        if a == x:
            print('100 place is right')
        if b == y:
            print('10  place is right')
        if c == z:
            print('1   place is right')
                     
        if i >= 3 and i <= 4:
            if a > x:
                print('100 place is bigger')
            elif a < x:
                print('100 place is smaller')
            if b > y:
                print('10  place is bigger')
            elif b < y:
                print('10  place is smaller')
            if c > z:
                print('1   place is bigger')
            elif c < z:
                print('1   place is smaller')
        
        if i == 5:
            print("I'm sorry...")

    i = i + 1
