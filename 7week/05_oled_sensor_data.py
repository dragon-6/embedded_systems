import board
import busio
import adafruit_ssd1306

from PIL import Image, ImageDraw

# I2C 초기화
i2c = busio.I2C(board.SCL, board.SDA)

# OLED 객체 생성
display = adafruit_ssd1306.SSD1306_I2C(
    128, 64, i2c, addr=0x3C
)

# 가상 온도 및 습도 데이터
temperature = 25.4
humidity = 61.2

# 이미지 생성
image = Image.new("1", (128, 64))
draw = ImageDraw.Draw(image)

# 화면에 데이터 표시
draw.text((0, 0), "Temperature", fill=255)
draw.text((0, 16), f"{temperature:.1f} C", fill=255)

draw.text((0, 34), "Humidity", fill=255)
draw.text((0, 50), f"{humidity:.1f} %RH", fill=255)

# 화면 180도 회전
image = image.rotate(180)

# OLED에 출력
display.image(image)
display.show()