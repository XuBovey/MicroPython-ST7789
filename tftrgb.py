from ST7789 import TFT,TFTColor
from machine import SPI,Pin
import time

spi = SPI(1, baudrate=80000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
tft=TFT(spi,16,2,15)
tft.initr()
tft.rgb(True)
# tft.invertcolor(True)
tft.fill(TFT.BLACK)

lcd_w = 240
lcd_h = 240
f1=open('picture1.rgb', 'rb')
f2=open('picture2.rgb', 'rb')

w = 240
h = 240
tft._setwindowloc((0,0), (w - 1,h - 1))
for loop in range (10):
  f1.seek(0)
  for row in range(h):
      rgb = f1.read(480)
      tft._writedata(rgb)

  f2.seek(0)
  for row in range(h):
      rgb = f2.read(480)
      tft._writedata(rgb)

spi.deinit()
