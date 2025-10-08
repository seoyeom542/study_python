students = ['egiing', 'sori', 'maru']
grades = [1, 3, 2]

print(students[1])
print('len: ', len(students))
print('min: ', min(grades))
print('max: ', max(grades))
print('sum: ', sum(grades))

import statistics # 통계
print('mean: ', statistics.mean(grades)) # 평균

import random
print('choice: ', random.choice(students)) # 랜덤 뽑기