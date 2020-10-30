# MicroPython-ST7789

删除了initb()和initb2()函数，用ST7789寄存器地址代替ST7735寄存器地址，修改inittr()函数。根据需要使用反色配置命令.

根据硬件修改了IO口配置。

This is a modified version of [boochow's ST7735.py](https://github.com/boochow/MicroPython-ST7735) ST7735 TFT LCD driver for MicroPython.

This version is for micropython-esp32.

A font file is necessary for displaying text (some font files are in [boochow's repo](https://github.com/boochow/MicroPython/tree/master/lib)).

Text nowrap option added(default: nowrap=False).

graphicstest.py is a sample code. I wrote this to make it similar to [Adafruit's graphicstest sketch for Arduino](https://github.com/adafruit/Adafruit-ST7735-Library/tree/master/examples/graphicstest).

If graphicstest.py doesn't work correctly. You can also change rgb(True) to rgb(False) to switch red and blue pixels if your LCD module shows incorrect colors.

Pin connections:

LCD |ESP32-DevKitC
----|----
VLED|3V3
RST |IO2
A0  |IO16(DC)
SDA |IO13(MOSI)
SCK |IO14(CLK)
VCC |3V3
CS  |IO15
GND |GND

tftbmp.py is another sample similar to [Adafruit's tftbmp sketch for Arduino](https://github.com/adafruit/Adafruit-ST7735-Library/blob/master/examples/spitftbitmap/spitftbitmap.ino).

Place bmp file named 'test240x240.bmp' in the file system of MicroPython using file uploading tool such as [ampy](https://github.com/adafruit/ampy), etc.
