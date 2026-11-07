import time
from datetime import datetime

import board
import adafruit_dht

sensor = adafruit_dht.DHT22(board.D17, use_pulseio=False)

success = failure = 0                   # 누적 집계는 반복문 밖에서 초기화

try:
    for count in range(1, 11):          # 총 10회 측정
        now = datetime.now().strftime("%H:%M:%S")
        try:
            t = sensor.temperature      # 온도(℃)
            h = sensor.humidity         # 상대습도(%RH)
            if t is None or h is None:  # 값이 없는지 먼저 검사
                raise ValueError("값 없음")
            if not (-40 <= t <= 80 and 0 <= h <= 100):   # 범위 검사
                raise ValueError("범위 초과")
            success += 1                # 검사를 모두 통과한 경우만 성공 집계
            print(f"[{count:02d}] {now} | 정상 | {t:.1f} ℃ | {h:.1f} %RH")
        except RuntimeError as error:   # 센서 읽기 실패
            failure += 1
            print(f"[{count:02d}] {now} | 재시도 | {error}")
        except ValueError as error:     # None 또는 범위 검사 실패
            failure += 1
            print(f"[{count:02d}] {now} | 제외 | {error}")
        time.sleep(2.0)                 # 실패해도 2초 뒤 다음 측정으로 진행
finally:
    sensor.exit()                       # 어떤 경우에도 센서 자원 정리

print(f"성공 {success}회, 실패 {failure}회")