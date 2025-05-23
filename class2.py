import random

def simulate_cycle_strategy(n):
    success_count = 0
    for _ in range(n):
        box = random.sample(range(1, 101), 100)
        success = True
        for prisoner in range(1, 101):
            idx = prisoner - 1
            for _ in range(50):
                target = box[idx]
                if target == prisoner:
                    break
                idx = target - 1
            else:
                success = False
                break
        if success:
            success_count += 1
    return success_count

def simulate_random_strategy(n):
    success_count = 0
    for _ in range(n):
        box = random.sample(range(1, 101), 100)
        success = True
        for prisoner in range(1, 101):
            opened = random.sample(range(100), 50)
            found = any(box[i] == prisoner for i in opened)
            if not found:
                success = False
                break
        if success:
            success_count += 1
    return success_count

# --- 메뉴 출력 및 실행 ---
print("==== 100명의 죄수 문제 시뮬레이션 ====")
print("1. 사이클 전략만 실행")
print("2. 무작위 전략만 실행")
print("3. 두 전략 비교 실행")
choice = input("선택 (1/2/3): ")

n = int(input("시뮬레이션 반복 횟수 입력: "))

if choice == "1":
    c = simulate_cycle_strategy(n)
    print(f"\n사이클 전략 성공률: {round(c / n * 100, 2)}%")

elif choice == "2":
    r = simulate_random_strategy(n)
    print(f"\n무작위 전략 성공률: {round(r / n * 100, 6)}%")

elif choice == "3":
    c = simulate_cycle_strategy(n)
    r = simulate_random_strategy(n)
    print(f"\n사이클 전략 성공률: {round(c / n * 100, 2)}%")
    print(f"무작위 전략 성공률: {round(r / n * 100, 6)}%")

else:
    print("잘못된 선택입니다. 1, 2, 또는 3을 입력하세요.")



