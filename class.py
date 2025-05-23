import random
n = int(input('난수 개수를 입력하세요: '))
a = int(input('시작 범위를 입력하세요: '))
b = int(input('끝 범위를입력하세요: '))
bindo = []
example = random.sample(range(a, b + 1), 5)
random_value = [random.randint(a, b) for _ in range(n)]
for i in example:
    bindo.append(random_value.count(i))
print(f'고유 숫자 리스트: {example}')
print(f'빈도 수 리스트: {bindo}')
print('가장 많이 등장한 숫자 Top 3 (동점 포함): \n')
top_values = [] 
while len(top_values) < 3:
    current_max = max(bindo)
    if current_max == 0:  
        break
    for c in range(len(bindo)):
        if bindo[c] == current_max:
            print(f'{example[c]} → {bindo[c]}회')
            bindo[c] = 0  
    top_values.append(current_max)


