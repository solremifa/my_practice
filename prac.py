'''
여러 명의 고객 구매 데이터를 받아
고객별 총구매횟수, 총금액, 등급 판정을 출력하는 프로그램을 작성하세요.

✅ 입력 형식
각 입력은 "이름 금액" 형식의 문자열입니다.
"end"가 입력되면 입력 종료

✅ 처리 조건
고객별 총 금액, 구매 횟수 계산

등급 판정 기준:

우수: 총 구매금액 ≥ 30000 and 구매횟수 ≥ 2

일반: 그 외
'''

data = {}

def is_vip(info):
    return info['total'] >= 30000 and info['count'] >= 2


def print_summary(name, info):
    return print(f"{name}: 총 {info['count']}회, {info['total']}원")

while True:
    raw = input(': ')
    if raw == 'end':
        for name, info in data.items():
            if is_vip(info):
                print_summary(name, info)
        break
    name, price = raw.split()
    price = int(price)
    if name not in data:
        data[name] = {'count' : 1, 'total' : price}
    
    else:
        data[name]['count'] += 1
        data[name]['total'] += price

