from gpiozero import LED
from time import sleep

# BCM GPIO17 핀을 제어할 객체 생성
led = LED(17)

try:
    print("프로그램 시작: 5회 반복 점멸을 시작합니다.")
    
    # 5회 반복 점멸 루프
    for count in range(5):
        print(f"상태 로그: 점등 (진행 횟수: {count + 1}/5)")
        led.on()
        sleep(1.0) # 1.0초 유지
        
        print(f"상태 로그: 소등 (진행 횟수: {count + 1}/5)")
        led.off()
        sleep(1.0) # 1.0초 유지
        
    print("반복 점멸 완료.")

finally:
    # 프로그램 종료 또는 예외 발생 시 리소스 안전 해제
    print("프로그램 종료: LED 리소스를 정리하고 꺼짐 상태로 복구합니다.")
    led.close()