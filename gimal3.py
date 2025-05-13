import random
while True:
    n = int(input())
    if 3 <= n <= 6:
        break
prev = []
checked = ["*" for _ in range(n)]
for _ in range(n):
    bingo = []
    while True:
        a = random.randint(1, 36)
        if len(bingo) == n:
            break
        if a not in prev:
            prev.append(a)
            bingo.append(a)
    print(*bingo)
count = 0
while True:
    bingo_count = 0
    action = input()
    r_int = random.randint(1, 36)
    for c in range(len(prev)):
        if prev[c] == r_int:
            prev[c] = "*"
    print(f'{count + 1}. random number: {r_int}')
    count += 1
    
    for i in range(n ** 2):
        if i % n == 0:
            print()
        print(prev[i], end=" ")

    for sero in range(n):
        if prev[sero::n] == checked:
            bingo_count += 1
        
    for garo in range(0, n**2, n):
        if prev[garo:garo + n] == checked:
            bingo_count += 1
            
    if prev[::n+1] == checked:
        bingo_count += 1
        
    if prev[n-1 : n**2 - 1 : n-1] == checked:
        bingo_count += 1

    print("\n", bingo_count)
    
    if action == "0":
        break
    if bingo_count >= 2:
        print('End')
        break


