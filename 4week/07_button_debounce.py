from gpiozero import Button             # 버튼 입력 클래스
from signal import pause                #메인 실행 흐름 대기

button = Button(                        #입력 객체 생성
    17,                                 # BCM GPIO17 사용
    pull_up=True,                       #내부 풀업: 누르면 LOW
    bounce_time=0.1                     #디바운스 시간 0.1초
)
count = 0 #눌림 횟수의 초기값

def count_press():                      #눌림 이벤트 처리
    global count                        #함수 밖의 count를 수정
    count += 1                          #콜백이 호출될 때 1증가
    print(f"count={count}")             #누적 횟수 출력

button.when_pressed = count_press       #콜백 등록

try:
    pause()                             #프로그램을 유지하며 이벤트 처리
finally:                                #종료 시 자원 정리
    button.close()                      #GPIO 자원 반환