'''

 2. 문제 설명
 - 국어, 영어, 수학 점수를 입력, 세 과목의 평균 점수를 계산
 
 ‣ 합격 조건 (모든 조건을 모두 만족해야 함):
 • 세 과목의 평균 점수가 70점 이상
 • 세 과목 각각의 점수가 모두 40점 이상
 
 ‣ 우수 합격 조건 (아래 조건을 모두 만족하면 우선 적용)
 • 평균 점수가 90점 이상
 • 세 과목 각각의 점수가 모두 80점 이상
 
 - 조건을 판정하여 아래와 같이 출력
 ‣ 우수 합격
 ‣ 합격
 ‣ 불합격
 
 3. 알고리즘 (입력 → 처리 → 출력)
 - 입력 : 국어, 영어, 수학 점수 (int형)
 - 처리 : 평균 계산
         and 조건을 활용한 판정 로직 구성
 - 출력 : 평균 점수(float)와 판정 결과
 
 4. 수식의 간결화 아이디어
 and연산자의 나열에 의하여 지나치게 수식이 길어지는 양상
 -우선 논리연산자의 영향을 받지 않는 평균을 먼저 출력한 뒤, 논리연산자 수식을 건드린다 어떻게?
 -논리연산의 과정을 함수로 리펙토링하여 수식을 간결화->return값 역시 불린값으로 출력->다른 논리연산의 항이 되도록
'''
# 정수 값 입력
input_value1 = int(input("국어 점수: "))
input_value2 = int(input("영어 점수: "))
input_value3 = int(input("수학 점수: "))

average = (input_value1 + input_value2 + input_value3) / 3


def cal_best(a, b, c): # 우수 합격 판별 함수
    return a >= 80 and b >= 80 and c >= 80 # 연산 결과에 따라 참 또는 거짓을 반환
      
def cal_second(a, b, c): # 합격 판별 함수
    return a >= 40 and b >= 40 and c >= 40

print(f'평균: {average:.2f}점') # 평균 출력

msg = "결과: " # 출력값 지정

# 평균이 90 이상이고 판별 함수의 반환값이 참일 때
if average >= 90 and cal_best(input_value1, input_value2, input_value3): 
    msg = '우수 합격' # 결과: 우수 합격 

# 평균이 70 이상이고 판별 함수의 반환값이 참일 때
elif average >= 70 and cal_second(input_value1, input_value2, input_value3):
    msg = '합격' # 결과: 합격

# 위의 조건식의 반환값이 거짓일 때
else:
    msg = '불합격'
    
print(msg)