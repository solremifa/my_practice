  
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