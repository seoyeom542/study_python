print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2.0

print(2**3) # 8
print(5%3) # 2 float가 아닌 int로 출력
print(5//3) # 1 이것도 float가 아닌 int로 출력
print(19//3) # 6

print(10 > 3) # True
print(4 >= 6) # False

print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 < 5)) # True
print((3 > 0) | (3 < 5)) # True

print(2 + 3 * 4) # 14
print((2+3)*4) # 20

number = 2 + 3 * 4
print(number) # 14
number = number + 2
print(number) # 16
number += 2
print(number) # 18
number *= 2
print(number) # 36
number /= 2
print(number) # 18.0
number **= 2
print(number) # 324.0

print(abs(-5)) # 5 절댓값
print(pow(4, 2)) # 16 4^2
print(max(4, 12))
print(min(4, 12))
print(round(2.13)) # 2 반올림

import math
print(math.floor(4.99)) # 버림
print(math.ceil(3.2)) # 올림
print(math.sqrt(16)) # 제곱근
print(math.sqrt(5)) # 2.23606797749979

import random
print(random.random()) # 0.0 ~ 1.0 미만 사이의 임의값 출력
print(random.random() * 10) # 0.0 ~ 10.0 미만 사이의 임의값 출력
print(int(random.random() * 10)) # 0 ~ 10 미만 사이의 임의값 출력
print(int(random.random() * 10) + 1) # 1 ~ 10 미만 사이의 임의값 출력

print(random.randint(1, 100)) # 1 ~ 100 이하 사이의 임의값 출력