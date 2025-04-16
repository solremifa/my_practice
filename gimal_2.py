'''
1. 입력 받기
- 사용자로부터 크기 N을 입력받는다. N은 3 이상 6 이하의 정수여야 한다
- 유효하지 않은 값이 입력될 경우, 올바른 값이 입력될 때까지 재입력
2. 빙고 보드 생성:
- N x N 크기의 빙고 보드를 위해 1차원 리스트를 생성
- 이 리스트는 1부터 36 사이의 중복되지 않은 정수로 채워진다
3. 보드 출력:
- 생성된 리스트를 사용하여 N x N 형태의 빙고 보드를 출력한다
4. 난수 발생 및 게임 진행:
- 사용자가 엔터 키를 누르면, 1부터 36사이 난수를 발생시키고 화면에 출력한다
- 화면에 출력된 난수와 일치하는 보드 상의 숫자는 *로 대체된다
- 매 난수 발생 시 게임 실행 횟수를 출력
5. 빙고 확인:
- 보드에서 가로, 세로, 또는 대각선(양방향)을 포함하여, 최소 2개 이상의
줄에서 모든 숫자가 *로 대체되면 빙고가 성립된다
- 2개 이상의 빙고 줄이 완성되면 사용자가 승리
'''
import random
bingo = []
bar = ""
count = 0
garo_count = 0
sero_count = 0
daegak_count1 = 0
daegak_count2 = 0
bingo_count = 0
new_text = ""
answer = []
num = 0
running = True

while running:
    raw = int(input('Enter the size of the bingo board (3 to 6): '))
    if raw < 3 or raw > 6:
        print('Size must be between 4 and 6. Please try again.')
        continue
    
    while True:
        rInt = random.randint(1, 36)
        if rInt not in bingo:
            bingo.append(rInt)
            count += 1
        if count == raw * raw:
            count = 0
            break
            
        
    for i in bingo:
        bar += (str(i) + " ")
        count += 1
        if count == raw:
            bar += "\n"
            count = 0
    
    print(bar)
    while True:
        num += 1
        bingo_count = 0
        answer = []
        input('Press Enter to generate a random number: ')
        rd = random.randint(1, 36)
        print(f'Random Number {num}: {rd}')
        token = ""
        for char in bar:
            if char == " ":
                if token == str(rd) or token == "*":
                    answer.append(1)
                    new_text += "* "
                else:
                    answer.append(0)
                    new_text += token + " "
                token = ""
            elif char == "\n":
                new_text += "\n"
            else:
                token += char

            
        for r in range(raw):
            garo_count = 0
            for c in range(raw): # 가로 판별 코드
                idx = r * raw + c
                if answer[idx] == 1:
                    garo_count += 1
            if garo_count == raw:
                bingo_count += 1
        
        for y1 in range(0, raw):
            sero_count = 0        
            for y in range(y1, len(answer), raw): # 세로 판별 코드
                if answer[y] == 1:
                    sero_count += 1
                    if sero_count == raw:
                        bingo_count += 1
                        sero_count = 0
                else:
                    sero_count = 0
                
        daegak_count1 = 0
        for i in range(raw): # 대각선 1
            idx = i * (raw + 1)
            if answer[idx] == 1:
                daegak_count1 += 1
        if daegak_count1 == raw:
            bingo_count += 1
                
        daegak_count2 = 0
        for i in range(raw): # 대각선 2
            idx = (i + 1) * (raw - 1)
            if answer[idx] == 1:
                daegak_count2 += 1   
                   
        print(f"\n{new_text}")
        print(f'bingo_count: {bingo_count}')
        bar = new_text
        new_text = ""
        
        if bingo_count >= 2: 
            print('Bingo!')
            running = False
            break
        
        
        
    