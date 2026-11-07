import board                    # SCL, SDA 핀 이름
import busio                    # I²C 버스 인터페이스
import adafruit_ssd1306         # OLED 드라이버

i2c = busio.I2C(board.SCL, board.SDA)           # 클록, 데이터 핀 연결
display = adafruit_ssd1306.SSD1306_I2C(         # OLED 객체 생성
    128, 64, i2c, addr=0x3C                     # 가로, 세로 픽셀 수, 버스, 주소
)

display.fill(0)                                 # 메모리의 모든 픽셀 지우기
display.text("Embedded System", 0, 0, 1)        # 첫 줄: 좌상단
display.text("I2C OLED", 0, 16, 1)              # 둘째 줄: y=16
display.text("Hello!", 0, 32, 1)                # 셋째 줄: y=32
display.show()                                  # 버퍼 내용을 실제 화면으로 전송