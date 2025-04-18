# basket = ["apple 3", "tv 1", "banana 10", "monitor 2"]
# baskets = {}
# prices = {"apple": 5000, "tv": 45000, "banana": 3000, "monitor": 30000}
# totals = {}

# for i in basket:
#     something, number = i.split()
#     number = int(number)
#     totals[something] = prices[something] * number
    
# result = [k for k, v in totals.items() if v >= 50000]
# print(sorted(result))


# records = [
#     "Alice 70", "Bob 85", "Alice 91", "Bob 75", "Charlie 90", "Alice 88"
# ]
# total = {}
# for i in records:
#     name, score = i.split()
#     score = int(score)
#     if name not in total or score > total[name]:
#         total[name] = score

# print(total)


'''
여러 학생들의 과목별 성적이 문자열로 주어집니다.
각 항목은 "이름 과목 점수" 형태이며,
같은 학생이 여러 과목에 대해 점수를 받을 수 있습니다.


📋 요구사항
각 학생별 평균 점수를 계산합니다.

평균이 90점 이상이면 "A",
80~89점이면 "B",
70~79점이면 "C",
**그 외는 "F"**로 평가 등급을 매깁니다.

결과는 이름 오름차순으로 정렬된 딕셔너리 형태로 출력합니다

평균은 소수 둘째자리까지 반올림, 출력은 소수 둘째자리까지 (round(평균, 2))
'''

# records = [
#     "Alice math 85", "Bob math 70", "Alice english 90", 
#     "Bob english 88", "Alice science 92", "Bob science 65",
#     "Charlie math 90", "Charlie english 93"
# ]
# total = {}
# answer = {}
# for i in records:
#     name, subject, score = i.split()
#     score = int(score)
#     if name not in total:
#         # total[name] = {subject : score}
#         total[name] = {}
#     total[name][subject] = score
# for name, info in total.items():
#     avg = round(sum(info.values()) / len(info), 2)
#     if avg >= 90:
#         answer[name] = {'avg' : avg, 'grade' : 'A'}
#     elif 80 <= avg <= 89:
#         answer[name] = {'avg' : avg, 'grade' : 'B'}
#     elif 70 <= avg <= 79:
#         answer[name] = {'avg' : avg, 'grade' : 'C'}
#     else:
#         answer[name] = {'avg' : avg, 'grade' : 'D'}

# print(answer)


'''
🎓 문제 배경
어떤 학급에서 학생들의 출석 로그가 문자열로 기록되어 있습니다.
각 항목은 "이름 요일 출결상태" 형식입니다.

출결상태는 다음 중 하나입니다:
P (출석), L (지각), A (결석)

각 학생별로
1. 총 출석 횟수 (P)
2. 총 지각 횟수 (L)
3. 총 결석 횟수 (A)
집계합니다.

학생 이름을 키로 하는 딕셔너리를 생성하여,
각 학생의 출결 통계를 {'P': n, 'L': n, 'A': n} 형태로 저장하세요.

결과는 학생 이름 기준 오름차순 정렬된 딕셔너리로 출력합니다
'''

# logs = [
#     "Alice Mon P", "Alice Tue L", "Alice Wed P", "Bob Mon A",
#     "Bob Tue L", "Bob Wed L", "Charlie Mon P", "Charlie Tue P", "Charlie Wed P"
# ]
# total = {}
# answer = {}
# for i in logs:
#     name, days, stud_id = i.split()
#     if name not in total:
#         total[name] = {'P' : 0, 'L' : 0, 'A' : 0}
#     total[name][stud_id] += 1

# print(total)


# orders = [
#     "Alice latte 2", "Bob espresso 1", "Alice espresso 1",
#     "Alice latte 1", "Bob latte 1", "Charlie americano 2",
#     "Bob espresso 1", "Charlie latte 1"
# ]
# answer = {} #정답 제출용 딕셔너리
# for info in orders: # 받은 리스트 안에서 반복
#     name, order, count = info.split() # 리스트 안의 원소 슬라이싱
#     count = int(count) # 카운트 정수화
#     if name not in answer: # 만약 딕셔너리 안에 이름이 중복되지 않으면
#         answer[name] = {} # 이름을 키로 딕셔너리 할당
#     if order not in answer[name]:
#         answer[name][order] = 0
        
#     answer[name][order] += count

# print(answer)
    
    
    
'''
📋 문제 개요
사용자는 "이름 과목 점수" 형식으로 데이터를 입력합니다.
입력은 "end"가 들어올 때까지 계속됩니다.

📌 목표 요구사항
1. 학생별 총점, 평균, 등급을 출력합니다.

평균 점수 기준으로 다음과 같이 등급 부여:
90점 이상: A
80~89점: B
70~79점: C
그 외: F

2. 과목별 평균 점수를 계산합니다.
3. 전체에서 평균이 가장 높은 과목과 학생을 각각 출력합니다.
'''

students = {}
subjects = {}
avg_dict = {}
sub_dict = {}

def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    else:
        return 'F'

while True:
    raw = input(':')
    if raw == "end":
        print('[\n학생별 성적]')
        for name, info in students.items():
            total_stud = sum(info.values())
            avg = round(total_stud / len(info.keys()), 1)
            avg_dict[name] = avg
            print(f"{name}: 총점 {total_stud}, 평균 {get_grade(avg)}")
            
        print('\n[과목별 평균]')
        
        for sub, score_dict in subjects.items():
            avg_sub = sum(score_dict.values()) / len(score_dict.keys())
            sub_dict[sub] = avg_sub
            print(f"{sub}: {round(avg_sub, 1)}")
            
        print(f'\n[최고 평균 학생]')
        
        most_stud = max(avg_dict, key=avg_dict.get)
        print(f"{most_stud}: {round(avg_dict[most_stud], 1)}")
        
        print(f'\n[최고 평균 과목]')
        
        most_sub = max(sub_dict, key=sub_dict.get)
        print(f"{most_sub} : {round(sub_dict[most_sub]), 2}")
        break
    name, sub, score = raw.split()
    score = int(score)
    if name not in students:
        students[name] = {sub : score}
    else:
        students[name][sub] = score
        
    if sub not in subjects:
        subjects[sub] = {name : score}
    else:
        subjects[sub][name] = score