from gpiozero import PWMLED
from time import sleep

# 일반 LED가 아닌 PWM 제어를 위한 객체 생성
led = PWMLED(17)

try:
    print("프로그램 시작: PWM 밝기 단계별 제어를 시작합니다.")
    
    # 듀티비(밝기 비율)를 0.0부터 1.0까지 25% 단위로 설정
    # 0.0은 완전 소등, 1.0은 최대 밝기
    for value in [0.0, 0.25, 0.5, 0.75, 1.0]:
        led.value = value
        print(f"상태 로그: 현재 설정된 밝기(듀티비) = {value * 100}%")
        sleep(2) # 각 밝기 단계를 2초간 유지
    
    print("페이드 인/아웃(숨쉬기 효과) 제어로 전환합니다.")
    
    # 1초 동안 서서히 밝아지고, 1초 동안 서서히 어두워짐을 반복
    led.pulse(fade_in_time=1.0, fade_out_time=1.0)
    print("상태 로그: 숨쉬기 모드 동작 중...")
    
    sleep(6) # 펄스 효과를 6초 동안 감상하도록 유지

finally:
    # 프로그램 종료 시 리소스 해제
    print("프로그램 종료: PWM LED 리소스를 정리합니다.")
    led.close()