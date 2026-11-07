import time
import board
import busio
import adafruit_dht
import adafruit_ssd1306

from PIL import Image, ImageDraw

# -----------------------------
# 1. DHT22 센서 초기화
# -----------------------------
sensor = adafruit_dht.DHT22(
    board.D17,
    use_pulseio=False
)

# -----------------------------
# 2. OLED 초기화
# -----------------------------
i2c = busio.I2C(board.SCL, board.SDA)

display = adafruit_ssd1306.SSD1306_I2C(
    128, 64, i2c, addr=0x3C
)

# -----------------------------
# 3. OLED 화면 출력 함수
# -----------------------------
def show_screen(line1, line2):

    image = Image.new("1", (128, 64))
    draw = ImageDraw.Draw(image)

    draw.text((0, 8), line1, fill=255)
    draw.text((0, 32), line2, fill=255)

    # 180도 회전
    image = image.rotate(180)

    display.image(image)
    display.show()


# -----------------------------
# 4. 센서 측정 및 화면 출력
# -----------------------------
try:

    while True:

        try:
            # 온도 및 습도 읽기
            t = sensor.temperature
            h = sensor.humidity

            # 측정값 검증
            if t is None or h is None:
                raise ValueError("No value")

            if not (-40 <= t <= 80 and 0 <= h <= 100):
                raise ValueError("Out of range")

            # 정상 데이터 출력
            show_screen(
                f"T: {t:.1f} C",
                f"H: {h:.1f} %RH"
            )

        except (RuntimeError, ValueError) as error:

            # 오류 발생 시 화면 출력
            show_screen(
                "Sensor Error",
                str(error)[:20]
            )

        # 2초 대기
        time.sleep(2.0)

finally:

    # 프로그램 종료 시 정리
    display.fill(0)
    display.show()
    sensor.exit()

    # 프로그램을 종료할 때는 Ctrl + C