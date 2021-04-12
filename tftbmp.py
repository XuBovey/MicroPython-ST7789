from ST7789 import TFT,TFTColor
from machine import SPI,Pin
import time

spi = SPI(1, baudrate=80000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
tft=TFT(spi,16,2,15)
tft.initr()
tft.rgb(True)
# tft.invertcolor(True)
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
            colorData = bytearray(2*240)
            for row in range(h):
                if flip:
                    pos = offset + (height - 1 - row) * rowsize
                else:
                    pos = offset + row * rowsize
                if f.tell() != pos:
                    dummy = f.seek(pos)
                colorDataIndex = 0
                readBgrNum = 6
                for col in range(0,w,6):
                    bgr = f.read(18)
                    bgrIndex = 0
                    for t in range(6):
                        color = ((bgr[bgrIndex+2] & 0xF8) << 8) | ((bgr[bgrIndex+1] & 0xFC) << 3) | (bgr[bgrIndex+0] >> 3)
                        colorData[colorDataIndex] = color >> 8
                        colorData[colorDataIndex+1] = color
                        colorDataIndex = colorDataIndex + 2
                        bgrIndex = bgrIndex + 3
                tft._writedata(colorData)
spi.deinit()
