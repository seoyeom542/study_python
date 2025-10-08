import pandas
house = pandas.read_csv('BostonHousing.csv')

print(house) # 전체 데이터를 요약해서 출력
print(house.head()) # 0번째부터 5줄 출력
print(house.head(2)) # 0번째부터 a줄 출력

print(house.describe()) # csv 전체 데이터를 요약 및 정리해서 출력