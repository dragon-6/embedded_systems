from gpiozero import LED
from time import sleep

led = LED(17)

def show_ok():
    # 1.0초 켜짐, 1.0초 꺼짐의 느린 반복
    print("시스템 상태 [OK]: 정상 동작 중 (느린 점멸 패턴 적용)")
    led.blink(on_time=1.0, off_time=1.0)

def show_warning():
    # 0.2초 켜짐, 0.2초 꺼짐의 빠른 반복
    print("시스템 상태 [WARNING]: 주의 요망 (빠른 점멸 패턴 적용)")
    led.blink(on_time=0.2, off_time=0.2)

def show_error():
    # 짧게 3번 점멸 후 1.5초 휴지기를 가지는 특수 패턴
    print("시스템 상태 [ERROR]: 오류 발생 (세 번 짧은 점멸 후 대기)")
    led.off()
    for _ in range(3):
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)
    sleep(1.5)

try:
    # 정상 상태 시뮬레이션 (5초 유지)
    show_ok()
    sleep(5)
    
    # 경고 상태 시뮬레이션 (3초 유지)
    show_warning()
    sleep(3)
    
    # 오류 상태 시뮬레이션 (오류 패턴 2회 반복)
    for _ in range(2):
        show_error()

finally:
    print("프로그램 종료: LED 리소스를 정리합니다.")
    led.close()