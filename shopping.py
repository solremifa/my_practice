purchase_value = int(input('총 구매 금액: '))
count_return = int(input('총 반품 횟수: '))
count_purchase = int(input('총 구매 횟수: '))
sub_months = int(input('가입 개월 수: '))

msg = '프로그램을 종료합니다.'
# 예외처리
if count_purchase == 0:
    print('오류: 구매 횟수가 0입니다. 반품률을 계산할 수 없습니다.')
    print(msg)
    
elif count_purchase < count_return:
    print('오류: 반품 횟수가 구매 횟수보다 많을 수 없습니다.')
    print(msg)

# 예외가 아닐 경우(올바른 입력)
else:
    return_rate = (count_return / count_purchase) * 100
    
    if return_rate >= 50 or (purchase_value <= 10000 and sub_months <= 3) or count_return >= 10:
        msg = "결과: 위험 고객" 
        
    elif purchase_value >= 2000000 and return_rate <= 10 and count_purchase >= 30 and sub_months >= 12:
        msg = '결과: 우수 고객' 
        
    else: 
        msg = '결과: 일반 고객' 
        
    print(f'반품률: {return_rate:.1f}%')
    print(msg)