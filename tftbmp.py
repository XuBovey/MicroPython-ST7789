from ST7789 import TFT,TFTColor
from machine import SPI,Pin
import time

spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
tft=TFT(spi,16,2,15)
tft.initr()
tft.rgb(True)
tft.invertcolor(True)
tft.fill(TFT.BLACK)

# print("black")
# time.sleep(5)
# tft.fill(TFT.WHITE)
# print("white")
# time.sleep(5)
# tft.fill(TFT.RED)
# print("red")
# time.sleep(5)
# tft.fill(TFT.GREEN)
# print("green")
# time.sleep(5)
# tft.fill(TFT.BLUE)
# print("blue")
# time.sleep(5)
# tft.fill(TFT.YELLOW)
# print("yellow")
# time.sleep(5)

lcd_w = 240
lcd_h = 240
f=open('test240x240.bmp', 'rb')

if f.read(2) == b'BM':  #header
    dummy = f.read(8) #file size(4), creator bytes(4)
    offset = int.from_bytes(f.read(4), 'little')
    hdrsize = int.from_bytes(f.read(4), 'little')
    width = int.from_bytes(f.read(4), 'little')
    height = int.from_bytes(f.read(4), 'little')
    if int.from_bytes(f.read(2), 'little') == 1: #planes must be 1
        depth = int.from_bytes(f.read(2), 'little')
        if depth == 24 and int.from_bytes(f.read(4), 'little') == 0:#compress method == uncompressed
            print("Image size:", width, "x", height)
            rowsize = (width * 3 + 3) & ~3
            if height < 0:
                height = -height
                flip = False
            else:
                flip = True
            w, h = width, height
            if w > lcd_w: w = lcd_w
            if h > lcd_h: h = lcd_h
            tft._setwindowloc((0,0),(w - 1,h - 1))
            for row in range(h):
                if flip:
                    pos = offset + (height - 1 - row) * rowsize
                else:
                    pos = offset + row * rowsize
                if f.tell() != pos:
                    dummy = f.seek(pos)
                for col in range(w):
                    bgr = f.read(3)
                    tft._pushcolor(TFTColor(bgr[2],bgr[1],bgr[0]))
spi.deinit()
