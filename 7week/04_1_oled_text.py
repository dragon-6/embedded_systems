import board
import busio
import adafruit_ssd1306

from PIL import Image, ImageDraw

# I2C 연결
i2c = busio.I2C(board.SCL, board.SDA)

# OLED 객체 생성
display = adafruit_ssd1306.SSD1306_I2C(
    128, 64, i2c, addr=0x3C
)

# 이미지 생성 (128x64, 흑백)
image = Image.new("1", (128, 64))

# 이미지에 글자 작성
draw = ImageDraw.Draw(image)

draw.text((0, 0), "Embedded System", fill=255)
draw.text((0, 16), "I2C OLED", fill=255)
draw.text((0, 32), "Hello!", fill=255)

# 180도 회전
image = image.rotate(180)

# OLED 화면에 출력
display.image(image)
display.show()