import time
import board
import busio
import adafruit_dht
import adafruit_ssd1306

from PIL import Image, ImageDraw

# DHT22 초기화
sensor = adafruit_dht.DHT22(
    board.D17,
    use_pulseio=False
)

# OLED 초기화
i2c = busio.I2C(board.SCL, board.SDA)

display = adafruit_ssd1306.SSD1306_I2C(
    128, 64, i2c, addr=0x3C
)

# OLED 화면 출력 함수
def show_screen(lines):

    image = Image.new("1", (128, 64))
    draw = ImageDraw.Draw(image)

    for index, line in enumerate(lines):
        draw.text((0, index * 16), line, fill=255)

    image = image.rotate(180)

    display.image(image)
    display.show()


try:

    while True:

        try:
            # 센서 데이터 읽기
            t = sensor.temperature
            h = sensor.humidity

            # 데이터 검증
            if t is None or h is None:
                raise ValueError("No value")

            if not (-40 <= t <= 80 and 0 <= h <= 100):
                raise ValueError("Out of range")

            # 경고 조건 확인
            if t >= 30 and h >= 70:
                status = "T/H WARNING"

            elif t >= 30:
                status = "TEMP WARNING"

            elif h >= 70:
                status = "HUMID WARNING"

            else:
                status = "NORMAL"

            # 화면 출력
            show_screen([
                f"T: {t:.1f} C",
                f"H: {h:.1f} %RH",
                "Status:",
                status
            ])

        except (RuntimeError, ValueError) as error:

            show_screen([
                "Sensor Error",
                str(error)[:20]
            ])

        time.sleep(2.0)

finally:

    display.fill(0)
    display.show()
    sensor.exit()

    # 프로그램을 종료할 때는 Ctrl + C
    